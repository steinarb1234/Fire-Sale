document.addEventListener("DOMContentLoaded", () => {
    const userFormPrefix = "user-details";
    const userProfileFormPrefix = "user-profile-details";
    const paymentFormPrefix = "payment-details";
    let hasAlerted = false;
  
    const removeRequiredAttribute = (selector) => {
      const elements = document.querySelectorAll(selector);
      elements.forEach((element) => {
        element.removeAttribute("required");
      });
    };
  
    removeRequiredAttribute("#rating-section input");
    removeRequiredAttribute("#rating-section textarea");
  
    const showSection = (sectionToShow) => {
      const sections = [
        "#user-details",
        "#payment-details",
        "#rating-section",
        "#review",
      ];
      sections.forEach((section) => {
        if (section === sectionToShow) {
          document.querySelector(section).style.display = "block";
        } else {
          document.querySelector(section).style.display = "none";
        }
      });
    };
  
    const isFormFilled = (formPrefix) => {
        const formFields = document.querySelectorAll(`#${formPrefix} input[type='text']`);
      
        for (let i = 0; i < formFields.length; i++) {
          if (formFields[i].value.trim() === "") {
            return false; // Exit the loop if any field is empty
          }
        }
      
        return true;
    };
  
    const invalidInputHandler = (event) => {
      if (!hasAlerted) {
        alert("Please fill in all information for User details and Payment details.");
        hasAlerted = true;
  
        setTimeout(() => {
          hasAlerted = false;
        }, 500);
      }
    };
  
    const submitFormHandler = (event) => {
      const userFormFilled = isFormFilled(userFormPrefix);
      const userProfileFormFilled = isFormFilled(userProfileFormPrefix);
      const paymentFormFilled = isFormFilled(paymentFormPrefix);
  
      if (userFormFilled && userProfileFormFilled && paymentFormFilled) {
        populateReviewSection();
        showSection("#review");
      } else {
        invalidInputHandler();
      }
    };
  
    const populateReviewSection = () => {
        const formElements = document.querySelector("#checkout-form").elements;
        const formValues = Array.from(formElements).filter((element) => {
            return !element.classList.contains("btn");
        }).slice(1);
    

        console.log(formValues)
      
        const nameDict = [
          "Full name",
          "Email",
          "Country",
          "City",
          "Address",
          "Zip code",
          "Name of cardholder",
          "Card number",
          "Expiration date",
          "Cvs",
          "Rating",
          "Message",
        ];
      
        const userSection = document.querySelector("#review-user-details");
        const paymentSection = document.querySelector("#review-payment-details");
        const ratingSection = document.querySelector("#review-rating-section");
      
        userSection.innerHTML = "";
        paymentSection.innerHTML = "";
        ratingSection.innerHTML = ""; // Clear previous review details
        let targetSection = userSection; // Start with the user section

        formValues.forEach((field, index) => {
            const fieldName = nameDict[index];
            const fieldValue = field.value;
            
            console.log(`Index: ${index}, Field Name: ${fieldName}, Field Value: ${fieldValue}`)

            if (index === 6) {
                targetSection = paymentSection; // Switch to the payment section after "Name of cardholder"
            } else if (index === 10) {
                targetSection = ratingSection; // Switch to the rating section after "Rating"
            }

            if (fieldValue.trim() !== "") {
            const fieldElement = document.createElement("p");
            fieldElement.innerHTML = `<strong>${fieldName}:</strong> ${"   " + fieldValue}`;
            targetSection.appendChild(fieldElement);
            }
        });
      };
      
      
  
    const backButtonHandler = () => {
      showSection("#user-details");
    };
  
    const buyNowButtonHandler = (event) => {
      event.preventDefault();
      document.querySelector("#checkout-form").submit();
    };
    
    document.querySelectorAll(".errorlist").forEach(item =>{
      item.remove();
    });

    document.querySelectorAll("#checkout-form input[required]").forEach((input) => {
      input.addEventListener("invalid", invalidInputHandler);
    });
  
    document.querySelector("[data-checkout-review]").addEventListener("submit", submitFormHandler);
  
    document.querySelector("#back").addEventListener("click", backButtonHandler);
  
    document
      .querySelector("[data-checkout-confirm]")
      .addEventListener("click", buyNowButtonHandler);
  
    document.querySelector("#next").addEventListener("click", () => {
      showSection("#payment-details");
    });
  
    document.querySelector("#prev").addEventListener("click", () => {
      showSection("#user-details");
    });
  
    document.querySelector("#next-to-rating").addEventListener("click", () => {
      showSection("#rating-section");
    });
  
    document.querySelector("#prev-to-payment").addEventListener("click", () => {
      showSection("#payment-details");
    });
  });
  