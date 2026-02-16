#!/usr/bin/env python3
"""
Quantum Bloch Sphere Challenge Generator
Encodes a message into qubit states on the Bloch sphere.

Each character is mapped to a quantum state |ψ⟩ = α|0⟩ + β|1⟩ where:
  - θ (polar angle) encodes the ASCII value: θ = ASCII * π / 128
  - φ (azimuthal angle) is a deterministic scatter: φ = ((ASCII * 37 + 17) % 128) * 2π / 128
  - α = cos(θ/2)
  - β = e^(iφ) · sin(θ/2) = cos(φ)·sin(θ/2) + i·sin(φ)·sin(θ/2)

To decode: extract θ = 2·arccos(α), then ASCII = round(θ · 128 / π)
"""

import math
import json


def encode(message):
    """Encode a message into quantum states on the Bloch sphere."""
    states = []
    for i, ch in enumerate(message):
        a = ord(ch)
        theta = a * math.pi / 128
        phi = ((a * 37 + 17) % 128) * 2 * math.pi / 128

        alpha = math.cos(theta / 2)
        beta_r = math.sin(theta / 2) * math.cos(phi)
        beta_i = math.sin(theta / 2) * math.sin(phi)

        bx = math.sin(theta) * math.cos(phi)
        by = math.sin(theta) * math.sin(phi)
        bz = math.cos(theta)

        states.append({
            'index': i,
            'theta': round(theta, 6),
            'phi': round(phi, 6),
            'alpha': round(alpha, 6),
            'beta_real': round(beta_r, 6),
            'beta_imag': round(beta_i, 6),
            'bloch_x': round(bx, 6),
            'bloch_y': round(by, 6),
            'bloch_z': round(bz, 6),
        })
    return states


def decode(states):
    """Decode quantum states back to a message."""
    chars = []
    for s in states:
        alpha = s['alpha']
        theta = 2 * math.acos(min(1.0, max(-1.0, alpha)))
        ascii_val = round(theta * 128 / math.pi)
        chars.append(chr(ascii_val))
    return ''.join(chars)


def print_states(states):
    """Print states in Dirac notation."""
    print("Quantum Register States:")
    print("=" * 72)
    for s in states:
        bi = s['beta_imag']
        sign = '+' if bi >= 0 else ''
        print(
            f"  |ψ_{s['index']:>2d}⟩ = "
            f"{s['alpha']:+.6f}|0⟩ + "
            f"({s['beta_real']:+.6f}{sign}{bi:.6f}i)|1⟩"
        )
    print()


def export_js_data(states):
    """Export state data formatted for JavaScript embedding."""
    thetas = [s['theta'] for s in states]
    phis = [s['phi'] for s in states]
    print("// Precomputed quantum state angles for JS embedding")
    print(f"const Q = {json.dumps(list(zip(thetas, phis)), indent=2)};")


if __name__ == '__main__':
    message = "ethan@esrpo.com"

    print(f"Message:  {message}")
    print(f"Length:   {len(message)} characters")
    print(f"Encoding: θ = ASCII · π / 128")
    print(f"Decoding: ASCII = round(θ · 128 / π)")
    print()

    states = encode(message)
    print_states(states)

    # Verify round-trip
    decoded = decode(states)
    print(f"Decoded:  {decoded}")
    print(f"Match:    {decoded == message}")
    print()

    # Export JS-ready data
    export_js_data(states)
