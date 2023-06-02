# REQUIREMENTS

Below are all functionalities of the website, required and extra. The extra requirements are highlighted in **bold**.

* Authentication
   * Login
   * Register
     * **Username**
     * **Password**
     * Name
     * **Email**
     * **Country**
     * **Address (optional)**
     * **City (optional)**
     * **Zip code (optional)**
     * Bio **(optional)**
     * Image **(optional)**
* Layout site
   * Navigation bar
     * Profile image
     * **Navigation bar includes search bar, allowing users to start searching immediately.**
       * **The search bar can both filter the search by a certain category and search all categories at once.**
     * **Navigation bar includes list of all categories, allowing users to easily navigate to their desired category.**
     * **Navigation bar includes a notification bell and notification indicator.**
       * **The notification indicator shows the number of notifications the user has not yet looked at.**
     * **Navigation bar includes the users profile image (or default icon if user has no image) as a clickable drop-down menu, giving the user quick access to various key parts of the site.**
       * **Navigation bar provides quick access to "Create listing" and "Watchlist".**
     * Average rating **(can be seen by clicking on the user's profile image)**
     * Logout **(can be seen by clicking on the user's profile image)**
   * Footer
* Home site
    * **Masthead**
      * Advertisement displayed at the top of the home site which links to all items sorted by listing date
    * **Category preview**
      * Below the masthead are all categories shown in a category preview slide ordered by your most viewed categories.
* Edit profile
   * Name
   * **Username**
   * **Email**
   * Bio
   * **Country**
   * **Address**
   * **City**
   * **Zip code**
   * Image
* Catalog site - lists available items for auction **(called "All" in the category drop down)**
   * Search (based on name)
   * Order by
     * Price
     * Name
     * **Date listed**
   * Each item should be clickable, which navigates to the item detail site
* **Category site** similar to the catalog site, but specific for each category
  * **Sub-category items also show up on parent-categories sites.**
* Create an item **("Create listing" in the lower nav bar)**
   * Name
   * **Category**
   * **Price**
   * Condition
   * Long description
   * Images
     * **(User can add multiple images via an "Add image" button and remove images by checking the "Delete:" checkbox)**
* Item detail site - shows more information about a certain item
   * Name
   * **Price**
   * Current highest offer
   * **Number of offers**
     * **Clickable link which leads to a list of all offers.**
       * **Offers are anonymous to all but seller.**
   * A button which allows you to place an offer
   * **A button which allows you to add to your watchlist.**
   * Long description
   * Images
     * **Images are fully visible, nothing is cut off and the image is neither streched nor squished.**
     * **If more than one image was uploaded for the specific item, the user can navigate between the pictures using either arrows on the side of each picture, or by clicking the image carousel indicators.**
   * **Number of views the item has gotten.**
   * **Number of people with the item in their watchlist.**
   * **Information on if the item is sold or not.**
   * Condition
   * **Seller information**
     * **Name**
     * **Average rating**
     * **Location**
   * A list of similar items **(from the same category)**
* Placing an offer
   * All items which are available (they don’t have an accepted offer) can receive
an offer
   * Users can send multiple offers, until the owner of the item accepts an offer
   * All users who placed an offer on an item should be notified when an offer has
been accepted. The one that made the accepting offer should be notified
that his offer has been accepted, but all others should be notified that their
offer was declined. **Notifications are handled as push-notifications, displayed in the nav bar.**
* **Offer details site**
  * **Contains all relevant information on the item, the offer and buttons with actions the user can take.**
    * **If the users offer is pending, the actionss are "Edit offer" and "Withdraw offer".**
    * **If the users offer is rejected, there are no actions.**
    * **If the users offer is accepted, the actionss are "Go to checkout" and "Withdraw offer".**
    * **If the item was purchased through the offer, there are no actions.**
* **The user can see a list of all of their offers.**
  * **They can be sorted by name, offer amount and date.**
  * **The list contains most relevant information for the user to have, as well as quick-action buttons and a link to the offer details site and a list of all offers made on the item.**
* Checkout
   * The user with the accepting offer must checkout in order to finalize the sale
of the item
   * There should be three stages of the checkout phase
     * Contact information
       * Full name
       * **Email**
       * Country (displayed as a `<select>` HTML element)
       * City
       * **Address (*Street name and house number combined*)**
       * **Zip** code
     * Payment
       * Name of cardholder
       * Card number
       * Expiration date
       * CVC
     * (Optionally) Rate the seller
       * **Rating (0-5, decimal number)**
       * **Message**
     * Review (a read-only site where a user can review what he is buying
and what information he has already typed in)
     * Confirm
       * Easy navigation between steps - it should be easy to navigate between the
steps in the checkout

