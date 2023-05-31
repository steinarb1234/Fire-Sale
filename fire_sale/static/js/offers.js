document.addEventListener('DOMContentLoaded', function() {
  document.addEventListener('click', function(event) {
    if (event.target.matches('.btn-primary')) {
      var item_id = event.target.dataset.itemid;
      axios.get('/offers/open_offer_window/' + item_id)
        .then(function(response) {
          document.querySelector('.modal-body').innerHTML = response.data.html_form;
          document.querySelector('#offerModal').classList.add('show');
          attachFormSubmitHandler();  // Call this function after the form HTML is loaded
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  });
});



