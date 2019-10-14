const imageUpload = document.getElementById('id_image');
const imageFileName = document.getElementById('imageFileName');
const uploadForm = document.getElementById('uploadForm');

imageUpload.addEventListener('change', (e) => {
    const filename = e.target.files[0].name;
    imageFileName.innerText = filename;
});


function submitForm(e) {
    if (imageFileName.innerText == '') {
        const errorMessage = document.getElementById('uploadError');
        errorMessage.style.display = 'block';
    } else {
        uploadForm.submit();
    }
}
