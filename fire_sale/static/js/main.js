
const getCSRFToken = () => {
    const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      .split('=')[1];
    return cookieValue;
  };


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

// Item card hearts - updating filled/empty and adding to/removing from watchlist 

document.addEventListener('DOMContentLoaded', () => {
    axios.defaults.headers.common['X-CSRFToken'] = getCSRFToken();

    const heartIcons = document.querySelectorAll('.card-heart');

    if (heartIcons === null) {
        return;
    }

    heartIcons.forEach(heartIcon => {
        heartIcon.addEventListener('click', async event => {
        event.preventDefault();
        const heartIcon = event.target
        const card = heartIcon.closest('.card');
        const itemId = card.dataset.fsItemId;

        // Check if the heart icon is filled or not
        const isFilled = heartIcon.classList.contains('card-heart-filled');

        // Make an Axios request to update the watchlist
        try {  
            // Update the heart icon on success
            if (isFilled) {
                heartIcon.classList.remove('card-heart-filled');
                await axios.post(`/watchlist/delete_from_watchlist/${itemId}`);
            } else {
                heartIcon.classList.add('card-heart-filled');
                await axios.post(`/watchlist/add_to_watchlist/${itemId}`);
            }
          } catch (error) {
            console.error('Error:', error);
          }
        });
    });
});
