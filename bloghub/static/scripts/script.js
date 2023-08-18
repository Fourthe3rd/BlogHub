document.addEventListener('DOMContentLoaded', function() {
    const postContainers = document.querySelectorAll('.article-content');
    const readMoreButtons = document.querySelectorAll('.read-more-btn');

    readMoreButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            postContainers[index].classList.toggle('expanded');
            if (postContainers[index].classList.contains('expanded')) {
                button.textContent = 'Read Less';
            } else {
                button.textContent = 'Read More';
            }
        });
    });
});
