
const dropArea = document.getElementById('drop-area');

// Prevent the default behavior of file dropping on the page
dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.border = '2px dashed #333';
});

dropArea.addEventListener('dragleave', () => {
    dropArea.style.border = '2px dashed #ccc';
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.style.border = '2px dashed #ccc';

    const files = e.dataTransfer.files;

    handleFiles(files);
});

const clickHere = document.querySelector(".upload button");
console.log(clickHere);