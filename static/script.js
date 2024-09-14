document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('resume-form');
    const fileInput = document.getElementById('linkedin-pdf');
    const fileName = document.getElementById('file-name');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const viewResumeBtn = document.getElementById('view-resume');

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            fileName.textContent = e.target.files[0].name;
        } else {
            fileName.textContent = 'No file chosen';
        }
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        loading.classList.remove('hidden');
        form.classList.add('hidden');

        try {
            const response = await fetch('/generate_resume', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                result.classList.remove('hidden');
                viewResumeBtn.href = data.file_path;
            } else {
                throw new Error(data.message || 'An error occurred');
            }
        } catch (error) {
            alert('Error: ' + error.message);
            form.classList.remove('hidden');
        } finally {
            loading.classList.add('hidden');
        }
    });

    // Add some animation to the background
    const backgroundAnimation = document.querySelector('.background-animation');
    let angle = 0;

    function animateBackground() {
        angle = (angle + 0.1) % 360;
        backgroundAnimation.style.background = `linear-gradient(${angle}deg, #0077b5, #00a0dc)`;
        requestAnimationFrame(animateBackground);
    }

    animateBackground();
});
