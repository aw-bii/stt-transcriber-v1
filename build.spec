# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Hinglish STT Offline App
Build with: pyinstaller build.spec
"""

import os
import sys

block_cipher = None

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(SPEC))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

a = Analysis(
    ['main.spec'],  # Entry point
    pathex=[BASE_DIR],
    binaries=[],
    datas=[
        # Include model cache directory if it exists
        # Add HuggingFace cache to be bundled
    ],
    hiddenimports=[
        'transformers',
        'torch',
        'accelerate',
        'streamlit',
        'scipy',
        'numpy',
        'stt_hinglish',
        'torch.serialization',
        'transformers.pipelines',
        'transformers.models',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tensorflow',
        'keras',
        'matplotlib',
        'pandas',
        'plotly',
        'altair',
        'vega',
        'pydeck',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HinglishSTT',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Set to False for windowed app
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(ASSETS_DIR, 'icon.ico') if os.path.exists(os.path.join(ASSETS_DIR, 'icon.ico')) else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='HinglishSTT',
)

# Create onefile bundle (uncomment for single exe)
# merge = MERGE([a])
# exe = EXE(
#     pyz,
#     a.scripts,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     strip=False,
#     upx=True,
#     console=False,
#     name='HinglishSTT',
# )
