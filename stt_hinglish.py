#!/usr/bin/env python3
"""
Hinglish Speech-to-Text using shunyalabs/zero-stt-hinglish model.
Optimized for Streamlit web deployment with caching and proper audio handling.
"""

import os
import numpy as np
import streamlit as st
from transformers import pipeline
import torch

# Cache the model to avoid reloading on every request
# WARNING: pipeline internally uses torch.load() which uses pickle for deserialization.
# This creates a potential integrity risk if the model weights are tampered with.
# The model is fetched from HuggingFace Hub - ensure the remote source is trusted.
# Consider implementing model signature verification for production use.
@st.cache_resource
def load_model():
    """Load and cache the transcription model."""
    try:
        return pipeline(
            "automatic-speech-recognition",
            model="shunyalabs/zero-stt-hinglish",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        )
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        return None

def transcribe_audio(audio_path):
    """
    Transcribe audio file to text using cached model.

    Args:
        audio_path (str): Path to the audio file

    Returns:
        str: Transcribed text
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    model = load_model()
    if model is None:
        raise RuntimeError("Model not available. Please refresh and try again.")

    try:
        result = model(audio_path)
        return result["text"]
    except Exception as e:
        error_msg = str(e)
        if "ffmpeg" in error_msg.lower():
            raise RuntimeError(
                "Audio processing requires ffmpeg. Please ensure ffmpeg is installed on the server."
            )
        raise RuntimeError(f"Transcription failed: {error_msg}")

def transcribe_audio_bytes(audio_bytes, sample_rate=16000):
    """
    Transcribe audio from bytes using the model.

    Args:
        audio_bytes (bytes): Raw audio bytes
        sample_rate (int): Sample rate of the audio

    Returns:
        str: Transcribed text

    Security: audio_bytes must be validated before use. sample_rate must be
    a positive integer within supported range to prevent arbitrary file writes.
    """
    import tempfile
    import scipy.io.wavfile as wavfile

    # Input validation to prevent arbitrary file write risks
    if not isinstance(audio_bytes, (bytes, bytearray, np.ndarray)):
        raise ValueError("audio_bytes must be bytes, bytearray, or numpy array")
    if not isinstance(sample_rate, int) or not (8000 <= sample_rate <= 48000):
        raise ValueError("sample_rate must be an integer between 8000 and 48000 Hz")
    if hasattr(audio_bytes, 'size') and audio_bytes.size == 0:
        raise ValueError("audio_bytes cannot be empty")

    model = load_model()
    if model is None:
        raise RuntimeError("Model not available. Please refresh and try again.")

    # Create temp file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Write bytes to wav file
        wavfile.write(tmp_path, sample_rate, audio_bytes)

        # Transcribe
        result = model(tmp_path)
        return result["text"]
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
