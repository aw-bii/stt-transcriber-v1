# Hinglish STT Tool with Drag-and-Drop Web Interface - Design Specification

## Project Overview
This document outlines the design for enhancing the existing Hinglish speech-to-text tool with a drag-and-drop web interface while maintaining the existing command-line functionality.

## Architecture
The system will consist of two main components:
1. **Core Transcription Module**: Existing Python package that handles audio transcription using the shunyalabs/zero-stt-hinglish model
2. **Web Service Layer**: Flask-based REST API that exposes the transcription functionality via HTTP endpoints
3. **Frontend Interface**: HTML/CSS/JavaScript drag-and-drop interface that communicates with the web service

## Components

### Core Transcription Module (Unchanged)
- **Location**: `stt_hinglish.py`
- **Function**: `transcribe_audio(audio_file, output_file=None)`
- **Dependencies**: torch, transformers, accelerate
- **Responsibility**: Load model and transcribe audio files to text
- **Interface**: Function-based API that can be imported and used by other modules

### Web Service Layer
- **Location**: `app.py` (new)
- **Framework**: Flask
- **Endpoints**:
  - `POST /transcribe`: Accepts audio file upload, returns JSON transcription
  - `GET /health`: Health check endpoint
  - `GET /`: Serves the frontend interface
- **Responsibility**: 
  - Handle file uploads securely
  - Validate audio file types
  - Call core transcription module
  - Return results in JSON format
  - Handle errors appropriately

### Frontend Interface
- **Location**: `static/index.html`, `static/style.css`, `static/script.js`
- **Features**:
  - Drag-and-drop area for audio files
  - File type validation (accepts common audio formats)
  - Progress indicator during transcription
  - Display transcription results
  - Option to download transcription as text file
  - Responsive design for mobile/desktop

## Data Flow
1. User drags audio file onto web interface or clicks to select file
2. Frontend validates file type and size
3. Frontend sends file to `/transcribe` endpoint via AJAX/FormData
4. Web service receives file, saves temporarily, calls transcription module
5. Transcription module processes audio and returns text
6. Web service returns JSON response with transcription text
7. Frontend displays result and provides download option

## Error Handling
- **File Validation**: Check file extension and MIME type
- **Size Limits**: Configure maximum file size (e.g., 100MB)
- **Transcription Errors**: Catch exceptions from transcription module and return appropriate HTTP error codes
- **Network Errors**: Frontend handles failed requests gracefully
- **Cleanup**: Temporary files are removed after processing

## Configuration
- Maximum file upload size: Configurable via environment variable
- Supported audio formats: .wav, .mp3, .m4a, .flac, .ogg
- Server host/port: Configurable via command line arguments or environment variables

## Testing Approach
- Unit tests for core transcription module (unchanged)
- Integration tests for web service endpoints
- Manual testing of frontend interface
- Test with various audio file formats and sizes

## Dependencies
- Existing: torch, transformers, accelerate
- New: flask, werkzeug (for file handling)
- Frontend: Plain HTML/CSS/JS (no additional dependencies required)

## Security Considerations
- Sanitize filenames to prevent path traversal
- Limit file size to prevent DoS attacks
- Validate file content type, not just extension
- Clean up temporary files promptly
- Consider rate limiting for production deployment

## Deployment
- Can be run locally with `python app.py`
- Supports environment variables for configuration
- Compatible with WSGI servers for production (gunicorn, uWSGI)