document.getElementById('image').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.getElementById('imagePreview');
            img.src = e.target.result;
            img.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('audio').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const audio = document.getElementById('audioPlayer');
        audio.src = URL.createObjectURL(file);
        audio.style.display = 'block';
    }
});

document.getElementById('video').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const video = document.getElementById('videoPlayer');
        video.src = URL.createObjectURL(file);
        video.style.display = 'block';
    }
});
