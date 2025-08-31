# 📘 Fly Wheels
**Fly Wheels** is a Django-based full-stack e-commerce web application for car enthusiasts to explore and purchase high-quality alloy and track edition wheels. Users can browse categories, filter by size and style, view detailed product pages, and manage their shopping cart through a streamlined checkout process.

## 🔗 Live Demo

[Fly Wheels App]()

[GitHub Repository](https://github.com/TinaGrigorova/fly_wheels)

---

## User Experience (UX)

Fly Wheels delivers a modern and performance-driven shopping experience tailored for car owners and motorsport enthusiasts. The platform is designed with intuitive navigation, responsive layouts, and clear call-to-action elements that guide users from product discovery to secure checkout.
Whether customers are looking for stylish alloy wheels for their daily car or track-ready editions for motorsport use, Fly Wheels offers categorized browsing, filtering options, and seamless cart management. The application is fully responsive, ensuring effortless shopping on desktop, tablet, and mobile devices.
Project Goals
The goal of the Fly Wheels project is to provide users with a sleek, accessible, and engaging e-commerce platform for purchasing automotive wheels. The project focuses on simplifying the shopping journey while offering detailed product insights and flexible cart functionality.
By integrating categories, cart management, and checkout, Fly Wheels aims to replicate a professional e-commerce experience while leaving room for future scalability, such as wishlist functionality, customer reviews, and testimonials.

### Project Goals

The goal of the Fly Wheels project is to provide users with a modern, accessible, and engaging e-commerce platform for exploring and purchasing high-quality alloy and track edition wheels. The project focuses on simplifying the shopping experience while offering clear product information, category separation, and dynamic cart functionality. By centralizing product browsing, filtering, and checkout processes, Fly Wheels aims to deliver a professional and user-friendly online shop for car enthusiasts.

### Agile Methodology

Agile Methodology was adopted to efficiently plan, execute, and iterate development for Fly Wheels. A GitHub Project Board and a user story template were used throughout the project lifecycle.
* Epics were defined to group user stories under broader goals (e.g., Product Browsing, Cart & Checkout, User Authentication).
* User Stories were written in the format:
As a [user], I can [action] so that [goal] — with clear acceptance criteria.
* The GitHub Project Board was made public to track progress across columns: To Do, In Progress, and Done.
* Labels (Bug, Enhancement, Testing, Priority) were applied to issues for visibility and prioritization.
* Iterative development ensured continuous improvements based on testing feedback and alignment with user experience goals.


### User Stories

#### Epics
Initial Deployment
Home Page & Navigation
User Registration & Authentication
Product Browsing & Shop
Cart & Checkout
Website Admin & Product Management
Maintain consistent design with responsiveness in mind

#### User Stories
1. Initial Deployment
* Create new Heroku application
* Link GitHub repository to the Heroku app
2. Home Page & Navigation
* Create a navigation bar with links to Shop, Cart, and Login/Signup
* Create a footer with relevant links and contact details
* Display featured products on the homepage
3. User Registration & Authentication
* Sign Up page for new users
* User login and logout functionality
* Display logged-in user’s name
* Email confirmation after registration
4. Product Browsing & Shop
* Display wheels categorized as Alloy Wheels and Track Edition
* Filter products by brand, size, and style
* Product detail page with image, description, and price
5. Cart & Checkout
* Add products to cart from product or category pages
* View cart summary with product details and totals
* Update product quantities in cart
* Remove products from cart
* Checkout page with order confirmation
* Pay with card option (Stripe integration planned)
* Website Admin & Product Management
6. Admin panel for managing products and categories
* CRUD functionality for adding, editing, and deleting products
* Alert messages for admin actions (e.g., product added, updated, deleted)
7. Order management in admin panel
* Maintain consistent design with responsiveness in mind
* Maintain consistent modern design across all pages
* Test responsiveness on desktop, tablet, and mobile devices

### Target Audience

* Car enthusiasts looking to purchase high-quality alloy and track edition wheels.
* Motorsport fans seeking performance wheels for track use.
* Everyday drivers wanting stylish upgrades for their vehicles.
* Users who value a fast and secure online shopping experience.
* Mobile users who prefer browsing and purchasing wheels on-the-go.
* Customers looking for an intuitive filtering system (by brand, size, and style) to quickly find products.
* Admins and store managers needing a simple way to manage products and orders through the admin panel.

### First time user

* Clear and responsive navigation across all devices to explore categories and products.
* Visually engaging product cards with wheel images, names, and prices.
* Concise and informative product descriptions to support decision-making.
* Straightforward sign-up process with validation and feedback messages.
* Easy-to-use “Add to Cart” buttons on both product listings and detail pages.
* Prominent CTAs like “Shop Now” or “Add to Cart” to guide user flow.
  
### Registered User

* Secure login with clear feedback messages and access to their account.
* Ability to browse and filter products by category, brand, size, or style.
* Add, update, or remove products from their shopping cart.
* Access to their order history and view order details.
* Seamless checkout process with secure card payment options.
* Success messages and confirmation screens after placing an order.
* Ability to log out and easily log back in on future visits.

### Admin user

* Secure and dedicated login portal with role-based access control to protect sensitive admin operations.
* Full access to a centralized admin dashboard for managing products, categories, and orders.
* Ability to add, edit, or remove wheel listings, including names, descriptions, images, and prices.
* Management of categories (e.g., Alloy Wheels, Track Edition) with options to update or remove.
* Control over user accounts, including the ability to deactivate or delete accounts when required.
* Oversight of all orders, with options to view details, update statuses, or cancel when necessary.
* Ability to handle support issues and maintain data integrity through Django’s built-in admin features.


---

## Desing 

* The Fly Wheels e-commerce website features a sleek and performance-inspired aesthetic that reflects the precision and style of high-quality automotive wheels. A modern and responsive design ensures users across all devices have a seamless shopping experience.
* The homepage showcases featured products with clean product cards, images, and clear price displays. A streamlined navigation bar allows users to easily browse the Shop, access their Cart, or manage their Account. Product cards feature engaging wheel imagery, responsive hover effects, and intuitive Add to Cart buttons.
* The shopping cart and checkout forms are styled with Bootstrap, ensuring a consistent look and feel while maintaining clarity and ease of use. The design follows a light-on-dark theme for a modern retail feel, balancing usability with visual appeal.
* The footer is fixed at the bottom of the page, styled to complement the overall tone of the site, and includes navigation links, copyright information, and brand identity.



### Color Scheme
![Color Scheme]()
![Color Scheme]()

### Wireframe

<details>
<summary> Home Page
</summary>


![Home Page]()
</details>

<details>
<summary> Place an Order
</summary>
  
![My Orders Page]()
</details>

<details>
<summary> Order History  
</summary>

![Order History]()
</details>

<details>
<summary> Login Page
</summary>

![Delete Order]()
</details>

---

### Data Models

1. User Model
Utilizes Django’s built-in User model, extended with Django Allauth for user registration, authentication, and account management.
Each User can place multiple Orders, establishing a one-to-many relationship between User and Order.
2. Product Model
* Represents individual wheel products available in the shop.
* Fields include:
  * name
  * description
  * price
  * category (e.g., Alloy, Track Edition)
  * brand
  * size
  * image
  * Each product belongs to a single category but can appear in multiple filtered views.
3. Category Model
* Used to group wheels by type (e.g., Alloy Wheels, Track Edition).
* Fields include name and friendly_name for UI display.
* Each category can contain multiple Products, forming a one-to-many relationship.
4. Order Model
* Represents a completed purchase by a user.
* Fields include:
  * user (ForeignKey to User model)
  * order_number
  * full_name
  * email
  * address fields
  * date
  * order_total
  * Each order contains one or more items via the OrderLineItem model.
5. OrderLineItem Model
* Represents a product and quantity within a specific order.
* Fields include:
  * order (ForeignKey to Order)
  * product (ForeignKey to Product)
  * quantity
  * lineitem_total
  * Used to calculate the overall order total dynamically.


  
---
## Security Features

### User Authentication
* Implemented using Django Allauth, which handles user registration, login, logout, password reset, and account management securely.
### Login Decorator
* Views related to cart, checkout, and order history are protected using Django’s @login_required decorator.
* This ensures only authenticated users can perform sensitive actions such as placing an order or viewing order history.
### CSRF Protection
* Django provides built-in protection against Cross-Site Request Forgery (CSRF) attacks.
* CSRF tokens are embedded in all forms to ensure only legitimate requests are processed.
* When a user logs out, their session and CSRF token are invalidated automatically, reducing security risks.
### Form Validation
* All checkout and cart update forms use Django’s built-in form validation mechanisms.
* This includes required fields, input type enforcement, and feedback for invalid or missing data.
* Additional validation ensures that only valid products and quantities are submitted to the backend.
### Custom error pages
* Custom 404 (Page Not Found) and 500 (Internal Server Error) templates are implemented to improve user experience.
* These pages display friendly messages and provide navigation options back to the homepage or shop.

---
## Features

* Browse wheels by category, brand, and size.
* View detailed product pages with images, descriptions, and pricing.
* Add products to the shopping cart from category or product pages.
* Update quantities or remove items from the cart.
* Secure user authentication (sign up, log in, log out).
* Checkout system with order summary and confirmation.
* Admin interface to manage products, categories, and orders.
* Protected views to ensure only logged-in users can check out and view past orders.


### Existing Features

* Home Page
 * Serves as the landing page where users are introduced to the Fly Wheels brand and highlighted products.
   * Contents:
   * Hero header with promotional message and CTA
   * Featured Wheels section with popular products
   * Clear CTA buttons linking to the shop or specific categories
   * Mobile-friendly layout
    
![Home Page - Upper](path/to/homepage_upper.png)

![Home Page - Lower](path/to/homepage_lower.png)

* Navigation Bar
  * Present across all pages for seamless navigation.
  * Contents:
  * Links to: Home, Shop, Cart, Login, Signup
  * If logged in: Account menu with "Order History", "Logout"

![Navigation Bar](path/to/navbar.png)

* Products
  * Displays a selection of top products on the homepage.
  * Contents:
  * Product cards with image, name, price
  * “Add to Cart” button linking directly to cart functionality

![Featured Products](path/to/featured_products.png)

* Shop Page
  * Shows all available wheels, organized by category.
  * Contents:
  * Filtered views for Alloy Wheels and Track Edition
  * Product cards with image, name, and price
  * Buttons to view details or add to cart
   
![Shop Page](path/to/shop_page.png)

* Product Detail Page
  * Dedicated page for each wheel product.
  * Contents:
  * Larger product image
  * Full description and price
  * “Add to Cart” button
  * Optional technical details or size info
 
  
   ![Product Detail](path/to/product_detail.png)

  
* Cart Page
  * Allows users to view and manage products they intend to purchase.
  * Contents:
  * Product name, quantity selector, subtotal
  * Total price display
  * “Update” or “Remove” product buttons
  * Link to checkout

  ![Cart Page](path/to/cart.png)

  
* Checkout Page
  * Secure checkout form for completing orders.
  * Contents:
  * Address and contact details

![Checkout](path/to/checkout.png)

* Order summary
  * “Place Order” button
  * Success message after submission
    
![Order](path/to/checkout.png)

* Login Page
  * Lets returning users sign in securely.
  * Contents:
  * Email and password fields
  * Redirects to home or cart upon login

![Login](path/to/login.png)

* Sign Up Page
  * Allows new users to register an account.
  * Contents:
  * Username, email, password
  * Redirects and logs in the user upon registration

    
![Sign Up](path/to/signup.png)

* Order History (My Orders)
  * Lets users view their previous purchases.
  * Contents:
  * Table with product names, dates, total cost
  * View details of each order
    
![Order History](path/to/order_history.png)

* Confirmation Messages
  * Displays alerts after actions like order placement or cart update.
    
![Success Message](path/to/success_message.png)

![Cart Updated](path/to/cart_updated.png)

![Error Message](path/to/error_message.png)

* Footer
  * Fixed at the bottom of each page.
  * Contents:
  * Copyright
  * Branding and additional nav links

![Footer](path/to/footer.png)

---

## Future Enhancements

- Stripe integration for secure online payments
- Wishlist functionality so users can save products for later
- Customer testimonials or reviews for each wheel product
- Order confirmation emails with receipt and delivery info
- Stock level notifications (e.g., “Only 2 left!”)
- User profile page with editable account and shipping info
- Filter by price range in the Shop view
- Admin sales dashboard with order statistics and performance metrics


---

## 🛠️ Technologies Used

| Type            | Stack                            |
|-----------------|----------------------------------|
| Frontend        | HTML5, CSS3, Bootstrap 5         |
| Backend         | Python 3.12, Django 5.2          |
| Database        | PostgreSQL                       |
| Authentication  | Django built-in Auth             |
| Hosting         | Heroku                           |
| Version Control | Git, GitHub                      |

---
### Databases Used

* [ElephantSQL](https://www.elephantsql.com/) - Postgres database

### Frameworks & Libreries
* Django – A high-level Python web framework that encourages rapid development and clean, pragmatic design.
* Django Allauth – Integrated for comprehensive user authentication, registration, and account management.
* Bootstrap 5 – Utilized for responsive design and styling, ensuring a mobile-first and consistent user interface.
* Heroku – Platform-as-a-Service (PaaS) used for deploying and hosting the web application.

### Programs Used

* [Github](https://github.com/) - Storing the code online
* [Gitpod](https://www.gitpod.io/) - To write the code.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [Figma](https://www.figma.com/) - Used to create wireframes and schemes
* [Git](https://git-scm.com/) - Version control
* [Favicon Generator](https://realfavicongenerator.net/) - Used to create a favicon
* [JSHint](https://jshint.com/) - Used to validate JavaScript
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python
* [Colormind](http://colormind.io/) - Color Scheme
* [Brands Hatch](https://www.brandshatch.co.uk), [Silverstone](https://www.silverstone.co.uk) and [Lydden Hill](https://lyddenhill.co.uk) - Additional Images 

---
## Deployment and Local Developement

Live deployment can be found on this [View live website here]()

### Local Developement

#### How to Fork
1. Log in(or Sign Up) to Github
2. Go to repository for this project[Track Day]([https://github.com/TinaGrigorova/fly_wheels])
3. Click the fork button in the top right corner

#### How to Clone
1. Log in(or Sign Up) to Github
2. Go to repository for this project [Track Day]([https://github.com/TinaGrigorova/fly_wheels])
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above)
6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### ElephantSQL Database
[Track Day](https://github.com/TinaGrigorova/fly_wheels) is using [ElephantSQL](https://www.elephantsql.com/) PostgreSQL Database

1. Click Create New Instance to start a new database.
2. Provide a name (this is commonly the name of the project: tribe).
3. Select the Tiny Turtle (Free) plan.
4. You can leave the Tags blank.
5. Select the Region and Data Center closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### Heroku Deployment
* Log into [Heroku](https://www.heroku.com/) account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Prepare enviroment and settings.py
* In your GitPod workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1 - this is temporary, and can be removed for the final deployment
* DATABASE_URL - Insert your own ElephantSQL database URL here

#### Heroku needs two additional files to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is updated.
4. Click 'Open App' to view the deployed live site.

---

## 🧪 Testing

Testing was performed manually and via Django’s built-in testing tools.

- Form validation for date and time
- Duplicate booking prevention
- Login/logout/signup processes
- Mobile responsiveness
- Booking updates/cancellation

➡️ See full documentation: [`TESTING.md`](TESTING.md)


### Content

* All of the content is imaginary and written by the developer, me, Tina Grigorova.

### Acknowledgments

* I would like to thank my mentor for support and feedback throughout this project, Mitko Bachvarov.
* I would also like to extend my appreciation to the Slack community for their continuous engagement and willingness to share knowledge. The collaborative environment provided a platform for learning, troubleshooting, and gaining inspiration from fellow developers.
