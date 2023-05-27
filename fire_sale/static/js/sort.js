document.addEventListener('DOMContentLoaded', () => {
  
  // Store references to the items container and sorting select element
  const itemsContainer = document.getElementsByClassName('card-grid')[0];
  const sortingSelect = document.getElementById('sort-selector');

  // Don't run the code if there is nothing to sort
  if (itemsContainer === null || sortingSelect === null) {
    return;
  }

  // Function to sort the items based on the selected option
  const sortItems = () => {
    const selectedOption = sortingSelect.value;
    let items = Array.from(itemsContainer.getElementsByClassName('card'));

    // Sorting based on the selected option
    items.sort((a, b) => {
      let aValue, bValue;

      if (selectedOption === 'name-a-z' || selectedOption === 'name-z-a') {
        // Sort by name
        aValue = a.querySelector('.card-title').textContent.toLowerCase();
        bValue = b.querySelector('.card-title').textContent.toLowerCase();
      } else if (selectedOption === 'price-hi-lo' || selectedOption === 'price-lo-hi') {
        // Sort by price
        aValue = parseFloat(a.querySelector('.card-text').textContent.replace('$', ''));
        bValue = parseFloat(b.querySelector('.card-text').textContent.replace('$', ''));
      } else if (selectedOption === 'date-new-old' || selectedOption === 'date-old-new' || selectedOption === 'sort'){
        // Sort by date (default)
        aValue = parseFloat(a.getAttribute("data-fs-item-id"));
        bValue = parseFloat(b.getAttribute("data-fs-item-id"));
      }

      if (selectedOption === 'name-z-a' || selectedOption === 'price-hi-lo' || selectedOption === 'date-old-new') {
        // Sort in descending order
        return (aValue < bValue) ? 1 : -1;
      } else {
        // Sort in ascending order
        return (aValue > bValue) ? 1 : -1;
      }
    });

    // Append sorted items to the container
    items.forEach(item => {
      itemsContainer.appendChild(item);
    });
  };

  // Sort items whenever the select option changes
  sortingSelect.addEventListener('change', sortItems);

  // Initial sorting
  sortItems();
});
