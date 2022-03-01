# HTML

Instaces of errors and warning using [W3C Markup Validator](https://validator.w3.org/#validate_by_input) were caused by referencing views, urls through {{ input }} {% input %} and considered "Bad values". They were also caused by the validator missing that parts that actually are present through the base.html are missing in the separate templates since they are an extention of base.html. Booth of these kinds of errors were not demed a cause for concern.

# CSS

[W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check the code.

All warning was cause by supplier extensions and are not considered a cause for concern. profile.css went through the W3C validator without issues.

![](media/base-css.jpg)
![](media/checkout-css.jpg)

# JavaScript

The javascript code was tested with [JSHint](https://jshint.com/)


# PEP8

All python code went through a [PEP8 online test](http://pep8online.com/). Except for a few lines that were keept long because of not finding an appropriate way to indent them the code is clean.

# Manual Testing

* Index, logo rotates, works.
* Index page logo doubles takes a user to the products page, works.

* Favicon on all pages, works.
* Header filter works without issues.
* Header searchbar works without issues.
* Header cart takes the user to the cart works.
* Header cart, product count shows under if products are added, works.
* Header profile dropdown, takes a user to allauth sign up if sign in pressed.
* Header profile dropdown, takes a user to allauth sign in if sign in pressed.

* Product, all products show, works.
* Product on page filter, all works.
* Product, when a product is pressed a user comes to product details for the specific product, works.

* Product details, if "Back to Store" button pressed the user goes back to products page, works.
* Product details, if "Add to Cart" button pressed the product is added to the cart.

* Cart, only one of each product can be added to the cart since all products are unique, works.
* Cart, all added products is shown in the cart, works.
* Cart, product information is shown, works.
* Cart, product cab be deleted, works.
* Cart, total, delivery and grand total is calculated correctly, works.
* Cart "Back to Store" takes the user to product page.
* Cart "Checkout" button takes the user to the checkout page.

* Checkout, form with relevant delivery inputs, works.
* Checkout, faulty inputs in form are not accepted and what the customer needs to do is obvious after pressing      "Complete Order", works.
* Checkout, order summary, works.
* Checkout, "Create an account and "login" under form works and takes a user to respective alluth htmls, works.
* Checkout, "Adjust Cart" button works and takes a user to the cart.
* Checkout, if correct input in form, payment info and "Complete Order" button pressed the order goes through and the user is taken to the checkout succes page, works.
* Checkout, bought products are removed from site, works.
* Checkout success, order info shown, works.
* Checkout success, if "Back to Store" button pressed the user is taken back to products page, works.

* User Profile, can be created, works.
* User Profile, receive confirmation mail (tested via authors mail) and link that finalizes the profile, works.
* Profile info, can be saved and is shown during checkout, works.
* Profile info, past orders is shown on page, works.

* Superuser, add product, works.
* Superuser, edit product, works.
* Superuser, delete product from product page, works.
* Superuser, delete product from product details page, works.

Test card numbers.
![](media/cardnumbers.jpg)

* Stripe Webhooks, checkout succeedes with booth card numbers on page, works.
* Stripe Webhooks, payment goes through on Stripe, works.

![](media/cardnumbers.jpg)

# Device Testing

Phone:

* Samsung A52 - 
* Iphone 7 - 

Laptop:

* Mac Book Pro, Chrome - 
* Mac Book Pro, Firefox - 
* Mac Book Pro, Brave - 

Tablet: 

* Ipad A2270, Chrome - 