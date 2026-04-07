# Processing Page Design Spec

**Page:** Processing View
**Purpose:** Audio transcription in progress
**Pattern:** iOS Activity/Loading state

---

## Layout Structure

```
┌─────────────────────────────────────┐
│ ← Back    Processing...           │  Navigation Bar
├─────────────────────────────────────┤
│                                     │
│                                     │
│           ╭─────────────╮           │
│           │   Spinner   │           │  Activity Indicator
│           │   60×60     │           │
│           ╰─────────────╯           │
│                                     │
│         Processing Your             │  Title 2
│         Audio File                  │
│                                     │
│    ┌───────────────────────────┐    │
│    │ ████████████░░░░░░░░░░░░  │    │  Progress Bar
│    └───────────────────────────┘    │
│                                     │
│         67% complete                │  Caption
│                                     │
│         ● ● ● ○ ○                   │  Step Indicator
│         ↑                           │
│     Upload  Process  Done           │
│                                     │
│                                     │
│    ┌───────────────────────────┐    │
│    │      Cancel               │    │  Tertiary Button
│    └───────────────────────────┘    │
│                                     │
└─────────────────────────────────────┘
```

---

## Visual Specifications

### Activity Indicator (Spinner)
- Size: 60×60px
- Style: Apple activity indicator (circular)
- Color: Primary blue
- Animation: Continuous rotation, 1s per revolution

### Title Section
- Title: 22px Bold, centered
- Subtitle: 17px Regular, secondary-label, centered

### Progress Bar
- Height: 4px (thin, iOS style)
- Track: var(--color-separator)
- Fill: Linear gradient (primary to secondary)
- Corner radius: 2px
- Width: Animated 0% → 100%

### Step Indicator
- Layout: Horizontal, 3 steps
- Active: Filled circle, primary color
- Completed: Checkmark icon, success color
- Pending: Empty circle, separator color
- Labels: 13px, below each dot

### Cancel Button
- Style: Tertiary (plain text)
- Color: var(--color-error)
- Position: Centered below progress

---

## States

| Phase | Progress | Step Indicator | Message |
|-------|----------|----------------|---------|
| Upload | 0-30% | Upload (active) | "Uploading file..." |
| Processing | 30-90% | Process (active) | "Analyzing audio..." |
| Complete | 90-100% | Done (active) | "Finalizing..." |

---

## Timing

| Phase | Duration | Progress Rate |
|-------|----------|---------------|
| Upload | 1-5s | Fast (depends on file size) |
| Processing | Variable | Indeterminate until near end |
| Complete | 500ms | Quick fill to 100% |

---

## Accessibility

- Spinner: `role="status"`, `aria-label="Processing audio"`
- Progress: `aria-valuenow`, `aria-valuemin`, `aria-valuemax`
- Steps: `aria-current="step"` for active step
- Cancel: `aria-label="Cancel processing"`

---

## Animations

| Element | Animation |
|---------|-----------|
| Spinner | Rotate 360° over 1s, linear, infinite |
| Progress | Width 300ms ease-out |
| Step transition | Scale 1→1.2→1 with opacity |
| Cancel appear | Fade in 200ms |

---

## Error State

```
┌─────────────────────────────────────┐
│              ⚠️                     │  Error Icon
│                                     │
│         Transcription               │
│         Failed                      │
│                                     │
│    Could not process the audio.     │
│    Please try again.                │
│                                     │
│    ┌─────────┐  ┌─────────────┐     │
│    │ Retry   │  │    Cancel   │     │
│    └─────────┘  └─────────────┘     │
│                                     │
└─────────────────────────────────────┘
```
