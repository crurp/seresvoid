# EchoSpark Design System - Quick Reference

Quick lookup guide for common design decisions.

## Colors

### Primary
```css
--primary: #6366f1;        /* Indigo 500 */
--secondary: #8b5cf6;      /* Violet 500 */
--accent: #ec4899;         /* Pink 500 */
```

### Backgrounds
```css
--bg-primary: #0a0a0f;     /* Deep dark */
--bg-secondary: #111118;   /* Secondary dark */
--bg-tertiary: #1a1a24;    /* Tertiary dark */
```

### Text
```css
--text-primary: #ffffff;   /* White */
--text-secondary: #a1a1aa; /* Zinc 400 */
--text-tertiary: #71717a;  /* Zinc 500 */
```

## Typography

### Fonts
- **Body:** Inter (400, 500, 600)
- **Headings:** Space Grotesk (600, 700, 800)

### Sizes
- **Hero:** `clamp(3rem, 8vw, 6rem)`
- **Section Title:** `clamp(2.5rem, 5vw, 4rem)`
- **Card Title:** `1.5rem`
- **Body:** `clamp(1rem, 2vw, 1.25rem)`

## Spacing

```css
--space-4: 1rem;    /* 16px - Standard */
--space-6: 1.5rem;  /* 24px - Medium */
--space-8: 2rem;    /* 32px - Large */
--space-12: 3rem;   /* 48px - XL */
```

## Components

### Button Primary
```css
background: linear-gradient(135deg, #6366f1, #8b5cf6);
padding: 1rem 2rem;
border-radius: 12px;
```

### Card
```css
background: var(--bg-secondary);
border: 1px solid var(--border);
border-radius: 24px;
padding: 2rem;
```

### Container
```css
max-width: 1400px;
margin: 0 auto;
padding: 0 2rem;
```

## Breakpoints

- **Mobile:** < 768px
- **Tablet:** 768px - 1024px
- **Desktop:** > 1024px

## Logo Sizes

- **Favicon:** 16px, 32px
- **Header:** 40px
- **Cards:** 48px
- **Large:** 128px, 256px, 512px

## Animations

- **Duration:** 0.3s - 0.6s
- **Easing:** `cubic-bezier(0.4, 0, 0.2, 1)`
- **Hover:** `translateY(-5px)`

---

For complete details, see [DESIGN_SYSTEM.md](./DESIGN_SYSTEM.md)
