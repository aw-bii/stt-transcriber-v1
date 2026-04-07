document.addEventListener('DOMContentLoaded', function() {
    const uploadArea = document.getElementById('uploadArea');
    const browseBtn = document.getElementById('browseBtn');
    const fileInput = document.getElementById('fileInput');
    const fileInfo = document.getElementById('fileInfo');
    const fileName = document.getElementById('fileName');
    const fileSize = document.getElementById('fileSize');
    const controls = document.getElementById('controls');
    const transcribeBtn = document.getElementById('transcribeBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    const progressContainer = document.getElementById('progressContainer');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const resultsContainer = document.getElementById('resultsContainer');
    const transcriptionText = document.getElementById('transcriptionText');
    const copyBtn = document.getElementById('copyBtn');
    const downloadBtn = document.getElementById('downloadBtn');

    let selectedFile = null;

    // Handle drag and drop
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        
        const dt = e.dataTransfer;
        if (dt.files && dt.files.length > 0) {
            handleFile(dt.files[0]);
        }
    });

    // Handle browse button click
    browseBtn.addEventListener('click', () => {
        fileInput.click();
    });

    // Handle file input change
    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    // Handle file selection
    function handleFile(file) {
        // Validate file type
        const allowedTypes = ['audio/wav', 'audio/mpeg', 'audio/mp4', 'audio/x-m4a', 'audio/flac', 'audio/ogg'];
        if (!allowedTypes.includes(file.type)) {
            alert('Please select a valid audio file (WAV, MP3, M4A, FLAC, OGG)');
            return;
        }

        // Validate file size (100MB limit)
        const maxSize = 100 * 1024 * 1024; // 100MB
        if (file.size > maxSize) {
            alert('File size exceeds 100MB limit');
            return;
        }

        selectedFile = file;
        fileName.textContent = file.name;
        fileSize.textContent = formatFileSize(file.size);
        fileInfo.style.display = 'block';
        controls.style.display = 'flex';
        transcribeBtn.disabled = false;
    }

    // Format file size for display
    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    // Handle transcribe button click
    transcribeBtn.addEventListener('click', async () => {
        if (!selectedFile) return;

        // Disable UI during processing
        transcribeBtn.disabled = true;
        browseBtn.disabled = true;
        fileInput.disabled = true;
        uploadArea.style.pointerEvents = 'none';
        
        // Show progress
        progressContainer.style.display = 'block';
        progressText.textContent = 'Uploading file...';
        progressFill.style.width = '0%';

        try {
            const formData = new FormData();
            formData.append('audio_file', selectedFile);

            const response = await fetch('/transcribe', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }

            const result = await response.json();
            
            // Update progress
            progressText.textContent = 'Processing complete!';
            progressFill.style.width = '100%';

            // Show results
            transcriptionText.textContent = result.text || 'No transcription available';
            resultsContainer.style.display = 'block';

            // Hide progress after a brief delay
            setTimeout(() => {
                progressContainer.style.display = 'none';
            }, 1000);

        } catch (error) {
            console.error('Error:', error);
            progressText.textContent = 'Error: ' + error.message;
            progressFill.style.backgroundColor = '#e74c3c';
            
            setTimeout(() => {
                progressContainer.style.display = 'none';
                progressFill.style.backgroundColor = '#3498db';
            }, 3000);
        } finally {
            // Re-enable UI
            transcribeBtn.disabled = false;
            browseBtn.disabled = false;
            fileInput.disabled = false;
            uploadArea.style.pointerEvents = 'auto';
        }
    });

    // Handle cancel button click
    cancelBtn.addEventListener('click', () => {
        // Reset form
        selectedFile = null;
        fileInput.value = '';
        fileInfo.style.display = 'none';
        controls.style.display = 'none';
        resultsContainer.style.display = 'none';
        progressContainer.style.display = 'none';
        progressFill.style.width = '0%';
        progressFill.style.backgroundColor = '#3498db';
        progressText.textContent = 'Processing...';
        transcribeBtn.disabled = true;
    });

    // Handle copy button click
    copyBtn.addEventListener('click', () => {
        const text = transcriptionText.textContent;
        navigator.clipboard.writeText(text).then(() => {
            const originalText = copyBtn.textContent;
            copyBtn.textContent = 'Copied!';
            setTimeout(() => {
                copyBtn.textContent = originalText;
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy: ', err);
            alert('Failed to copy text to clipboard');
        });
    });

    // Handle download button click
    downloadBtn.addEventListener('click', () => {
        const text = transcriptionText.textContent;
        const blob = new Blob([text], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `transcription_${new Date().toISOString().slice(0,19)}.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });
});