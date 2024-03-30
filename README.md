# CSE471


## Module - 1: User Authentication

### Feature 1: Signup

Allow users to register by providing their name, email, password and confirmation password.

**Validation during signup:**

* Ensure uniqueness of email addresses associated with user accounts.
* Passwords must be at least 8 characters long.
* Passwords must contain at least one uppercase letter, one digit, and one special character.

### Feature 2: Sign In

Enable users to log in using their email and password

**Error Handling:**

* Display an error message for invalid credentials if the user enters an incorrect email and password.

### Feature 3: Profile Management

Provide users with the ability to view, update and delete their profile information

* Users can view their personal info while logged in

**Update Profile:**

* Users can update their personal information and add additional details

**Email update validation:**

* Validate email updates to ensure that the entered email is not already associated with another user account.
* Display an error message and prompt the user to enter a different email if the provided email is already in use.

**Account deletion:**

* Users navigate to their profile
* They select the option to delete their account
* A confirmation popup appears, prompting the user to confirm the irreversible deletion process by clicking "Confirm" or to cancel by clicking "Cancel"
* Before confirmation they have to provide their password for extra layer of security
* If the user clicks "Confirm", the account deleted and take him to the home page with a success message
* If the user clicks "Cancel," the deletion process is cancelled, and the user will remain on their profile page without any changes.


### Feature 4: Password Reset

Allow users to reset their password if forgotten.

* **Password reset procedure:**
    * Users can request a password reset link via email.
    * Upon clicking the link, users can reset their password securely.

### Feature 5: Sign Out

Provide users with the option to securely log out of their accounts.



## Module - 2: Property Information

### Feature 1: Property Listings

* Allow users to explore a wide range of properties listed for sale or rent, including residential, commercial, and land types.
* Display basic info about different properties on the property listings page.

### Feature 2: Property Details

* Enable users to view detailed information about individual properties.
* Display the property-agent name who approved the property for listings.

### Feature 3: Add Property

Allow logged-in users to list their property for sale or rent by filling out a listing form. Support property types including residential, commercial, and land.
* After adding the property user must wait from arrpoval for the agent
* Once approved, the listed properties become available on our Property   Listing page for public viewing
* Users have access to a "View Posted Properties" page where they can see all the properties they have listed both approved and not approved

### Feature 4: Property Documents

* Users can provide property documents (PDFs, Docs, images, etc.) during the property addition process.
* Agents can view and approve properties based on the submitted documents.

### Feature 5: Update Property

* Provide users with the ability to update property information as needed.
* Offer an "Update Property" button on the property details page for convenient access.
* Restrict property updates to the original user who posted the property.



## Feature 6: Delete Property

Allow users to delete their listed properties.

**Procedure:**

* User can delete their listed property by clicking the delete button on the property details page.
* The "Delete Property" option is available on the property details page.
* Only the user who posted the property can delete it.


## Feature 7: Property Calculator

This feature helps users estimate the total price without manually using their phone or calculator.

* Users enter the property's price and area.
* The system calculates the estimated total price.




## Module 3: User Interaction

### Feature -1: Agent Profile

Beside our customer, we have our agent team. Agent team is responsible to approve, cancel or review the posted properties. When an agent logs in, they have a dashboard from where they can approve or cancel a property after viewing the property document.

### Feature - 2: Feedback and Rating

Allow our valued customers to give their review and star rating based on their experience with us. Reviews will be displayed based on star ratings. A higher star rating will appear first

**Validation:**

* The reviewer cannot leave any field blank while submitting the form. If they do, the system will notify them with an error message. Otherwise, the user will be notified with a success message that the review was submitted successfully.

* If a reviewer has already submitted a review and wants to update it, their review and rating will be updated based on the present review and rating. The system will notify the reviewer with a success message that the review was updated successfully.

### Feature 3: Email Subscription

Allow users to subscribe with their email. Subscribers will get updates and news occasionally on their email from our website. An agent can send emails to the subscribers.

### Feature 4: Customer Support

Allow users to share their problems, experience or seek support from us.

**Procedure:**

* Users can find support forms on the contact page.

* They can fill out the form with their email address.

* The user will receive a confirmation message on their email.

* Our customer support team will review the email and give feedback to the user within the shortest possible time.



## Module 4: Advanced Features

### Feature 1: Basic search and filter

Allow users to search property based on property type, property on: sale/rent and area.

* **Procedure:**
  * Users will find basic search options on the home page.
  * System will show result based on their selected criteria

### Feature 2: Advanced Filtering

Allow users to filter property based on different types of criteria to find their desired property. Advanced filtering option available on both property list and posted property pages.

* **Procedure:**
  * Users primarily find property type, property on: sale/rent, area and sorting(default, Ascending, Descending) based on price option.
  * Property type specific field will be available when user select specific property type
  * After clicking apply filter, user will see result based on his/her selected criteria

### Feature 3: Saved Search

Allow users to save the selected filter criteria for future use with a given name. They can see their saved search item on the saved search page.

* **Constraints:**
  * Users only have 12 saved searches at a time. To add more he/she needs to delete saved searches from previous ones.
  * Duplicate name for saved search is not allowed

### Feature 4: Pagination

Pagination is helpful to display property lists in a more organised way. Pagination available on the property list, posted property list and testimonial pages


## Feature 5: Auction

Allows users to put their property on auction on our page. Other users can bid on that property within a timeframe. To participate in auction users have to pay a security money through payment gateway.

* **Procedure:**
  * User can list their property for auction with a starting price and set a duration for the auction.
  * Other users can see the listed properties for auction.
  * Interested users can place their bid on a property during the auction time.
  * The highest bidder wins the property at the end of the auction.
  * The winner will be charged the winning bid amount and the security money will be refunded to others who participated in the bidding on that property.

* **Note:**
    * Security money will be refunded only to those who did not win the bid.

## Feature 6: Payment Gateway

Payment gateway helps the user to purchase different subscription or services from the website.

* **Services available through Payment Gateway:**
    * Pay security money to participate in the auction.
    * Users can purchase premium plans with additional benefits.
