function changeContent(contentNumber) {
    var content1 = document.getElementById('overview_container');
    var content2 = document.getElementById('archive_container');
    var content3 = document.getElementById('org-container');

    // Hide all contents
    content1.style.display = 'none';
    content2.style.display = 'none';
    content3.style.display = 'none';

    // Show the selected content based on contentNumber
    if (contentNumber === 1) {
        content1.style.display = 'block';
    } else if (contentNumber === 2) {
        content2.style.display = 'block';
    } else if (contentNumber === 3) {
        content3.style.display = 'block';
    }
}