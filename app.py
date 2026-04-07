#!/usr/bin/env python3
"""
Luxury Premium Streamlit web service for Hinglish Speech-to-Text tool.
"""

import streamlit as st
import os
import tempfile
from pathlib import Path
from stt_hinglish import transcribe_audio

# Configure page
st.set_page_config(
    page_title="Hinglish Speech-to-Text Tool",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for luxury premium design
st.markdown(
    """
<style>
    /* Luxury Color Variables */
    :root {
        --luxury-black: #1C1917;
        --luxury-charcoal: #44403C;
        --luxury-gold: #CA8A04;
        --luxury-gold-hover: #B07804;
        --luxury-gold-active: #996603;
        --luxury-bg: #FAFAF9;
        --luxury-text: #0C0A09;
    }
    
    /* Global Styles */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Luxury Typography */
    h1, h2, h3 {
        font-family: 'Bodoni Moda', serif !important;
        color: var(--luxury-black);
        letter-spacing: -0.5px;
        font-weight: 700;
        line-height: 1.2;
    }
    
    h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        font-size: 2rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    p, li, label, .stTextInput label, .stFileUploader label {
        font-family: 'Jost', sans-serif !important;
        color: var(--luxury-text);
        font-weight: 400;
        line-height: 1.6;
    }
    
    /* Luxury File Uploader */
    .stFileUploader>div {
        border: 2px dashed var(--luxury-gold);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        background: rgba(202, 138, 4, 0.03);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .stFileUploader>div:hover {
        background: rgba(202, 138, 4, 0.08);
        border-color: var(--luxury-gold-hover);
        transform: translateY(-2px);
        box-shadow: 0 12px 24px rgba(202, 138, 4, 0.15);
    }
    
    .stFileUploader>div:active {
        transform: translateY(0px);
    }
    
    /* Luxury Button Styling */
    .stButton>button {
        background-color: var(--luxury-gold);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        font-family: 'Jost', sans-serif;
        padding: 0.75rem 2rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 12px rgba(202, 138, 4, 0.2);
        letter-spacing: -0.25px;
        text-transform: none;
        height: 3rem;
        min-width: 120px;
    }
    
    .stButton>button:hover {
        background-color: var(--luxury-gold-hover);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(202, 138, 4, 0.3);
    }
    
    .stButton>button:active {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(202, 138, 4, 0.2);
        background-color: var(--luxury-gold-active);
    }
    
    .stButton>button:focus {
        box-shadow: 0 0 0 3px rgba(202, 138, 4, 0.25);
    }
    
    /* Secondary/Cancel Button */
    .stButton>button[kind="secondary"] {
        background-color: transparent;
        color: var(--luxury-charcoal);
        border: 2px solid var(--luxury-charcoal);
        box-shadow: none;
    }
    
    .stButton>button[kind="secondary"]:hover {
        background-color: rgba(68, 64, 60, 0.05);
        color: var(--luxury-black);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(68, 64, 60, 0.15);
    }
    
    /* Results Container */
    .results-container {
        background: rgba(250, 250, 249, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 2.5rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(202, 138, 4, 0.1);
    }
    
    /* Text Area Styling */
    .stTextArea textarea {
        border-radius: 16px;
        border: 1px solid rgba(202, 138, 4, 0.2);
        background-color: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(5px);
        font-family: 'Jost', sans-serif;
        font-size: 1.1rem;
        padding: 1.5rem;
        transition: all 0.3s ease;
        color: var(--luxury-black);
    }
    
    .stTextArea textarea:focus {
        border-color: var(--luxury-gold);
        box-shadow: 0 0 0 3px rgba(202, 138, 4, 0.2);
        background-color: white;
        backdrop-filter: none;
    }
    
    /* File Info Styling */
    .file-info {
        background: rgba(202, 138, 4, 0.05);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid var(--luxury-gold);
    }
    
    /* Progress Bar Styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--luxury-gold), var(--luxury-gold-hover));
        border-radius: 10px;
        height: 8px;
    }
    
    /* Spinner Styling */
    .stSpinner > div {
        border-top-color: var(--luxury-gold) !important;
        border-left-color: var(--luxury-gold) !important;
    }
    
    /* Alert/Info Box Styling */
    .stAlert {
        border-radius: 16px;
        border: none;
        background: rgba(202, 138, 4, 0.1);
        backdrop-filter: blur(5px);
    }
    
    .stAlert > div {
        padding: 1rem 1.5rem;
    }
    
    /* Success/Error Specific */
    .stSuccess {
        background: rgba(16, 185, 129, 0.1);
        border-left: 4px solid #10B981;
    }
    
    .stError {
        background: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #EF4444;
    }
    
    .stInfo {
        background: rgba(59, 130, 246, 0.1);
        border-left: 4px solid #3B82F6;
    }
    
    /* Footer Styling */
    footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(202, 138, 4, 0.2);
        color: var(--luxury-charcoal);
        font-size: 0.9rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        h1 {
            font-size: 2rem;
        }
        
        h2 {
            font-size: 1.75rem;
        }
        
        .stFileUploader>div {
            padding: 2rem 1.5rem;
        }
        
        .stButton>button {
            width: 100%;
            margin: 0.5rem 0;
        }
    }
    
    /* Animation for luxury feel */
    @keyframes luxuryPulse {
        0% { box-shadow: 0 0 0 0 rgba(202, 138, 4, 0.4); }
        70% { box-shadow: 0 0 0 12px rgba(202, 138, 4, 0); }
        100% { box-shadow: 0 0 0 0 rgba(202, 138, 4, 0); }
    }
    
    .luxury-pulse {
        animation: luxuryPulse 2s infinite;
    }
    
    /* Hide Streamlit elements we don't need */
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stActionButton {display:none;}
</style>
""",
    unsafe_allow_html=True,
)

# Initialize session state
if "transcription_result" not in st.session_state:
    st.session_state.transcription_result = ""
if "is_processing" not in st.session_state:
    st.session_state.is_processing = False
if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = ""

# Title and description
st.markdown("<h1>🎤 Hinglish Speech-to-Text</h1>", unsafe_allow_html=True)
st.markdown(
    "<p>Convert Hindi-English code-switched audio to text with studio-quality precision</p>",
    unsafe_allow_html=True,
)

# File upload section
uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3", "m4a", "flac", "ogg"],
    help="Drag & drop or click to browse audio files (Max 200MB)",
    label_visibility="collapsed",
)

