# Design System Master File

> **LOGIC:** When building a specific page, first check `design-system/pages/[page-name].md`.
> If that file exists, its rules **override** this Master file.
> If not, strictly follow the rules below.

---

**Project:** HinglishSTT
**Generated:** 2026-04-07
**Design Philosophy:** Apple Human Interface Guidelines (HIG) + Native iOS/macOS aesthetics
**Category:** Utility / Productivity Tool

---

## Design Philosophy

**Apple HIG Core Principles:**
1. **Clarity** — Content is paramount, UI fades into background
2. **Deference** — UI helps users understand and interact with content, never competes
3. **Depth** — Visual layers and motion convey hierarchy and enable navigation

---

## Color Palette (Apple System Colors)

| Role | Light Mode | Dark Mode | CSS Variable |
|------|------------|-----------|--------------|
| Primary | `#007AFF` | `#0A84FF` | `--color-primary` |
| Secondary | `#5856D6` | `#5E5CE6` | `--color-secondary` |
| Accent | `#CA8A04` | `#DDA15E` | `--color-accent` |
| Background | `#F5F5F7` | `#000000` | `--color-bg` |
| Surface | `#FFFFFF` | `#1C1C1E` | `--color-surface` |
| GroupedBg | `#F2F2F7` | `#000000` | `--color-grouped-bg` |
| Label | `#000000` | `#FFFFFF` | `--color-label` |
| SecondaryLabel | `#3C3C43` (60%) | `#EBEBF5` (60%) | `--color-secondary-label` |
| TertiaryLabel | `#3C3C43` (30%) | `#EBEBF5` (30%) | `--color-tertiary-label` |
| Separator | `#3C3C43` (29%) | `#545458` (65%) | `--color-separator` |
| Success | `#34C759` | `#30D158` | `--color-success` |
| Warning | `#FF9500` | `#FF9F0A` | `--color-warning` |
| Error | `#FF3B30` | `#FF453A` | `--color-error` |

**Color Notes:**
- Use system colors that automatically adapt to light/dark mode
- Reserve color for actionable or status information only
- Gold accent preserved from original brand identity

---

## Typography (SF Pro / System Font)

| Style | Weight | Size | Leading | Tracking |
|-------|--------|------|---------|----------|
| Large Title | Bold (700) | 34px | 41px | 0.37 |
| Title 1 | Bold (700) | 28px | 34px | 0.36 |
| Title 2 | Bold (700) | 22px | 28px | 0.35 |
| Title 3 | Semibold (600) | 20px | 25px | 0.38 |
| Headline | Semibold (600) | 17px | 22px | -0.41 |
| Body | Regular (400) | 17px | 22px | -0.41 |
| Callout | Regular (400) | 16px | 21px | -0.32 |
| Subhead | Regular (400) | 15px | 20px | -0.24 |
| Footnote | Regular (400) | 13px | 18px | -0.08 |
| Caption 1 | Regular (400) | 12px | 16px | 0 |
| Caption 2 | Regular (400) | 11px | 13px | 0.07 |

**Font Stack (Web):**
```css
font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
```

**Apple Typography Rules:**
- Use `font-weight: -0.41` (ultrabold tracking) for large titles
- Body text: 17px with 22px line-height (optimal reading)
- Never use font sizes below 11px
- Uppercase text only for labels and categories, never for body content

---

## Spacing System (Apple 8pt Grid)

| Token | Value | Apple Usage |
|-------|-------|-------------|
| `--space-1` | 4px | Icon-to-label gaps |
| `--space-2` | 8px | Tight component spacing |
| `--space-3` | 12px | Standard padding |
| `--space-4` | 16px | Section padding |
| `--space-5` | 20px | Grouped content padding |
| `--space-6` | 24px | Large gaps |
| `--space-8` | 32px | Section margins |
| `--space-10` | 40px | Hero spacing |
| `--space-12` | 48px | Major sections |
| `--space-16` | 64px | Page margins |

**HIG Spacing Rules:**
- Content padding: 16px minimum on iPhone, 20px on iPad
- Safe area insets: 44px minimum from screen edges
- Touch targets: 44×44pt minimum (equal to 44×44px at 1x scale)

---

## Component Specifications

### Buttons (Apple Style)

```css
/* Primary Button - Filled */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 12px 24px;
  background: var(--color-primary);
  color: white;
  border: none;
  border-radius: 12px;
  font-family: inherit;
  font-size: 17px;
  font-weight: 600;
  letter-spacing: -0.41px;
  cursor: pointer;
  transition: all 200ms ease;
}

.btn-primary:hover {
  opacity: 0.85;
}

.btn-primary:active {
  opacity: 0.65;
  transform: scale(0.98);
}

/* Secondary Button - Tinted */
.btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 12px 24px;
  background: var(--color-primary);
  color: white;
  border: none;
  border-radius: 12px;
  font-family: inherit;
  font-size: 17px;
  font-weight: 600;
  letter-spacing: -0.41px;
  cursor: pointer;
  opacity: 0.15;
  transition: all 200ms ease;
}

.btn-secondary:hover {
  opacity: 0.25;
}

/* Tertiary Button - Plain */
.btn-tertiary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 12px 24px;
  background: transparent;
  color: var(--color-primary);
  border: none;
  border-radius: 12px;
  font-family: inherit;
  font-size: 17px;
  font-weight: 600;
  letter-spacing: -0.41px;
  cursor: pointer;
  transition: all 200ms ease;
}

.btn-tertiary:hover {
  background: var(--color-primary);
  color: white;
  opacity: 0.1;
}
```

### Cards / Containers

