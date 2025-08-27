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

