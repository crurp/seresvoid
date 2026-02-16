#!/usr/bin/env python3
"""
Convert SVG logo to PNG at various sizes
Requires: cairosvg (install with: pip install cairosvg)
"""

import os
import sys

try:
    import cairosvg
except ImportError:
    print("Error: cairosvg not found. Installing...")
    print("Please run: pip install cairosvg")
    print("Or: pip install --user cairosvg")
    sys.exit(1)

# Logo sizes to generate
sizes = [16, 32, 40, 48, 64, 128, 256, 512]

# Input SVG file
svg_file = "icons/logo-master.svg"
output_dir = "icons/png"

# Create output directory
os.makedirs(output_dir, exist_ok=True)

print(f"Converting {svg_file} to PNG at various sizes...")
print(f"Output directory: {output_dir}\n")

for size in sizes:
    output_file = f"{output_dir}/logo-{size}.png"
    
    try:
        # Convert SVG to PNG at specified size
        cairosvg.svg2png(
            url=svg_file,
            write_to=output_file,
            output_width=size,
            output_height=size
        )
        print(f"✓ Created {output_file} ({size}x{size}px)")
    except Exception as e:
        print(f"✗ Failed to create {output_file}: {e}")

print(f"\nConversion complete! PNG files saved to {output_dir}/")
