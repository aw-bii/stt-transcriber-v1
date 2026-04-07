# Results Page Design Spec

**Page:** Results View
**Purpose:** Display transcription output with actions
**Pattern:** iOS Detail View with toolbar

---

## Layout Structure

```
┌─────────────────────────────────────┐
│ ← Back    Transcription       Share │  Navigation Bar
├─────────────────────────────────────┤
│                                     │
│  ┌─────────────────────────────┐    │
│  │  AUDIO FILES               │    │  Grouped Card
│  ├─────────────────────────────┤    │
│  │                             │    │
│  │  📄 filename.mp3            │    │  File Info Row
│  │     2.4 MB • 1:32           │    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  ┌─────────────────────────────┐    │
│  │  TRANSCRIPTION              │    │  Section Label
│  ├─────────────────────────────┤    │
│  │                             │    │
│  │  ┌─────────────────────┐   │    │
│  │  │                     │   │    │
│  │  │  Transcription      │   │    │  Text Content
│  │  │  text appears here  │   │    │  (Editable)
│  │  │  ...                │   │    │
│  │  │                     │   │    │
│  │  └─────────────────────┘   │    │
│  │                             │    │
│  │  ✓ 98% accuracy estimated   │    │  Confidence Badge
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  ┌─────────────────────────────┐    │
│  │  [ Copy ]  [ Download ]    │    │  Action Buttons
│  │        [ New Upload ]       │    │
│  └─────────────────────────────┘    │
│                                     │
│         Made with ♥ in India         │  Footer
│                                     │
└─────────────────────────────────────┘
```

---

## Visual Specifications

### Navigation Bar
- Height: 44px
- Back button: Primary color, left
- Title: "Transcription", 17px Semibold, centered
- Share button: Primary color icon, right

### File Info Card
- Background: var(--color-surface)
- Corner radius: 12px
- Content: File icon (document) + filename + size + duration
- Font: 17px Body for filename, 13px Caption for metadata

### Transcription Section
- Background: var(--color-grouped-bg)
- Corner radius: 12px
- Section label: "TRANSCRIPTION" uppercase
- Padding: 16px

### Text Content Area
- Style: Inset grouped (iOS settings style)
- Background: var(--color-surface)
- Corner radius: 10px
- Padding: 16px
- Min height: 150px
- Max height: 400px (scrollable)
- Font: 17px Regular, 1.4 line-height
- Editable: Yes (contenteditable or textarea)

### Confidence Badge
- Position: Below text area, right aligned
- Icon: Checkmark circle (SF Symbol)
- Text: "98% accuracy estimated"
- Color: Success green
- Style: Inline badge, 13px

### Action Buttons
- Layout: Horizontal, space-between
- Primary action: Full width or split
- Style: Filled primary for main, tinted for secondary
- Corner radius: 12px
- Min height: 50px (44px touch + padding)
- Icons: Copy, Download, Plus (for new)

---

## Component States

### Copy Button States
| State | Appearance |
|-------|------------|
| Default | "Copy" with clipboard icon |
| Success | "Copied!" with checkmark, green, 2s |

### Download Button States
| State | Appearance |
|-------|------------|
| Default | "Save as TXT" with download icon |
| Downloading | "Saving..." with spinner |
| Complete | "Saved!" briefly, then reset |

### New Upload Button
| State | Appearance |
|-------|------------|
| Default | "New Transcription" with plus icon |
| Hover | Slight background tint |

---

## Accessibility

- Text area: `role="textbox"`, `aria-label="Transcription text"`
- Edit indicator: "Tap to edit" hint on first view
- Copy: `aria-label="Copy transcription to clipboard"`
- Download: `aria-label="Download as text file"`
- Confidence: `aria-label="Estimated 98 percent accuracy"`

---

## Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Move between action buttons |
| Enter | Activate focused button |
| Cmd+C | Copy text (when text focused) |
| Escape | Close results, return to upload |

---

## Animations

| Interaction | Animation |
|-------------|-----------|
| Results appear | Fade in + slide up 300ms |
| Copy success | Checkmark scales in 200ms |
| Button hover | Background opacity change 150ms |

---

## Responsive Behavior

| Breakpoint | Layout |
|------------|--------|
| 375px | Full width, stacked buttons |
| 768px+ | Max-width 600px, centered |
| 1024px+ | Larger text area, more padding |

---

## Edge Cases

| Case | Handling |
|------|----------|
| Empty transcription | Show placeholder: "No speech detected" |
| Very long text | Scrollable container, max 400px |
| Copy fails | Show error toast, fallback to select-all |
| Download fails | Show retry option |
