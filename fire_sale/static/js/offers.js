document.addEventListener('DOMContentLoaded', () => {
  document.addEventListener('click', async (event) => {
    if (event.target.matches('.btn-primary')) {
      const item_id = event.target.dataset.itemid;
      try {
        const response = await axios.get('/offers/open_offer_window/' + item_id);
        document.querySelector('.modal-body').innerHTML = response.data.html_form;
        document.querySelector('#offerModal').classList.add('show');
      } catch (error) {
        console.log(error);
      }
    }
  });
});
