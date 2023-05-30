const parseDate = (dateString) => {
  const parts = dateString.split("/");
  const day = parseInt(parts[0], 10);
  const month = parseInt(parts[1], 10) - 1; // Month is zero-based in JavaScript Date object
  const year = 2000 + parseInt(parts[2], 10); // Assuming year is in the range 2000-2099

  return new Date(year, month, day);
}


// Sort item cards. Used for category/index.html and watchlist/index.html

document.addEventListener('DOMContentLoaded', () => {
  
  const itemsContainer = document.getElementsByClassName('card-grid')[0];
  const sortingSelect = document.getElementById('sort-selector');

  if (itemsContainer === null || sortingSelect === null) {
    return;
  }

  const sortItems = () => {
    const selectedOption = sortingSelect.value;
    let items = Array.from(itemsContainer.getElementsByClassName('card'));

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
        aValue = parseInt(a.getAttribute("data-fs-item-id"));
        bValue = parseInt(b.getAttribute("data-fs-item-id"));
      }

      if (selectedOption === 'name-z-a' || selectedOption === 'price-hi-lo' || selectedOption === 'date-new-old' || selectedOption === 'sort') {
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

  // Initializing
  if (itemsContainer && sortingSelect) {
    sortingSelect.addEventListener('change', sortItems);
    sortItems();
  }
});



// Sort tables. Used for my_offers.html and my_listings.html

document.addEventListener('DOMContentLoaded', () => {
  
  const sortSelector = document.getElementById('sort-selector');
  const sortableTbody = document.querySelector('[data-sortable-table]');

  
  if (sortSelector === null || sortableTbody === null) {
    return;
  }

  const sortTable = () => {
    let selectedOption = sortSelector.value;

    if (selectedOption === 'sort' || selectedOption === '') {
      // Set default sorting to date-new-old
      selectedOption = 'date-new-old';
    }

    if (sortableTbody) {
      const rows = Array.from(sortableTbody.querySelectorAll('tr'));

      rows.sort((a, b) => {
        let aValue, bValue;

        if (selectedOption === 'name-a-z' || selectedOption === 'name-z-a') {
          // Sort by name
          aValue = a.querySelector('[data-sort-name]').textContent.toLowerCase();
          bValue = b.querySelector('[data-sort-name]').textContent.toLowerCase();
        } else if (selectedOption === 'price-hi-lo' || selectedOption === 'price-lo-hi') {
          // Sort by price
          aValue = parseFloat(a.querySelector('[data-sort-amount]').textContent.replace('$', ''));
          bValue = parseFloat(b.querySelector('[data-sort-amount]').textContent.replace('$', ''));
        } else if (selectedOption === 'date-new-old' || selectedOption === 'date-old-new' || selectedOption === 'sort'){
          // Sort by date (default)
          aValue = parseDate(a.getAttribute("[data-sort-date]"));
          bValue = parseDate(b.getAttribute("[data-sort-date]"));
        }
        console.log(`a: ${aValue} -  b: ${bValue}`)


        if (selectedOption === 'name-a-z') {
          return aValue.localeCompare(bValue);
        } else if (selectedOption === 'name-z-a') {
          return bValue.localeCompare(aValue);
        } else if (selectedOption === 'price-hi-lo' || selectedOption === 'date-new-old') {
          return bValue - aValue;
        } else if (selectedOption === 'price-lo-hi' || selectedOption === 'date-old-new') {
          return aValue - bValue;
        }
      });

      rows.forEach(row => {
        sortableTbody.appendChild(row);
      });
    }
  };

  // Initializing
  if (sortSelector && sortableTbody) {
    sortSelector.addEventListener('change', sortTable);
    sortTable();
  }
});