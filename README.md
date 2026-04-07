# Hinglish Speech-to-Text Tool

A simple tool to convert audio files to text using the [shunyalabs/zero-stt-hinglish](https://huggingface.co/shunyalabs/zero-stt-hinglish) model from Hugging Face. This model is specifically designed for Hinglish (Hindi-English code-switching) speech recognition.

## Features

- Transcribes Hinglish audio (Hindi-English code-switching)
- Supports common audio formats (mp3, wav, etc.)
- Outputs transcription to console or saves to file
- Easy to use command-line interface
- **NEW**: Drag-and-drop web interface for easy file transcription

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface
Basic usage:
```bash
python stt_hinglish.py path/to/audio/file.mp3
```

Save output to a file:
```bash
python stt_hinglish.py path/to/audio/file.mp3 -o transcription.txt
```

Specify a different model (optional):
```bash
python stt_hinglish.py path/to/audio/file.mp3 --model shunyalabs/zero-stt-hinglish
```

### Web Interface
Start the web service:
```bash
python app.py
```

Then open your browser to `http://localhost:5000` to access the drag-and-drop interface.

## Requirements

- Python 3.7+
- torch
- transformers
- accelerate
- flask
- werkzeug

See `requirements.txt` for details.

## How It Works

This tool uses the Hugging Face Transformers library to load the `shunyalabs/zero-stt-hinglish` model, which is a post-trained version of OpenAI's Whisper Medium model specifically fine-tuned for Hinglish speech recognition.

The model excels at handling code-switched speech where speakers naturally alternate between Hindi and English mid-sentence.

## Model Information

- **Model ID**: `shunyalabs/zero-stt-hinglish`
- **Base Model**: OpenAI Whisper Medium
- **Language**: Hinglish (Hindi-English code-switching)
- **License**: OpenRAIL
- **Size**: 0.8B parameters

For more information about the model, visit: https://huggingface.co/shunyalabs/zero-stt-hinglish

## Example

```bash
python stt_hinglish.py sample.wav
```

Output:
```
Loading the shunyalabs/zero-stt-hinglish model...
Transcribing sample.wav...

Transcription:
--------------------------------------------------
अरे यार आज meeting में बड़ा fun था हम लोग नए project पर discuss कर रहे थे
--------------------------------------------------
```

## Notes

- The first run will download the model (~1.5GB), which may take some time depending on your internet connection
- Subsequent runs will use the cached model
- GPU acceleration is automatically used if available
- For best results, use clear audio with minimal background noise
- Maximum file size for web interface: 100MB

## Troubleshooting

If you encounter issues:

1. Make sure you have a stable internet connection for the initial model download
2. Check that your audio file is in a supported format
3. Ensure you have sufficient disk space for the model (~2GB)
4. If you get CUDA errors and don't have a GPU, the model will fall back to CPU (slower but functional)
5. For web interface issues, check that Flask is installed correctly

## License

This tool is provided as-is. The underlying model is licensed under OpenRAIL - see the model card for details.