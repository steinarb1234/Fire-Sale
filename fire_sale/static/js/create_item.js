
document.addEventListener('DOMContentLoaded', () => {
    const addButton = document.querySelector('#add-image-button');
    const formsetContainer = document.getElementById('formset-container');
    const formTemplate = document.querySelector('#form-template');
    const totalFormsInput = document.querySelector('#id_form-TOTAL_FORMS');

    if (!addButton || !formsetContainer || !formTemplate || !totalFormsInput) {
      return
    }

    let formCount = totalFormsInput.value; // Initial form count
  
    addButton.addEventListener('click', () => {
      const clone = formTemplate.cloneNode(true);
      clone.removeAttribute('id');
      clone.removeAttribute('style');
  
      // Replace the __prefix__ placeholder with the formCount
      clone.innerHTML = clone.innerHTML.replace(/__prefix__/g, formCount);
  
      // Update the name attribute of the input field
      const imageInput = clone.querySelector('input[name$="image"]');
      imageInput.setAttribute('name', `form-${formCount}-image`);
  
      formsetContainer.appendChild(clone);
      formCount++;
  
      // Update the form-TOTAL_FORMS field value
      totalFormsInput.value = formCount;
    });
  });
  