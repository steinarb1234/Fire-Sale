
// Get references to the filter button and filter content
const filterButton = document.getElementById('filter-button');
const filterContent = document.getElementById('filter-my-offers');

// Add click event listener to the filter button
filterButton.addEventListener('click', function() {
  // Toggle the display of the filter content
  filterContent.classList.toggle('show');
});