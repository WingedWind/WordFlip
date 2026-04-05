document.addEventListener('DOMContentLoaded', function() {
    const existingBtn = document.getElementById('existing-collection-btn');
    const newBtn = document.getElementById('new-collection-btn');
    const existingGroup = document.getElementById('existing-collection-group');
    const newGroup = document.getElementById('new-collection-group');
    existingBtn.addEventListener('click', function() {
        existingBtn.classList.add('active');
        newBtn.classList.remove('active');
        existingGroup.style.display = 'block';
        newGroup.style.display = 'none';
    });

    newBtn.addEventListener('click', function() {
        newBtn.classList.add('active');
        existingBtn.classList.remove('active');
        newGroup.style.display = 'block';
        existingGroup.style.display = 'none';
    });
});
