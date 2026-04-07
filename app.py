#!/usr/bin/env python3
"""
Flask web service for Hinglish Speech-to-Text tool with drag-and-drop interface.
"""

import os
import tempfile
import logging
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from stt_hinglish import transcribe_audio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, static_folder="static")

# Configuration
UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {"wav", "mp3", "m4a", "flac", "ogg"}
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    """Serve the main HTML interface."""
    return send_from_directory(app.static_folder, "index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    """Handle audio file transcription requests."""
    # Check if file was uploaded
    if "audio_file" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    file = request.files["audio_file"]

    # Check if file is empty
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Validate file type
    if not allowed_file(file.filename):
        return jsonify(
            {
                "error": "File type not allowed. Supported formats: WAV, MP3, M4A, FLAC, OGG"
            }
        ), 400

    # Save file temporarily
    temp_path = None
    try:
        filename = secure_filename(file.filename)
        temp_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(temp_path)

        logger.info(f"Saved uploaded file to {temp_path}")

        # Transcribe the audio file
        logger.info("Starting transcription...")
        text = transcribe_audio(temp_path)
        logger.info("Transcription completed")

        # Return transcription result
        return jsonify({"text": text, "filename": filename})

    except Exception as e:
        logger.error(f"Error during transcription: {str(e)}")
        return jsonify({"error": f"Transcription failed: {str(e)}"}), 500
    finally:
        # Clean up temporary file if it exists
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
                logger.info(f"Removed temporary file {temp_path}")
            except OSError as e:
                logger.warning(f"Could not remove temporary file {temp_path}: {e}")


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "hinglish-stt"})


if __name__ == "__main__":
    # Get configuration from environment variables
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "False").lower() == "true"

    logger.info(f"Starting Hinglish STT service on {host}:{port}")
    app.run(host=host, port=port, debug=debug)