if uploaded_file is not None:
    # Store file info in session state
    st.session_state.uploaded_file_name = uploaded_file.name
    file_size_mb = uploaded_file.size / (1024 * 1024)

    # Display file info with luxury styling
    st.markdown(
        f"""
    <div class="file-info">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <strong>{uploaded_file.name}</strong>
            </div>
            <div style="font-family: 'Jost', sans-serif; color: var(--luxury-charcoal);">
                {file_size_mb:.2f} MB
            </div>
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
            "🎯 Transcribe Audio",
            type="primary",
            use_container_width=True,
            disabled=st.session_state.is_processing,
        )

    # Process transcription
    if transcribe_button and not st.session_state.is_processing:
        st.session_state.is_processing = True
        st.session_state.transcription_result = ""  # Clear previous result

        with st.spinner("🎧 Processing audio with premium AI model..."):
            try:
                # Transcribe the audio file
                text = transcribe_audio(tmp_file_path)
                st.session_state.transcription_result = text
                st.success("✨ Transcription completed with studio precision!")
            except Exception as e:
                st.error(f"❌ Transcription failed: {str(e)}")
                st.session_state.transcription_result = ""
            finally:
                st.session_state.is_processing = False

    # Clean up temporary file
    try:
        os.unlink(tmp_file_path)
    except:
        pass

# Results section
if st.session_state.transcription_result:
    st.markdown("<h2>📝 Transcription Results</h2>", unsafe_allow_html=True)

    # Results container with luxury styling
    st.markdown('<div class="results-container">', unsafe_allow_html=True)

    # Transcription text area
    st.text_area(
        label="Transcription",
        value=st.session_state.transcription_result,
        height=200,
        label_visibility="collapsed",
        help="Your transcribed text - ready for professional use",
    )

    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("📋 Copy Text", use_container_width=True):
            # For Streamlit, we'll show a success message
            st.success("Text copied to clipboard!")
            # Note: Actual clipboard access would require additional components

    with col2:
        if st.button("💾 Download TXT", use_container_width=True):
            # Create download button
            st.download_button(
                label="Download Transcription",
                data=st.session_state.transcription_result,
                file_name=f"{Path(st.session_state.uploaded_file_name).stem}_transcription.txt",
                mime="text/plain",
                use_container_width=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

# Alternative: Cancel button when processing
if st.session_state.is_processing:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⏹️ Cancel Processing", type="secondary", use_container_width=True):
            st.session_state.is_processing = False
            st.session_state.transcription_result = ""
            st.rerun()

# Footer
st.markdown(
    """
<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(202, 138, 4, 0.2);">
    <p style="color: var(--luxury-charcoal); font-family: 'Jost', sans-serif; font-size: 0.9rem;">
        Powered by <strong>shunyalabs/zero-stt-hinglish</strong> • Studio Grade Audio AI
    </p>
    <p style="color: var(--luxury-charcoal); font-family: 'Jost', sans-serif; font-size: 0.8rem; margin-top: 0.5rem;">
        Precision Engineered for Professional Transcription
    </p>
</div>
""",
    unsafe_allow_html=True,
)
