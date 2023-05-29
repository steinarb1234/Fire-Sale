// Search bar - updating category from dropdown

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('search-form');
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const categoryOptions = document.querySelectorAll('.category-option');

    categoryOptions.forEach(option => {
        option.addEventListener('click', e => {
            e.preventDefault();
            const category = option.textContent;
            form.action = `/categories/${category}`;
            dropdownToggle.textContent = `Search by: ${category}`;
        });
    });
});