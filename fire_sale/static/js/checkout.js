$(document).ready(function(){

            $("#rating-section input").removeAttr("required");
            $("#rating-section textarea").removeAttr("required");
            
            $("#next").click(function(){
                $("#user-details").hide();
                $("#payment-details").show();
                checkFormCompletion();
            });

            $("#prev").click(function(){
                $("#payment-details").hide();
                $("#user-details").show();
                checkFormCompletion();
            });

            $("#next-to-rating").click(function(){
                $("#payment-details").hide();
                $("#rating-section").show();
                checkFormCompletion();
            });

            $("#prev-to-payment").click(function(){
                $("#rating-section").hide();
                $("#payment-details").show();
                checkFormCompletion();
            });

            // Function to check form completion and update button text
            function checkFormCompletion() {
                var userFormFilled = isFormFilled(userFormPrefix);
                var userProfileFormFilled = isFormFilled(userProfileFormPrefix);
                var paymentFormFilled = isFormFilled(paymentFormPrefix);

                if (userFormFilled && userProfileFormFilled && paymentFormFilled) {
                    $("#checkout-form input[type='submit']").val("Review checkout");
                    //$("#checkout-form input[type='submit']").attr("formaction", "javascript:void(0)");
                } else {
                    $("#checkout-form input[type='submit']").val("Buy now");
                    //$("#checkout-form input[type='submit']").removeAttr("formaction");
                }
           }

            // Function to check if a specific form is filled
            function isFormFilled(formPrefix) {
                console.log(formPrefix)
                var formFields = $("#" + formPrefix + " input[type='text']");
                var isFilled = true;

                formFields.each(function() {
                    if ($(this).val().trim() === "") {
                        isFilled = false;
                        console.log("0")
                        return false; // Exit the loop if any field is empty
                    }
                });
                console.log(isFilled)
                return isFilled;
            }

            let hasAlerted = false;

            $("#checkout-form :input[required]").on('invalid', function() {
                if (!hasAlerted) {
                    alert('Please fill in all information for User details and Payment details.');
                    hasAlerted = true;

                    // Reset the flag after a delay to allow for subsequent alerts if needed
                    setTimeout(() => {
                        hasAlerted = false;
                    }, 500);
                }
            });

            // Display the review section when all forms are filled
            $("#checkout-form").submit(function() {
                
                event.preventDefault(); 

                var userFormFilled = isFormFilled(userFormPrefix);
                var userProfileFormFilled = isFormFilled(userProfileFormPrefix);
                var paymentFormFilled = isFormFilled(paymentFormPrefix);

                if (userFormFilled && userProfileFormFilled && paymentFormFilled) {
                    populateReviewSection();
                    $("#review").show();
                    $("#user-details").hide();
                    $("#payment-details").hide();
                    $("#rating-section").hide();
                    $("#checkout-form input[type='submit']").val("Buy now");
                }
            });

            // Populate the review section with form values
            function populateReviewSection() {
                console.log("yi")
                var formValues = $("#checkout-form").serializeArray().slice(1);
                console.log("Form values: ", formValues);

                // Clear previous review details
                $("#main-header").empty();
                $("#review-user-details").empty();
                $("#review-payment-details").empty();

                // Display user details and payment details
                var name_dict = ['Full name', 'Email', 'Country', 'City', 'Address', 'Zip code', 'Name of cardholder', 'Card number', 'Expiration date', 'Cvs', 'Rating', 'Message'];
                var userSection = $("#review-user-details");
                var paymentSection = $("#review-payment-details");

                for (var i = 0; i < formValues.length; i++) {
                    var fieldName = name_dict[i];
                    var fieldValue = formValues[i].value;

                    // Determine the target section based on index
                    var targetSection = (i < 6) ? userSection : paymentSection;

                    // Add an indent to the field value
                    fieldValue = "   " + fieldValue;

                    // Append the field to the target section
                    targetSection.append("<p><strong>" + fieldName + ":</strong> " + fieldValue + "</p>");
                }
            }
            
            // Back button functionality
            $("#back").click(function() {
                $("#review").hide();
                $("#user-details").show();
                $("#payment-details").hide();
                $("#rating-section").hide();
                checkFormCompletion();
            });


              // Add your Buy Now button click event listener here
            $("#review input[type='submit']").click(function(event){
                event.preventDefault();
                $("#checkout-form").submit();
            });

        });