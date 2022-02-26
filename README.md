![](media/front-page.jpg)
![](media/products.jpg)

# UX 
The design of the website has been a collaboration with the author and the storeowners ideas for how the store should look. The minimalist design has it's limitations in terms of UX since it can come of as unclear. I'm aware that the lack of langueage could be a cause for concern since how to use the site can vauge to some people. But since it was pretty much a requirement from the client to keep language to a minimum I've tried to use as familiar symbols a possible to minimize confusion.

On the first page on is greeted with a spinning company logo. The Logo is based on a LP shape, the choice to rotate it for this reason probably is obvious. The first idea was to spin the LP in the same pace as it normally would, which is 33 roations a minute. Unfortunatly this made it possible to read what is written on the logo so a slower rotation speed was settled on.

The goal with the different parts of the site has been to keep them as similar as possible. 
The sites main color is white with black text, symbols and buttons. The choice to use white is in part a decision made with the intention to keep the content in focus. Another aspect is that the author is not famililar with many photos direction tools, the index page rotating photo has a white background.

The footer is despite it's languge very similar to the header in terms on design, the letters are bold and the Facebook logo is a familiar symbol to most people. 

# User Stories

![](media/user-stories.jpg)

# Features

## Header

Except for showing the name of the company which takes one to the front-page the header of the page has svereal functionalites. The drop down menu on the left is a filter, a user can filter through the products by price, category, clothing and go back to show all.
On the right there are three symbols the first symbolises a profile, it gives one the ability to sign in or up. What is possible while logged in as a user or superuser will be covered later on. The second symbol is a cart it takes one to the customers cart. If a product has been added a circle is shown under the cart with a number which shows how many products are in the cart. The color of the circle is based on onw of the colors in the logo. The third displays a searchbar while clicked it displays a input field.

## Footer

The footers content consist of a copyright symbol, about page and contact page links that are intended to be created in future and a facebook link that would guide one to a facebook page if there was one. Instead screenshots of the facebook page are shown later in the README.

## Products page

After one has entered the site via the index page one is greeted with all products available on the site. When having scrolled to the bottom of the page there is a arrow symbol which when clicked sends the user back to the top of the page.

## Product details pages

When clicking on a product the user is shown info about the product and is given the option to add the product to the cart or go back to the store.

## Cart page

The cart displays the products that are in the cart, some general info about the products and the total, delivery cost and grand total.

## Profile

Users of the site can create their own profile, the main features availbable to a user is being able to save their delivery info and keep track of previous orders.

## Superuser

On top of the features availabel to a regular profile a supersusers profile has the abillity to add, edit and delete products from the site without having to use the admin page. 

## SKU

Since each product on the site is unique a product can not be added more than once and the maximum quantity is one. After the checkout the product is deleted.

## Messages

Depending on what a user or superuser does on the site their are associated toast messages to clarify if an action went according to plan, if there are any issues with the site or the way an action was performed.

## Checkout page

The checkout page displays a form with details that fully or partially needs to be filled in depending on if the user has a profile or not and if the user has saved its delivery information previously. The form also includes an input field for payment information. The page also includes an order summary and finally two button which let one go back to the cart or go through with the order.

### Stripe

# Facebook page

![](media/facebook.jpg)

### Checkout success page

If the form was filled in correctly and the payment goes through one is sent to the checkout success page. It confirms to the customer that the order went through and shows the order info as well as a button that takes one back to the store.

# Future features

The footer does at this point have a about and contact link that does now work. The to links seem resonable to have if this was a working site, but I'm choosing to not priotitize this because of time issues and that it would not fill a purpose just yet.
* Create a about page with the story about the company and pictures of the store.
* Create a contact page.

# Testing

The testing can be found [here](test.md).


# Unfixed Bugs


# Deployment
Deployment on Heroku.
1. After login click New button in the right top corner.
2. Chose app-name and region.
3. Choose settings in the bar.
4. Click reveal Config Vars and add Key Port and the Value 8000.
5. Add the buildpack heroku/python and heroku/nodejs in this order.
6. Click on Deploy in the bar.
7. Click on connect on github in the Deployment method section.
8. Click search in the connect to GitHUb section and choose the relevant github repository.
9. Click on Automatic deploys or manual deploy depending on preference. Manual deploy was chosen for this      project.

 Here is a link to the finished project [Úma](https://uma-vintage.herokuapp.com/).

# Credits
TIM!!!


# Acknowledgements 

[Code Institute](https://codeinstitute.net) for providing excellent course material and tutoring.