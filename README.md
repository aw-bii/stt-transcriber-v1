# Hinglish Speech-to-Text Tool

A standalone Windows app for Hindi-English speech-to-text transcription using the [shunyalabs/zero-stt-hinglish](https://huggingface.co/shunyalabs/zero-stt-hinglish) model.

## Features

- **Offline Ready** - Works after first run (model cached locally)
- **Apple Design** - Beautiful iOS-style interface
- **Hinglish Support** - Optimized for Hindi-English code-switching
- **Drag & Drop** - Easy audio file upload
- **Privacy First** - All processing happens on your computer

## Quick Start

### Option 1: Run as Python App
```bash
pip install -r requirements.txt
python main.py
```

### Option 2: Run Standalone Executable
```bash
dist\HinglishSTT.exe
```

Open your browser to http://localhost:8501

## Building the Executable

```batch
build.bat
```

Or manually:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name HinglishSTT main.py
```

## System Requirements

- **OS:** Windows 10 or later
- **RAM:** 8GB minimum (16GB recommended)
- **Storage:** 5GB free space
- **Internet:** Required for first run only (model download)

## First Run

The AI model (~3GB) downloads automatically on first use and is cached locally. Subsequent runs work offline.

Model cached at: `%USERPROFILE%\.cache\huggingface\hub\`

## Project Structure

```
├── app.py              # Streamlit app (Apple HIG design)
├── stt_hinglish.py     # Transcription module
├── main.py             # Launcher script
├── build.bat           # Build script
├── build.spec          # PyInstaller spec
├── requirements.txt    # Python dependencies
└── design-system/      # UI design specs
```

## Supported Formats

- WAV, MP3, M4A, FLAC, OGG
- Max file size: 200MB

## Model Info

- **Model:** shunyalabs/zero-stt-hinglish
- **Base:** OpenAI Whisper Medium
- **Languages:** Hinglish (Hindi-English code-switching)
- **Size:** ~3GB cached

## Troubleshooting

### Out of Memory
Close other apps, ensure 8GB+ RAM available.

### Model download fails
Check internet connection and try again.

### Port 8501 in use
Change port in main.py or kill the conflicting process.

## License

MIT - Model licensed under OpenRAIL
