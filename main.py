#!/usr/bin/env python3
"""
Hinglish STT - Offline Desktop App Launcher
Runs the Streamlit app locally without internet after first run.
"""

import subprocess
import sys
import os
from pathlib import Path


def get_resource_path(relative_path: str) -> Path:
    """Get the path to a resource, works for dev and PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).parent / relative_path


def main():
    """Launch the Streamlit app."""
    app_dir = Path(__file__).parent
    app_path = app_dir / "app.py"

    if not app_path.exists():
        print(f"ERROR: {app_path} not found!")
        print("Press Enter to exit...")
        try:
            input()
        except (EOFError, OSError):
            pass
        sys.exit(1)

    # Check for model cache
    hf_cache = os.environ.get(
        "HF_HOME",
        os.path.join(os.path.expanduser("~"), ".cache", "huggingface")
    )
    model_path = Path(hf_cache) / "hub" / "models--shunyalabs--zero-stt-hinglish"

    if not model_path.exists():
        print("=" * 60)
        print("  FIRST RUN SETUP")
        print("=" * 60)
        print()
        print("  The AI model (~3GB) will download automatically.")
        print("  This requires an internet connection.")
        print()
        print("  Estimated download time:")
        print("    - Fast broadband: 5-10 minutes")
        print("    - Mobile hotspot: 20-30 minutes")
        print()
        print("  Model will be cached for offline use after this.")
        print("=" * 60)
        print()

    # Streamlit configuration
    streamlit_args = [
        sys.executable, "-m", "streamlit", "run",
        str(app_path),
        "--browser.gatherUsageStats", "false",
        "--server.headless", "true",
        "--server.port", "8501",
        "--server.address", "localhost",
    ]

    print("=" * 60)
    print("  HINGLISH SPEECH-TO-TEXT")
    print("=" * 60)
    print()
    print("  Starting app...")
    print("  Please wait...")
    print()
    print("  Open your browser and go to:")
    print("  -> http://localhost:8501")
    print()
    print("  Press Ctrl+C to stop the app.")
    print("=" * 60)
    print()

    try:
        subprocess.run(streamlit_args, check=True)
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        print("Thank you for using Hinglish STT!")
    except Exception as e:
        print(f"\n\nERROR: {e}")
        print("Press Enter to exit...")
        try:
            input()
        except (EOFError, OSError):
            pass


if __name__ == "__main__":
    main()
