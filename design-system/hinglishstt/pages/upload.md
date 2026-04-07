# Upload Page Design Spec

**Page:** Upload View
**Purpose:** File selection and upload initiation
**Pattern:** iOS Settings-style grouped interface

---

## Layout Structure

```
┌─────────────────────────────────────┐
│ ← Back    Upload Audio      Settings │  Navigation Bar
├─────────────────────────────────────┤
│                                     │
│         ╭─────────────────╮         │
│         │   App Icon      │         │  Hero Icon
│         │   80×80         │         │
│         ╰─────────────────╯         │
│                                     │
│      Hinglish Speech-to-Text        │  Large Title
│                                     │
│   Convert Hindi-English audio       │  Body
│   to accurate text transcriptions   │
│                                     │
├─────────────────────────────────────┤
│  ┌─────────────────────────────┐    │
│  │  AUDIO FILES               │    │  Section Label
│  ├─────────────────────────────┤    │
│  │                             │    │
│  │    ┌───────────────────┐    │    │
│  │    │  Upload Zone     │    │    │  Control Panel
│  │    │  (Drop area)     │    │    │  (Liquid Glass)
│  │    └───────────────────┘    │    │
│  │                             │    │
│  │    Supported: WAV, MP3,    │    │  Caption
│  │    M4A, FLAC, OGG          │    │
│  │                             │    │
│  └─────────────────────────────┘    │
│                                     │
│  ┌─────────────────────────────┐    │
│  │  Drop your audio file here  │    │  Placeholder State
│  │  or tap to browse          │    │
│  └─────────────────────────────┘    │
│                                     │
└─────────────────────────────────────┘
```

---

## Visual Specifications

### Navigation Bar
- Height: 44px
- Background: blur (transparent)
- Title: 17px Semibold, centered
- Back button: Primary color, left aligned
- Settings: Icon only, right aligned

### App Icon
- Size: 80×80px
- Corner radius: 18px (Apple icon standard)
- Shadow: `--shadow-md`
- Content: Waveform/mic icon in primary color

### Title Section
- Title: 34px Bold (Large Title), centered
- Body: 17px Regular, centered, secondary-label color

### Upload Zone (Control Panel)
- Style: Liquid Glass (floating above content)
- Background: `rgba(255,255,255,0.72)` + blur
- Border: 1px solid `rgba(255,255,255,0.5)`
- Corner radius: 20px
- Padding: 32px
- Min height: 200px
- Dashed border: 2px dashed var(--color-primary) when empty

### States

| State | Appearance |
|-------|------------|
| Empty | Dashed border, cloud upload icon, instruction text |
| Drag Over | Solid primary border, highlighted background, scale 1.02 |
| File Selected | Solid border, file info displayed, transcribe button appears |
| Uploading | Progress bar visible, percentage shown |
| Error | Red border, error message, retry option |

---

## Component States

### Upload Zone Empty
```
Icon: Arrow up from circle (SF Symbol: arrow.up.doc)
Text: "Drop your audio file here"
Subtext: "or tap to browse"
Caption: "Supported: WAV, MP3, M4A, FLAC, OGG • Max 200MB"
```

### Upload Zone Drag Over
```
Border: 2px solid var(--color-primary)
Background: rgba(0,122,255,0.05)
Icon: Animated bounce
Text: "Release to upload"
```

### File Info Card (appears after selection)
```
Layout: Horizontal, space-between
Left: File icon + filename
Right: File size + remove button
Background: var(--color-surface)
Corner radius: 12px
Padding: 16px
```

---

## Spacing (8pt Grid)

| Element | Spacing |
|---------|---------|
| Nav to content | 0px (edge-to-edge) |
| Icon to title | 24px |
| Title to body | 8px |
| Title section to upload zone | 40px |
| Upload zone internal padding | 32px |
| Section gap | 24px |

---

## Interactions

| Interaction | Behavior |
|-------------|----------|
| Tap upload zone | Opens file picker |
| Drag file over | Highlight zone, show release state |
| Drop file | Validate, show file info |
| Invalid file | Shake animation, show error |
| Remove file | Fade out, return to empty state |

---

## Accessibility

- Upload zone: `role="button"`, `aria-label="Upload audio file"`
- File input: `aria-label="Select audio file"`
- Drag/drop: Announced via aria-live
- Error states: `role="alert"` for screen readers
