#!/usr/bin/env python3
"""
Simple tool to convert audio files to text using the shunyalabs/zero-stt-hinglish model.
Supports Hinglish (Hindi-English code-switching) speech recognition.
"""

import argparse
import os
import sys
from transformers import pipeline

def transcribe_audio(audio_file, output_file=None):
    """
    Transcribe audio file to text using the zero-stt-hinglish model.
    
    Args:
        audio_file (str): Path to the audio file
        output_file (str, optional): Path to save the transcription. If None, prints to console.
    
    Returns:
        str: Transcribed text
    """
    # Check if audio file exists
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Audio file not found: {audio_file}")
    
    # Load the model pipeline
    print("Loading the shunyalabs/zero-stt-hinglish model...")
    transcriber = pipeline("automatic-speech-recognition", model="shunyalabs/zero-stt-hinglish")
    
    # Transcribe the audio
    print(f"Transcribing {audio_file}...")
    result = transcriber(audio_file)
    text = result["text"]
    
    # Output the result
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Transcription saved to {output_file}")
    else:
        print("\nTranscription:")
        print("-" * 50)
        print(text)
        print("-" * 50)
    
    return text

def main():
    parser = argparse.ArgumentParser(description="Convert audio files to text using shunyalabs/zero-stt-hinglish model")
    parser.add_argument("audio_file", help="Path to the audio file to transcribe")
    parser.add_argument("-o", "--output", help="Path to save the transcription (optional)")
    parser.add_argument("--model", default="shunyalabs/zero-stt-hinglish", 
                       help="Hugging Face model ID (default: shunyalabs/zero-stt-hinglish)")
    
    args = parser.parse_args()
    
    try:
        transcribe_audio(args.audio_file, args.output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
