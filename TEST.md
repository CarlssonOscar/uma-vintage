# HTML

 [W3C Markup Validator](https://validator.w3.org/#validate_by_input) was used tfor the tests.
* base.html 
Since base.html is the page that all others extends from it has passed testing without issues.

* index.html
 ![](media/index.png)

* products.html
![](media/products.png)

* product_details.html
![](media/product-details.png)

* edit_product.html / custom_clerable_file_input.html

The errors all seem to be caused while rendering the form in forms.py, forms.py does how ever work as intended so a bit unclear if these errors are a cause of concern or not. The forms were rendered as cripsy forms which potentially could cause the problems. custom_clerable_file_input.html did not have any errors.

![](media/edit-product.png)

* add_product.html 
The errors all seem to be caused while rendering the form in forms.py, forms.py does how ever work as intended so a bit unclear if these errors are a cause of concern or not. The forms were rendered as cripsy forms which potentially could cause the problems.

![](media/add-product.png)

* cart.html
![](media/cart.png)

* checkout.html
![](media/checkout.png)

* checkout_success.html
![](media/success)

* profile.html
The error was cause by these lines of code and as obvious it's the validator that has missinterpreted the code. The same page-header code is present throught most of the files that extend from base.html and did not cause a error then.

![](media/cause-profile-error.png)

![](media/profile.png)

* login.html
![](media/signin.png)

* signup.html
![](media/signup.png)


# CSS

[W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check the code.

All warning was cause by supplier extensions and are not considered a cause for concern. profile.css went through the W3C validator without issues.

![](media/base-css.jpg)
![](media/checkout-css.jpg)

# JavaScript

The javascript code was tested with [JSHint](https://jshint.com/)


# PEP8

All python code went through a [PEP8 online test](http://pep8online.com/). 

* cart

apps.py

![](media/cart-apps.png)

contexts.py

![](media/cart-contexts.png)

urls.py

![](media/cart-urls.png)

views.py

![](media/cart-views.png)

* checkout

admin.py

![](media/ch-admin.png)

apps.py

![](media/ch-apps.png)

forms.py

![](media/ch-forms.png)

models.py

![](media/ch-models.png)

signals.py

![](media/ch-signals.png)

urls.py

![](media/ch-urls.png)

views.py

![](media/ch-views.png)

webhook-handler.py
The to long lines were left because of time restraints which did not enable enough time to find solutions.

![](media/ch-wh-handler.png)

webhooks.py

![](media/ch-webhooks.png)

* index

apps.py

![](media/ind-apps.png)

urls.py

![](media/ind-urls.png)

views.py

![](media/ind-views.png)

* products

admin.py

![](media/prod-admin.png)

apps.py

![](media/prod-apps.png)

forms.py

![](media/prod-forms.png)

models.py

![](media/prod-models.png)

urls.py

![](media/prod-urls.png)

views.py 
The to long lines were left because of time restraints which did not enable enough time to find solutions.

![](media/prod-views.png)

widgets.py
The to long line was left because of time restraints which did not enable enough time to find solutions.

![](media/prod-widgets.png)

* profiles

admin.py

![](media/prof-admin.png)

apps.py

![](media/prof-apps.png)

forms.py
The to long line was left because of time restraints which did not enable enough time to find solutions.

![](media/prof-forms.png)

models.py

![](media/prof-models.png)

urls.py 

![](media/prof-urls.png)

views.py

![](media/prof-views.png)

* uma 

setting.py

![](media/uma-settings.py)

urls.py

![](media/uma-urls.png)

wsgi.py

![](media/uma-wsgi.png)

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
* Checkout success, the customer receives a order confirmation email, works.

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

# Responsive design

## Pages availabel to all

* Large screen

Front page

![](media/front-page.png)

Header

![](media/ls-header.png)

Footer

![](media/ls-footer.png)

Products page

![](media/products.jpg)

Product details

![](media/ls-pd.png)

Cart

![](media/ls-cart.png)

Checkout

![](media/ls-ch.png)

Checkout success

![](media/ls-chs.png)

Sign in

![](media/ls-signin.png)

Sign out

![](media/ls-signout)

* Laptop

Front page
![](media/lt-fp.png)

Header

![](media/lt-header.png)

Footer

![](media/lt-footer.png)

Products

![](media/lt-prod.png)

Product details

![](media/lt-pd.png)

Cart

![](media/lt-cart.png)

Checkout

![](media/lt-ch.png)

Checkout success

![](media/lt-chs.png)

Sign in

![](media/lt-signin.png)

Sign out

![](media/lt-signout.png)

* Phone

Front-page

![](media/phone-fp.png)

Header

![](media/phone-header.png)

Footer

![](media/phone-footer.png)

Products

![](media/phone-prod.png)

Product details

![](media/phone-pd.png)

Cart

![](media/phone-cart.png)

Checkout

![](media/phone-ch-1.png)
![](media/phone-ch-2.png)

Checkout success

![](media/phone-chs1.png)
![](media/phone-chs2.png)

Sign in

![](media/phone-signin.png)

Sign out

![](media/phone-signout.png)

## Pages availabel to users with profiles

* Large Screen

Profile

![](media/ls-prof.png)

* Laptop

Profile

![](media/lt-prof.png)

* Phone

Profile

![](media/phone-prof1)
![](media/phone-prof2)

## Pages availabel to superusers

Products
Will only show one page since identical to products page except for edit | delete.

![](media/su-products.png)

* Large Screen

Add products

![](media/ls-add.png)

Edit products

![](media/ls-edit-product.png)

* Laptop

Add products

![](media/lt-add.png)

Edit products

![](media/lt-edit-product.png)

* Phone

Add products

![](media/phone-add1.png)
![](media/phone-add2.png)

Edit Products

![](media/phone-edit1.png)
![](media/phone-edit2.png)



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