```css
/* Standard Card - Rounded white surface */
.card {
  background: var(--color-surface);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

/* Grouped Inset Card - iOS Settings style */
.card-grouped {
  background: var(--color-grouped-bg);
  border-radius: 12px;
  overflow: hidden;
}

/* Floating Control - HIG Control Panel */
.control-panel {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.12);
}

@media (prefers-color-scheme: dark) {
  .control-panel {
    background: rgba(28, 28, 30, 0.72);
    border: 1px solid rgba(255, 255, 255, 0.1);
  }
}
```

### Text Fields / Inputs

```css
/* Standard Text Input */
.input {
  width: 100%;
  min-height: 44px;
  padding: 12px 16px;
  background: var(--color-surface);
  border: 1px solid var(--color-separator);
  border-radius: 12px;
  font-family: inherit;
  font-size: 17px;
  color: var(--color-label);
  transition: border-color 200ms ease;
}

.input:focus {
  border-color: var(--color-primary);
  outline: none;
}

.input::placeholder {
  color: var(--color-tertiary-label);
}

/* Text Area */
.textarea {
  width: 100%;
  min-height: 120px;
  padding: 16px;
  background: var(--color-surface);
  border: 1px solid var(--color-separator);
  border-radius: 12px;
  font-family: inherit;
  font-size: 17px;
  line-height: 22px;
  color: var(--color-label);
  resize: vertical;
  transition: border-color 200ms ease;
}
```

### Icons (SF Symbols Style)

```css
/* Icon Container - 44x44 touch target */
.icon-container {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  transition: background 200ms ease;
}

.icon-container:hover {
  background: rgba(0, 122, 255, 0.1);
}

/* SVG Icons - Use stroke, not fill */
.icon {
  width: 24px;
  height: 24px;
  stroke-width: 1.5;
  stroke: currentColor;
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}
```

### Progress Indicators

```css
/* Progress Bar - Thin iOS style */
.progress-bar {
  width: 100%;
  height: 4px;
  background: var(--color-separator);
  border-radius: 2px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--color-primary);
  border-radius: 2px;
  transition: width 300ms ease;
}

/* Spinner - Apple Activity Indicator */
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid var(--color-separator);
  border-top-color: var(--color-primary);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### Labels & Badges

```css
/* Section Label - Uppercase Apple style */
.label {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: -0.08px;
  color: var(--color-secondary-label);
  text-transform: uppercase;
}

/* Status Badge */
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 10px;
  font-size: 13px;
  font-weight: 600;
  border-radius: 6px;
}

.badge-success {
  background: rgba(52, 199, 89, 0.15);
  color: var(--color-success);
}

.badge-error {
  background: rgba(255, 59, 48, 0.15);
  color: var(--color-error);
}
```

---

## Shadows (Apple Depth)

| Level | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 3px rgba(0,0,0,0.08)` | Subtle lift, cards |
| `--shadow-md` | `0 4px 12px rgba(0,0,0,0.1)` | Floating elements |
| `--shadow-lg` | `0 12px 40px rgba(0,0,0,0.15)` | Modals, sheets |

**HIG Depth Rules:**
- Never use pure black for shadows
- Use opacity 0.08-0.15 for subtle shadows
- Layer elements by shadow depth, not borders

---

## Border Radius (Apple Standard)

| Element | Radius |
|---------|--------|
| Buttons | 12px |
| Cards | 16px |
| Modal/Sheet | 20px |
| Small elements | 8px |
| Pills/Chips | 22px (full height) |

---

## Animation & Motion (Apple Timing)

| Type | Duration | Easing |
|------|----------|--------|
| Micro (hover) | 150ms | ease-out |
| Standard | 200ms | ease-in-out |
| Complex | 300ms | ease-in-out |
| Spring | 400ms | cubic-bezier(0.25, 0.1, 0.25, 1) |

**HIG Motion Rules:**
- Prefer system-standard animations
- Respect `prefers-reduced-motion`
- Use motion to convey relationship between screens
- Never animate purely for decoration

---

## Anti-Patterns (Do NOT Use)

### Absolutely Forbidden
- ❌ **Emojis as icons** — Use SF Symbols or SVG icons only
- ❌ **Pure black text on pure white** — Use system colors for proper contrast
- ❌ **Hard shadows** — Always use subtle, diffuse shadows
- ❌ **Flat design without depth** — iOS uses depth through blur/shadows
- ❌ **Instant transitions** — All changes must animate (150ms minimum)
- ❌ **Below 11px text** — Apple minimum is Caption 2 (11px)

### Layout Warnings
- ❌ **Centered everything** — Content should follow natural reading patterns
- ❌ **Uniform spacing everywhere** — Vary spacing to create hierarchy
- ❌ **More than 3 font sizes in one view** — Stick to type scale

---

## Pre-Delivery Checklist

Before delivering any UI code, verify:

### Visual Quality
- [ ] No emojis used as icons (use SF Symbols / SVG instead)
- [ ] All icons use consistent 24x24 viewBox with 1.5px stroke
- [ ] `cursor-pointer` on all interactive elements
- [ ] Touch targets minimum 44×44px
- [ ] Consistent border-radius (12px buttons, 16px cards)

### Color & Contrast
- [ ] Light mode: text contrast ≥ 4.5:1
- [ ] Dark mode: text contrast ≥ 4.5:1
- [ ] System colors used (auto-adapt to light/dark)
- [ ] Color not sole indicator of state

### Motion
- [ ] Transitions 150-300ms
- [ ] `prefers-reduced-motion` respected
- [ ] No layout-shifting animations

### Accessibility
- [ ] Focus states visible (2px primary color outline)
- [ ] aria-labels on icon-only buttons
- [ ] Keyboard navigation works
- [ ] Screen reader labels present

### Responsive
- [ ] Safe area insets respected (44px from edges)
- [ ] No content behind fixed elements
- [ ] Works at 375px, 768px, 1024px, 1440px
