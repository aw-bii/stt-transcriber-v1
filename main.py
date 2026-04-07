#!/usr/bin/env python3
"""
Hinglish STT Offline App Launcher
Runs the Streamlit app in offline mode with bundled dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Launch the Streamlit app."""
    # Get the directory of this script
    app_dir = Path(__file__).parent

    # Path to the Streamlit app
    app_path = app_dir / "app.py"

    if not app_path.exists():
        print(f"Error: {app_path} not found!")
        sys.exit(1)

    # Check for HuggingFace model cache
    hf_cache = os.environ.get("HF_HOME", os.path.join(os.path.expanduser("~"), ".cache", "huggingface"))
    model_path = Path(hf_cache) / "hub" / "models--shunyalabs--zero-stt-hinglish"

    if not model_path.exists():
        print("=" * 60)
        print("IMPORTANT: First run will download the AI model (~3GB)")
        print("Please ensure you have a stable internet connection.")
        print("Subsequent runs will work offline.")
        print("=" * 60)
        print()

    # Launch Streamlit
    print("Starting Hinglish Speech-to-Text...")
    print("Open your browser to http://localhost:8501")
    print()
    print("Press Ctrl+C to stop.")
    print()

    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run",
            str(app_path),
            "--browser.gatherUsageStats", "false",
            "--server.headless", "true",
            "--server.port", "8501",
        ])
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
