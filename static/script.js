/* ============================================
   HinglishSTT - Apple HIG JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
    // -----------------------------------------
    // DOM Elements
    // -----------------------------------------
    const uploadZone = document.getElementById('uploadZone');
    const uploadContent = document.getElementById('uploadContent');
    const emptyState = document.getElementById('emptyState');
    const fileSelectedState = document.getElementById('fileSelectedState');
    const dragOverState = document.getElementById('dragOverState');
    const fileInput = document.getElementById('fileInput');
    const fileNameEl = document.getElementById('fileName');
    const fileMetaEl = document.getElementById('fileMeta');
    const removeFileBtn = document.getElementById('removeFileBtn');
    const actionSection = document.getElementById('actionSection');
    const transcribeBtn = document.getElementById('transcribeBtn');
    const progressSection = document.getElementById('progressSection');
    const progressStatus = document.getElementById('progressStatus');
    const progressFill = document.getElementById('progressFill');
    const progressPercent = document.getElementById('progressPercent');
    const cancelBtn = document.getElementById('cancelBtn');
    const resultsSection = document.getElementById('resultsSection');
    const transcriptionContent = document.getElementById('transcriptionContent');
    const confidenceBadge = document.getElementById('confidenceBadge');
    const resultFileName = document.getElementById('resultFileName');
    const resultFileMeta = document.getElementById('resultFileMeta');
    const copyBtn = document.getElementById('copyBtn');
    const copyBtnText = document.getElementById('copyBtnText');
    const downloadBtn = document.getElementById('downloadBtn');
    const newTranscriptionBtn = document.getElementById('newTranscriptionBtn');
    const stepUpload = document.getElementById('stepUpload');
    const stepProcess = document.getElementById('stepProcess');
    const stepComplete = document.getElementById('stepComplete');

    // -----------------------------------------
    // State
    // -----------------------------------------
    let selectedFile = null;
    let isProcessing = false;

    // -----------------------------------------
    // Utility Functions
    // -----------------------------------------
    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    function showState(elementToShow) {
        // Hide all states
        emptyState.hidden = true;
        fileSelectedState.hidden = true;
        dragOverState.hidden = true;

        // Show requested state
        if (elementToShow) {
            elementToShow.hidden = false;
        }
    }

    function updateProgress(percent, status) {
        progressFill.style.width = percent + '%';
        progressPercent.textContent = Math.round(percent) + '%';
        if (status) {
            progressStatus.textContent = status;
        }
    }

    function setStep(step) {
        // Reset all steps
        stepUpload.classList.remove('active', 'completed');
        stepProcess.classList.remove('active', 'completed');
        stepComplete.classList.remove('active', 'completed');

        // Activate up to current step
        if (step >= 1) stepUpload.classList.add('completed');
        if (step >= 2) stepProcess.classList.add('active');
        if (step >= 3) stepComplete.classList.add('active');
        if (step === 4) {
            stepUpload.classList.add('completed');
            stepProcess.classList.add('completed');
            stepComplete.classList.add('completed');
        }
    }

    function showScreen(screen) {
        actionSection.hidden = true;
        progressSection.hidden = true;
        resultsSection.hidden = true;

        if (screen === 'action') {
            actionSection.hidden = false;
        } else if (screen === 'progress') {
            progressSection.hidden = false;
        } else if (screen === 'results') {
            resultsSection.hidden = false;
        }
    }

    // -----------------------------------------
    // File Handling
    // -----------------------------------------
    function handleFile(file) {
        // Validate file type
        const allowedTypes = ['audio/wav', 'audio/mpeg', 'audio/mp3', 'audio/x-m4a', 'audio/m4a', 'audio/flac', 'audio/ogg'];
        const allowedExtensions = ['.wav', '.mp3', '.m4a', '.flac', '.ogg'];
        const extension = '.' + file.name.split('.').pop().toLowerCase();

        if (!allowedTypes.includes(file.type) && !allowedExtensions.includes(extension)) {
            alert('Please select a valid audio file (WAV, MP3, M4A, FLAC, OGG)');
            return;
        }

        // Validate file size (200MB limit)
        const maxSize = 200 * 1024 * 1024;
        if (file.size > maxSize) {
            alert('File size exceeds 200MB limit');
            return;
        }

        selectedFile = file;

        // Update file info display
        fileNameEl.textContent = file.name;
        fileMetaEl.textContent = formatFileSize(file.size);

        // Update result file info
        resultFileName.textContent = file.name;
        resultFileMeta.textContent = formatFileSize(file.size);

        // Show file selected state
        showState(fileSelectedState);
        actionSection.hidden = false;
        transcribeBtn.disabled = false;
    }

    function clearFile() {
        selectedFile = null;
        fileInput.value = '';
        showState(emptyState);
        actionSection.hidden = true;
        transcribeBtn.disabled = true;
    }

    // Upload zone click
    uploadZone.addEventListener('click', () => {
        if (!isProcessing) {
            fileInput.click();
        }
    });

    // Upload zone keyboard
    uploadZone.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            if (!isProcessing) {
                fileInput.click();
            }
        }
    });

    // File input change
    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    // Remove file button
    removeFileBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        clearFile();
    });

    // -----------------------------------------
    // Drag and Drop
    // -----------------------------------------
    uploadZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        if (!isProcessing) {
            uploadZone.classList.add('drag-over');
            showState(dragOverState);
        }
    });

    uploadZone.addEventListener('dragleave', (e) => {
        e.preventDefault();
        uploadZone.classList.remove('drag-over');
        if (selectedFile) {
            showState(fileSelectedState);
        } else {
            showState(emptyState);
        }
    });

    uploadZone.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadZone.classList.remove('drag-over');

        if (!isProcessing) {
            const dt = e.dataTransfer;
            if (dt.files && dt.files.length > 0) {
                handleFile(dt.files[0]);
            }
        }
    });

    // -----------------------------------------
    // Transcribe Button
    // -----------------------------------------
    transcribeBtn.addEventListener('click', async () => {
        if (!selectedFile || isProcessing) return;

        isProcessing = true;
        transcribeBtn.disabled = true;
        uploadZone.style.pointerEvents = 'none';

        // Show progress screen
        showScreen('progress');
        updateProgress(0, 'Uploading file...');
        setStep(1);

        try {
            // Simulate upload progress
            await simulateProgress(0, 30, 1000, 'Uploading file...');
            setStep(2);

            // Simulate processing progress
            updateProgress(30, 'Analyzing audio...');
            await simulateProgress(30, 80, 2000, 'Processing audio...');

            // Simulate completion
            updateProgress(90, 'Finalizing...');
            await simulateProgress(90, 100, 500, 'Complete!');
            setStep(4);

            // Show demo transcription
            transcriptionContent.textContent = getDemoTranscription();

            // Show results
            setTimeout(() => {
                showScreen('results');
                isProcessing = false;
                uploadZone.style.pointerEvents = 'auto';
            }, 500);

        } catch (error) {
            console.error('Error:', error);
            progressStatus.textContent = 'Error: ' + error.message;
            isProcessing = false;
            uploadZone.style.pointerEvents = 'auto';
            showScreen('action');
            transcribeBtn.disabled = false;
        }
    });

    // -----------------------------------------
    // Progress Simulation (Demo)
    // -----------------------------------------
    function simulateProgress(start, end, duration, status) {
        return new Promise((resolve) => {
            const startTime = performance.now();
            updateProgress(start, status);

            function animate(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(start + (end - start) * (elapsed / duration), end);

                updateProgress(progress, status);

                if (elapsed < duration) {
                    requestAnimationFrame(animate);
                } else {
                    updateProgress(end, status);
                    resolve();
                }
            }

            requestAnimationFrame(animate);
        });
    }

    // -----------------------------------------
    // Demo Transcription
    // -----------------------------------------
    function getDemoTranscription() {
        return `Hello everyone, welcome to today's meeting.

So basically, what I was thinking is that we should really focus on improving the user experience, you know? The interface is good but there are some pain points that users have been reporting.

Main points to consider:
1. The upload process takes too long for large files
2. Some users are having trouble with the audio format support
3. We need to add more language options in the future

Kya aap log sochte ho ki ye sahi hai? I think we should prioritize the upload speed issue first, what do you all think?

Let me know your thoughts on this. Thank you.`;
    }

    // -----------------------------------------
    // Cancel Button
    // -----------------------------------------
    cancelBtn.addEventListener('click', () => {
        isProcessing = false;
        transcribeBtn.disabled = false;
        uploadZone.style.pointerEvents = 'auto';
        showScreen('action');
        updateProgress(0, 'Cancelled');
    });

    // -----------------------------------------
    // Copy Button
    // -----------------------------------------
    copyBtn.addEventListener('click', () => {
        const text = transcriptionContent.textContent;

        navigator.clipboard.writeText(text).then(() => {
            // Success state
            const originalText = copyBtnText.textContent;
            copyBtnText.textContent = 'Copied!';
            copyBtn.style.background = 'rgba(52, 199, 89, 0.15)';
            copyBtn.style.color = 'var(--color-success)';

            setTimeout(() => {
                copyBtnText.textContent = originalText;
                copyBtn.style.background = '';
                copyBtn.style.color = '';
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy:', err);
            // Fallback: select text
            const range = document.createRange();
            range.selectNodeContents(transcriptionContent);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
        });
    });

    // -----------------------------------------
    // Download Button
    // -----------------------------------------
    downloadBtn.addEventListener('click', () => {
        const text = transcriptionContent.textContent;
        const blob = new Blob([text], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${selectedFile ? selectedFile.name.replace(/\.[^/.]+$/, '') : 'transcription'}_transcript.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });

    // -----------------------------------------
    // New Transcription Button
    // -----------------------------------------
    newTranscriptionBtn.addEventListener('click', () => {
        // Reset everything
        clearFile();
        showScreen('action');
        transcriptionContent.textContent = '';
        updateProgress(0, '');
        setStep(1);
    });

    // -----------------------------------------
    // Initialize
    // -----------------------------------------
    showState(emptyState);
    showScreen('action');
});
