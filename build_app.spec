# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec for Hinglish STT
Run: pyinstaller build_app.spec
"""

from PyInstaller.utils.hooks import collect_all

# Collect all needed files from these packages
hiddenimports = [
    'transformers',
    'torch',
    'accelerate',
    'streamlit',
    'streamlit.web',
    'scipy',
    'stt_hinglish',
    'numpy',
    'safetensors',
    'tokenizers',
    'huggingface_hub',
    'torch.serialization',
    'transformers.pipelines',
    'transformers.models.whisper',
]

excludes = [
    'tensorflow',
    'keras',
    'matplotlib',
    'pandas',
    'plotly',
    'altair',
    'vega',
    'pydeck',
    'torchvision',
    'torchaudio',
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HinglishSTT',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico' if False else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='HinglishSTT',
)
