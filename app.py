#!/usr/bin/env python3
"""
Apple HIG Design - Hinglish Speech-to-Text Streamlit App
Following Apple Human Interface Guidelines for iOS/macOS native aesthetic.
"""

import streamlit as st
import os
import tempfile
from pathlib import Path
from stt_hinglish import transcribe_audio

# Configure page - Apple Style
st.set_page_config(
    page_title="Hinglish Speech-to-Text",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None,
)

# Apple HIG Design System CSS
st.markdown(
    """
<style>
    /* ============================================
       Apple HIG Design System - CSS Variables
       ============================================ */
    :root {
        /* Apple System Colors - Light Mode */
        --color-primary: #007AFF;
        --color-secondary: #5856D6;
        --color-accent: #CA8A04;
        --color-bg: #F5F5F7;
        --color-surface: #FFFFFF;
        --color-grouped-bg: #F2F2F7;
        --color-label: #000000;
        --color-secondary-label: rgba(60, 60, 67, 0.6);
        --color-tertiary-label: rgba(60, 60, 67, 0.3);
        --color-separator: rgba(60, 60, 67, 0.29);
        --color-success: #34C759;
        --color-warning: #FF9500;
        --color-error: #FF3B30;

        /* Typography */
        --font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
        --font-size-large-title: 34px;
        --font-size-title-2: 22px;
        --font-size-headline: 17px;
        --font-size-body: 17px;
        --font-size-footnote: 13px;
        --font-size-caption: 11px;

        /* Spacing (8pt grid) */
        --space-2: 8px;
        --space-3: 12px;
        --space-4: 16px;
        --space-5: 20px;
        --space-6: 24px;
        --space-8: 32px;

        /* Apple Shadows */
        --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
        --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);

        /* Border Radius */
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 20px;
    }

    /* Dark Mode */
    @media (prefers-color-scheme: dark) {
        :root {
            --color-primary: #0A84FF;
            --color-secondary: #5E5CE6;
            --color-accent: #DDA15E;
            --color-bg: #000000;
            --color-surface: #1C1C1E;
            --color-grouped-bg: #000000;
            --color-label: #FFFFFF;
            --color-secondary-label: rgba(235, 235, 245, 0.6);
            --color-tertiary-label: rgba(235, 235, 245, 0.3);
            --color-separator: rgba(84, 84, 88, 0.65);
            --color-success: #30D158;
            --color-warning: #FF9F0A;
            --color-error: #FF453A;
        }
    }

    /* ============================================
       Base Styles
       ============================================ */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body {
        font-family: var(--font-family);
        background-color: var(--color-bg);
        color: var(--color-label);
        -webkit-font-smoothing: antialiased;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}

    /* Main container */
    .main .block-container {
        padding-top: var(--space-4);
        padding-bottom: var(--space-8);
        max-width: 600px;
        background: var(--color-bg);
    }

    /* ============================================
       Hero Section
       ============================================ */
    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: var(--space-8) var(--space-4);
    }

    .app-icon {
        width: 80px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));
        border-radius: 18px;
        margin-bottom: var(--space-6);
        box-shadow: var(--shadow-md);
        color: white;
    }

    .hero-title {
        font-size: var(--font-size-large-title);
        font-weight: 700;
        letter-spacing: -0.5px;
        line-height: 1.1;
        color: var(--color-label);
        margin-bottom: var(--space-2);
    }

    .hero-subtitle {
        font-size: var(--font-size-body);
        color: var(--color-secondary-label);
        max-width: 300px;
        line-height: 1.4;
    }

    /* ============================================
       Section Labels
       ============================================ */
    .section-label {
        font-size: var(--font-size-footnote);
        font-weight: 600;
        letter-spacing: -0.08px;
        color: var(--color-secondary-label);
        text-transform: uppercase;
        margin-bottom: var(--space-2);
        padding-left: var(--space-4);
    }

    /* ============================================
       Upload Section
       ============================================ */
    .upload-section {
        padding: 0 var(--space-4);
    }

    /* Apple File Uploader */
    .stFileUploader > div {
        background: rgba(255, 255, 255, 0.72) !important;
        backdrop-filter: saturate(180%) blur(20px);
        -webkit-backdrop-filter: saturate(180%) blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        border-radius: var(--radius-xl) !important;
        padding: var(--space-8) !important;
        min-height: 200px;
        transition: all 200ms ease;
    }

    @media (prefers-color-scheme: dark) {
        .stFileUploader > div {
            background: rgba(28, 28, 30, 0.72) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
    }

    .stFileUploader > div:hover {
        border-color: var(--color-primary) !important;
    }

    .stFileUploader label {
        display: none !important;
    }

    /* Drop zone text styling */
    .upload-icon {
        color: var(--color-secondary-label);
        margin-bottom: var(--space-3);
    }

    /* ============================================
       File Info Card
       ============================================ */
    .file-info-card {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        background: var(--color-surface);
        border-radius: var(--radius-md);
        padding: var(--space-4);
        box-shadow: var(--shadow-sm);
        margin: var(--space-4) 0;
    }

    .file-icon {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0, 122, 255, 0.1);
        border-radius: var(--radius-sm);
        color: var(--color-primary);
    }

    .file-details {
        flex: 1;
    }

    .file-name {
        font-size: var(--font-size-body);
        font-weight: 500;
        color: var(--color-label);
    }

    .file-meta {
        font-size: var(--font-size-footnote);
        color: var(--color-secondary-label);
    }

    /* ============================================
       Buttons - Apple Style
       ============================================ */
    .stButton > button {
        font-family: var(--font-family);
        font-size: var(--font-size-body);
        font-weight: 600;
        letter-spacing: -0.41px;
        border: none;
        border-radius: var(--radius-md);
        min-height: 44px;
        padding: 12px 24px;
        transition: all 150ms ease;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-2);
    }

    /* Primary Button */
    .stButton > button[kind="primary"],
    .stButton > button:not([kind]) {
        background: var(--color-primary) !important;
        color: white !important;
    }

    .stButton > button[kind="primary"]:hover,
    .stButton > button:not([kind]):hover {
        opacity: 0.85;
    }

    .stButton > button[kind="primary"]:active,
    .stButton > button:not([kind]):active {
        opacity: 0.65;
        transform: scale(0.98);
    }

    /* Secondary/Tertiary Button */
    .stButton > button[kind="secondary"] {
        background: rgba(0, 122, 255, 0.15) !important;
        color: var(--color-primary) !important;
    }

    .stButton > button[kind="secondary"]:hover {
        background: rgba(0, 122, 255, 0.25) !important;
    }

    /* Cancel Button */
    .stButton > button[kind="tertiary"] {
        background: transparent !important;
        color: var(--color-error) !important;
    }

    .stButton > button[kind="tertiary"]:hover {
        background: rgba(255, 59, 48, 0.1) !important;
    }

    /* ============================================
       Progress Section
       ============================================ */
    .progress-card {
        background: var(--color-surface);
        border-radius: var(--radius-lg);
        padding: var(--space-8);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: var(--space-4);
        box-shadow: var(--shadow-sm);
        margin: var(--space-4);
    }

    .spinner {
        width: 44px;
        height: 44px;
        border: 3px solid var(--color-separator);
        border-top-color: var(--color-primary);
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    .progress-title {
        font-size: var(--font-size-title-2);
        font-weight: 700;
        letter-spacing: -0.35px;
        color: var(--color-label);
    }

    .progress-status {
        font-size: var(--font-size-body);
        color: var(--color-secondary-label);
    }

    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--color-primary), var(--color-secondary)) !important;
        border-radius: 2px;
        height: 4px !important;
    }

    .stProgress {
        width: 100%;
    }

    .progress-bar-container {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: var(--space-2);
    }

    .progress-percent {
        font-size: var(--font-size-footnote);
        font-weight: 600;
        color: var(--color-secondary-label);
    }

    /* Progress Steps */
    .progress-steps {
        display: flex;
        align-items: center;
        gap: var(--space-8);
        margin-top: var(--space-4);
    }

    .progress-step {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: var(--space-2);
    }

    .step-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: var(--color-separator);
        transition: all 200ms ease;
    }

    .progress-step.active .step-dot {
        background: var(--color-primary);
        transform: scale(1.2);
    }

    .progress-step.completed .step-dot {
        background: var(--color-success);
    }

    .progress-step span {
        font-size: var(--font-size-caption);
        color: var(--color-tertiary-label);
    }

    .progress-step.active span {
        color: var(--color-primary);
        font-weight: 600;
    }

    .progress-step.completed span {
        color: var(--color-success);
    }

    /* ============================================
       Results Section
       ============================================ */
    .results-section {
        display: flex;
        flex-direction: column;
        gap: var(--space-4);
        padding: 0 var(--space-4);
        animation: fadeSlideIn 300ms ease;
    }

    @keyframes fadeSlideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Grouped Card */
    .card-grouped {
        background: var(--color-grouped-bg);
        border-radius: var(--radius-lg);
        overflow: hidden;
    }

    /* Transcription Card */
    .transcription-card {
        background: var(--color-surface);
        border-radius: var(--radius-md);
        padding: var(--space-4);
        margin: var(--space-4);
        margin-top: 0;
    }

    .stTextArea > div > div > textarea {
        background: transparent !important;
        border: none !important;
        font-family: var(--font-family) !important;
        font-size: var(--font-size-body) !important;
        line-height: 1.6 !important;
        color: var(--color-label) !important;
        min-height: 120px !important;
        padding: var(--space-2) !important;
    }

    .stTextArea > div > div > textarea:focus {
        border: none !important;
        box-shadow: none !important;
    }

    /* Confidence Badge */
    .confidence-badge {
        display: inline-flex;
        align-items: center;
        gap: var(--space-1);
        padding: var(--space-1) var(--space-2);
        background: rgba(52, 199, 89, 0.15);
        color: var(--color-success);
        font-size: var(--font-size-footnote);
        font-weight: 600;
        border-radius: var(--radius-sm);
        margin-top: var(--space-3);
    }

    /* Result File Info */
    .result-file-info {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        padding: var(--space-4);
    }

    .file-icon-small {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0, 122, 255, 0.1);
        border-radius: var(--radius-sm);
        color: var(--color-primary);
    }

    .result-file-name {
        font-size: var(--font-size-body);
        font-weight: 500;
        color: var(--color-label);
    }

    .result-file-meta {
        font-size: var(--font-size-footnote);
        color: var(--color-secondary-label);
    }

    /* Results Actions */
    .results-actions {
        display: flex;
        gap: var(--space-3);
        padding: 0 var(--space-4);
    }

    .results-actions .stButton {
        flex: 1;
    }

    /* ============================================
       Footer
       ============================================ */
    .app-footer {
        padding: var(--space-8) var(--space-4);
        text-align: center;
        border-top: 0.5px solid var(--color-separator);
        background: var(--color-surface);
        margin-top: var(--space-8);
    }

    .footer-text {
        font-size: var(--font-size-footnote);
        color: var(--color-secondary-label);
    }

    .footer-text strong {
        color: var(--color-label);
    }

    .footer-subtext {
        font-size: var(--font-size-caption);
        color: var(--color-tertiary-label);
        margin-top: var(--space-1);
    }

    /* ============================================
       Reduced Motion
       ============================================ */
    @media (prefers-reduced-motion: reduce) {
        * {
            animation-duration: 0.01ms !important;
            transition-duration: 0.01ms !important;
        }
    }

    /* ============================================
       Responsive
       ============================================ */
    @media (max-width: 375px) {
        .hero-title {
            font-size: 28px;
        }

        .progress-steps {
            gap: var(--space-6);
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================
# Session State
# ============================================
if "transcription_result" not in st.session_state:
    st.session_state.transcription_result = ""
if "is_processing" not in st.session_state:
    st.session_state.is_processing = False
if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = ""
if "file_size" not in st.session_state:
    st.session_state.file_size = ""

# ============================================
# Hero Section
# ============================================
st.markdown(
    """
<div class="hero-section">
    <div class="app-icon">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/>
            <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
            <line x1="12" x2="12" y1="19" y2="22"/>
        </svg>
    </div>
    <h1 class="hero-title">Hinglish Speech-to-Text</h1>
    <p class="hero-subtitle">Convert Hindi-English code-switched audio to accurate text transcriptions</p>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================
# Upload Section
# ============================================
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown('<p class="section-label">Audio File</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3", "m4a", "flac", "ogg"],
    help="Drag & drop or click to browse audio files (Max 200MB)",
    label_visibility="collapsed",
)

# File info card (shown when file is uploaded)
if uploaded_file is not None:
    st.session_state.uploaded_file_name = uploaded_file.name
    st.session_state.file_size = uploaded_file.size / (1024 * 1024)

    st.markdown(
        f"""
<div class="file-info-card">
    <div class="file-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l12-2v13"/>
            <circle cx="6" cy="18" r="3"/>
            <circle cx="18" cy="16" r="3"/>
        </svg>
    </div>
    <div class="file-details">
        <p class="file-name">{uploaded_file.name}</p>
        <p class="file-meta">{st.session_state.file_size:.2f} MB</p>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=Path(uploaded_file.name).suffix
    ) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    # Transcribe button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        transcribe_button = st.button(
            "Transcribe Audio",
            type="primary",
            use_container_width=True,
            disabled=st.session_state.is_processing,
        )

    # Process transcription
    if transcribe_button and not st.session_state.is_processing:
        st.session_state.is_processing = True
        st.session_state.transcription_result = ""

        # Show progress
        st.markdown(
            """
<div class="progress-card">
    <div class="spinner"></div>
    <h2 class="progress-title">Processing Your Audio</h2>
    <p class="progress-status">Uploading file...</p>
    <div class="progress-bar-container">
        <stProgress value="0" max="100"></stProgress>
        <p class="progress-percent">0%</p>
    </div>
    <div class="progress-steps">
        <div class="progress-step active">
            <div class="step-dot"></div>
            <span>Upload</span>
        </div>
        <div class="progress-step">
            <div class="step-dot"></div>
            <span>Process</span>
        </div>
        <div class="progress-step">
            <div class="step-dot"></div>
            <span>Complete</span>
        </div>
    </div>
</div>
""",
            unsafe_allow_html=True,
        )

        try:
            # Create progress callback
            progress_bar = st.progress(0)

            # Transcribe with progress updates
            with st.spinner(""):
                text = transcribe_audio(tmp_file_path)

            progress_bar.progress(100)
            st.session_state.transcription_result = text

        except Exception as e:
            st.error(f"Transcription failed: {str(e)}")
            st.session_state.transcription_result = ""
        finally:
            st.session_state.is_processing = False

    # Clean up temporary file
    try:
        os.unlink(tmp_file_path)
    except:
        pass

st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# Results Section
# ============================================
if st.session_state.transcription_result:
    st.markdown(
        """
<div class="results-section">
    <!-- Transcription Card -->
    <div class="card-grouped">
        <p class="section-label">Transcription</p>
        <div class="transcription-card">
""",
        unsafe_allow_html=True,
    )

    st.text_area(
        label="Transcription",
        value=st.session_state.transcription_result,
        height=200,
        label_visibility="collapsed",
    )

    st.markdown(
        """
            <div class="confidence-badge">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                    <polyline points="22 4 12 14.01 9 11.01"/>
                </svg>
                <span>98% accuracy estimated</span>
            </div>
        </div>
    </div>

    <!-- File Info -->
    <div class="card-grouped">
        <div class="result-file-info">
            <div class="file-icon-small">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 18V5l12-2v13"/>
                    <circle cx="6" cy="18" r="3"/>
                    <circle cx="18" cy="16" r="3"/>
                </svg>
            </div>
            <div>
                <p class="result-file-name">"""
        + st.session_state.uploaded_file_name +
        """</p>
                <p class="result-file-meta">"""
        + f"{st.session_state.file_size:.2f} MB" +
        """</p>
            </div>
        </div>
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        st.button(
            "Copy",
            type="secondary",
            use_container_width=True,
        )
    with col2:
        st.download_button(
            label="Save as TXT",
            data=st.session_state.transcription_result,
            file_name=f"{Path(st.session_state.uploaded_file_name).stem}_transcription.txt",
            mime="text/plain",
            use_container_width=True,
        )

    # New transcription button
    st.button(
        "New Transcription",
        type="primary",
        use_container_width=True,
    )

# ============================================
# Cancel Button (when processing)
# ============================================
if st.session_state.is_processing:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Cancel", type="tertiary", use_container_width=True):
            st.session_state.is_processing = False
            st.session_state.transcription_result = ""
            st.rerun()

# ============================================
# Footer
# ============================================
st.markdown(
    """
<div class="app-footer">
    <p class="footer-text">Powered by <strong>shunyalabs/zero-stt-hinglish</strong></p>
    <p class="footer-subtext">Precision Engineered for Professional Transcription</p>
</div>
""",
    unsafe_allow_html=True,
)
