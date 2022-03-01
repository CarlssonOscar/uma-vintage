![](media/front-page.jpg)
![](media/products.jpg)

## UX 
The design of the website has been a collaboration with the author and the storeowners ideas for how the store should look. The minimalist design has it's limitations in terms of UX since it can come of as unclear. I'm aware that the lack of langueage could be a cause for concern since how to use the site can vauge to some people. But since it was pretty much a requirement from the client to keep language to a minimum I've tried to use as familiar symbols a possible to minimize confusion.

On the first page on is greeted with a spinning company logo. The company logo is based on a LP shape, the choice to rotate it for this reason probably is obvious. The first idea was to spin the LP in the same pace as it normally would, which is 33 roations a minute. Unfortunatly this made it possible to read what is written on the logo so a slower rotation speed was settled on.

The goal with the different parts of the site has been to keep them as similar as possible. 
The sites main color is white with black text, symbols and buttons. The choice to use white is a decision made with the intention to keep the content in focus, it was also based on the whishes of the client.

The footer is despite it's languge very similar to the header in terms on design, the letters are bold and the Facebook and Instagram logos is a familiar symbol to most people. 

## User Stories

![](media/user-stories.jpg)

## Features

### Header

Except for showing the name of the company which takes one to the front-page the header of the page has svereal functionalites. The drop down menu on the left is a filter, a user can filter through the products by price, category, clothing and go back to show all.
On the right there are three symbols the first symbolises a profile, it gives one the ability to sign in or up. What is possible while logged in as a user or superuser will be covered later on. The second symbol is a cart it takes one to the customers cart. If a product has been added a circle is shown under the cart with a number which shows how many products are in the cart. The color of the circle is based on onw of the colors in the logo. The third displays a searchbar while clicked it displays a input field.

### Footer

The footers content consist of a copyright symbol, about page and contact page links that are intended to be created in future and a facebook link that would guide one to a facebook page if there was one. Instead screenshots of the facebook page are shown later in the README.

### Products page

After one has entered the site via the index page one is greeted with all products available on the site. When having scrolled to the bottom of the page there is a arrow symbol which when clicked sends the user back to the top of the page.

### Product details pages

When clicking on a product the user is shown info about the product and is given the option to add the product to the cart or go back to the store.

### Cart page

The cart displays the products that are in the cart, some general info about the products and the total, delivery cost and grand total.

### Profile

Users of the site can create their own profile, the main features availbable to a user is being able to save their delivery info and keep track of previous orders.

### Superuser

On top of the features availabel to a regular profile a supersusers profile has the abillity to add, edit and delete products from the site without having to use the admin page. 

### SKU

Since each product on the site is unique a product can not be added more than once and the maximum quantity is one. After the checkout the product is deleted.

### Messages

Depending on what a user or superuser does on the site their are associated toast messages to clarify if an action went according to plan, if there are any issues with the site or the way an action was performed.

### Checkout page

The checkout page displays a form with details that fully or partially needs to be filled in depending on if the user has a profile or not and if the user has saved its delivery information previously. The form also includes an input field for payment information. The page also includes an order summary and finally two button which let one go back to the cart or go through with the order.

### Stripe 

Users can checkout using [Stripe](https://stripe.com/docs/security/stripe), which is a well establised and safe payment provider.

### Checkout success page

If the form was filled in correctly and the payment goes through one is sent to the checkout success page. It confirms to the customer that the order went through and shows the order info as well as a button that takes one back to the store.

## Future features

The footer does at this point have a about and contact link that does now work. The to links seem resonable to have if this was a working site, but I'm choosing to not priotitize this because of time issues and that it would not fill a purpose just yet.
* Create a about page with the story about the company and pictures of the store.
* Create a contact page.

## Facebook page

![](media/facebook.jpg)

## Testing

The testing can be found [here](test.md).

## Deployment

### **Forking**

If you wish to use this repository as a starting point or to propose changes to this project, you can fork it. Follow the steps below.

1. Navigate to the repository [CarlssonOscar/uma-vintage](https://github.com/CarlssonOscar/uma-vintage)
2. Click 'Fork' in the top-right corner.

### **Cloning**

Cloning a repository creates a local copy on your computer. Follow the steps below.

1. Navigate to the repository [CarlssonOscar/uma-vintage](https://github.com/CarlssonOscar/uma-vintage)
2. Click 'Code' above the list of files.
3. In the new window, cloning using HTTPS is the default option. Copy the provided link manually or by clicking on the clipboard symbol.
4. Open your preferred terminal.
5. Navigate to your desired directory for the cloned project.
6. Type `git clone https://github.com/CarlssonOscar/uma-vintage.git` or paste the copied address from step 3.
7. Press **Enter** to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/CarlssonOscar/uma-vintage)

### **Deploy remotely**

To deploy the site remotely on [Heroku](https://www.heroku.com/) please follow the steps below.

1. Create either a **requirements.txt** file with `pip3 install -r requirements.txt`, to enable Heroku to install the required dependencies for the app.
2. Create a **Procfile** with the content `web: gunicorn uma.wsgi`. Remove any blank lines at the end as they may cause errors.
3. Register a free Heroku account, if you don't have one already, sign in and create the app.
4. Select the **Deploy** tab and choose **GitHub** as **Deployment Method**.
5. Select the **Settings** tab and click on **Reveal Config Vars** in the section **Config Vars**. Add the following variables:

    - DATABASE_URL: `<your Postgress db URL from Heroku>`
    - SECRET_KEY: `<your secret key>`
    - CLOUDINARY_URL: `<your Cloudinary key>`
    - STRIPE_SECRET_KEY: `<your Stripe secret key from the Stripe dashboard>`
    - STRIPE_PUBLIC_KEY: `<your Stripe public key from the Stripe dashboard>`
    - STRIPE_WEBHOOK_KEY: `<your Stripe webhook key. Only necessary if using webhooks.>`
    - EMAIL_HOST_PASS: `<your project email password>`
    - EMAIL:HOST_USER: `<your project email address>`
    - DEBUG: `False`
        - Set this value to 'True' when updating the code.
        - **In any other case set it to 'False' or remove it to avoid remote code execution!**

6. Push the **Procfile** to your GitHub repo.
7. Back under the **Deploy** tab in Heroku enable **Automatic deploys**.
8. Select the **main branch** and click on **Deploy branch**.
9. Wait for the message 'Your app was successfully deployed' and then click **View** to start your app in the browser.

 Here is a link to the finished project [Úma](https://uma-vintage.herokuapp.com/).

## Credits


## Acknowledgements 
My mentor Tim Nelson for providing excellent mentoring booth in terms of technical ability as well as being encouraging and motivating.

[Code Institute](https://codeinstitute.net) for providing excellent course material and tutoring.
