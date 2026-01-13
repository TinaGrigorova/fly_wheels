# Fly Wheels | Testing

Return to [README](README.md)
- - -
Comprehensive testing has been performed to ensure the website's seamless and optimal functionality.
---
## Responsiveness Testing

The Fly Wheels website was meticulously tested across a variety of devices and screen sizes to ensure optimal responsiveness and user experience. Utilizing browser developer tools, such as Chrome DevTools, the site was evaluated in simulated environments representing smartphones, tablets, and desktops. This process allowed for real-time adjustments and ensured that the layout and functionality remained consistent across different viewports.​

<details>
<summary> Desktop PC
</summary>

![Desktop PC](/fly_wheels/media/images/testing_images/desktop.png)
</details>

<details>
<summary> Laptop
</summary>

![Laptop](/fly_wheels/media/images/testing_images/edge.png)
</details>

<details>
<summary> Tablet
</summary>

![Tablet](/fly_wheels/media/images/testing_images/tablet.png)
</details>

<details>
<summary> Mobile
</summary>

![Mobile](/fly_wheels/media/images/testing_images/phone.png)
</details>

## Browser Compatibility Testing

The Fly Wheels website was rigorously tested across multiple web browsers to ensure consistent functionality and appearance. This testing process guarantees a smooth and uniform user experience, regardless of the browser used.​

<details>
<summary> Chrome
</summary>

![Chrome](/fly_wheels/media/images/testing_images/chrome_testing.png)
</details>

<details>
<summary> Microsoft Edge
</summary>

![Chrome](/fly_wheels/media/images/testing_images/edge.png)
</details>

<details>
<summary> Safari
</summary>

![Safari](/fly_wheels/media/images/testing_images/safari.png)
</details>

<details>
<summary> Iphone Internet (Mobile)
</summary>

![Iphone Internet Mobile](/fly_wheels/media/images/testing_images/phone.png)
</details>
---
## Device Testing

Device testing was conducted on a variety of phone models, including Iphone 11, Oppo, iPhone 14, Huawei. The assistance of family members and friends was sought to perform the testing. This comprehensive approach ensured that the website was thoroughly evaluated on different devices and platforms, contributing to a more robust and user-friendly final product.

---
## Code Validation

### HTML Validation

<details>
<summary> Home Page
</summary>

![Home Page](/fly_wheels/media/images/testing_images/html_home_page.png)
</details>

<details>
<summary> Login Page
</summary>
  
![Login Page](/fly_wheels/media/images/testing_images/login_page.png)
</details>

<details>
<summary> Sign up Page
</summary>
  
![Login Page](/fly_wheels/media/images/testing_images/signup.png)
</details>

<details>
<summary> Cart Page
</summary>

![Make an order](/fly_wheels/media/images/testing_images/cart_page.png)
</details>

<details>
<summary> My Orderds
</summary>

![My Orders](/fly_wheels/media/images/testing_images/my_orders.png)
</details>

<details>
<summary> Category Page
</summary>
  
![Shop Page](/fly_wheels/media/images/testing_images/track_page.png)
</details>

<details>
<summary> Shop By Size
</summary>

![Shop by size Page](/fly_wheels/media/images/testing_images/size_page.png)
</details>

<details>
<summary> Shop By Brand
</summary>

![Brand Page](/fly_wheels/media/images/testing_images/brand_page.png)
</details>

<details>
<summary> Shop By Type
</summary>

![Type Page](/fly_wheels/media/images/testing_images/track_page.png)
</details>

<details>
<summary>   Weight Page
</summary>

![Weight Page](/fly_wheels/media/images/testing_images/weight_page.png)
</details>


### CSS Validation

<details>
<summary> Custom CSS (style.css)
</summary>

![Custom CSS (style.css)](/fly_wheels/media/images/testing_images/css.png)
</details>

### Python

#### Fly_wheels app

<details>
<summary> urls.py
</summary>

![admin.py](/fly_wheels/media/images/testing_images/fly_wheels_urls.png)
</details>


#### Accounts app

<details>
<summary> views.py
</summary>

![views.py](/fly_wheels/media/images/testing_images/accounts_views.png)
</details>


#### Products app

<details>
<summary> admin.py
</summary>

![admin.py](/fly_wheels/media/images/testing_images/products_admin.png)
</details>


<details>
<summary> models.py
</summary>

![models.py](/fly_wheels/media/images/testing_images/products_models.png)
</details>

<details>
<summary> urls.py
</summary>

![urls.py](/fly_wheels/media/images/testing_images/products_urls.png)
</details>

#### Store app

<details>
<summary> cart.py
</summary>

![views.py](/fly_wheels/media/images/testing_images/store_cart.png)
</details>

<details>
<summary> views.py
</summary>

![tests.py](/fly_wheels/media/images/testing_images/store_views.png)
</details>

## Lighthouse Report

<details>
<summary> Home Page
</summary>

![Home Page](/fly_wheels/media/images/testing_images/lighthouse_home.png)
</details>


<details>
<summary> Sign Up Page
</summary>

![Sign Up Page](/fly_wheels/media/images/testing_images/lighthouse_signup.png)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](/fly_wheels/media/images/testing_images/lighthouse_login.png)
</details>


<details>
<summary>  Shop Page
</summary>

![Browse Tracks](/fly_wheels/media/images/testing_images/lighthouse_shop.png)
</details>

<details>
<summary> Category Page
</summary>
  
![Edit Booking Page](/fly_wheels/media/images/testing_images/loghthouse_category.png)
</details>

<details>
<summary> Brand Page
</summary>

![Delete Booking Page](/fly_wheels/media/images/testing_images/lighthouse_brand.png)
</details>

<details>
<summary> Size Page
</summary>

![Delete Booking Page](/fly_wheels/media/images/testing_images/lighthouse_size.png)
</details>

<details>
<summary> Weight Page
</summary>

![Delete Booking Page](/fly_wheels/media/images/testing_images/lighthouse.png)
</details>

## Bugs 

### Present Bugs

- **Real email delivery fails (production SMTP)**
  - **Status:** Open (known limitation)
  - **Observed:** Order/notification emails are not delivered when using real SMTP providers in production. Works perfectly with Mailtrap (testing).
  - **Repro:** Place an order with production SMTP configured; logs show SMTP/auth errors or timeouts; no email received.
  - **Attempted:** Gmail (with app password), Mailchimp Transactional, and other SMTP providers; correct TLS/port (587), environment variables on Heroku, different from-addresses. Unfortunately, the fix is currently beyond my scope.
  - **Likely cause:** Provider restrictions and/or missing domain DNS records (SPF/DKIM/DMARC) that require verified domain ownership and DNS changes.
  - **Mitigation:** Email sending is wrapped in `try/except` so orders still complete; the UI shows a non-blocking warning toast if email fails. Mailtrap remains enabled for reliable test sends.


### Resolved Bugs

| Bug                                                                                    | Fix                                                                                                                                             |
| :------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| Heroku boot error: `ModuleNotFoundError: No module named 'fly_wheels.wsgi'`            | Corrected **Procfile** to `web: gunicorn fly_wheels.wsgi:application` and confirmed project root structure. Restarted dynos.                    |
| DisallowedHost after deploy                                                            | Added the Heroku domain to **ALLOWED\_HOSTS** and **CSRF\_TRUSTED\_ORIGINS** in `settings.py`.                                                  |
| Home “hero” image missing locally & on Heroku                                          | Moved image to `store/static/store/images/bg-collage.png`, referenced it via `/static/...` in CSS, ran `collectstatic`, and enabled WhiteNoise. |
| Layout shift when showing success messages (hero dropped until refresh)                | Switched Django messages to **Bootstrap toasts** positioned `position-fixed top-0 end-0`; removed inline alerts that pushed the page content.   |
| Heroku build failed: `mailchimp-marketing==3.0.xx` incompatible with Python 3.12       | Removed the package and replaced it with plain **SMTP email** + a simple in-app **Newsletter** model.                                           |
| Build warning: `.venv` committed                                                       | Deleted the `.venv/` folder from the repo, added it to `.gitignore`, rebuilt.                                                                   |
| SMTPAuthenticationError on checkout email                                              | Standardised **EMAIL\_**\* settings to read from environment variables; set Mailtrap creds in Heroku Config Vars; verified TLS/port.            |
| `relation "store_newsletter" does not exist` after subscribing                         | Created `Newsletter` model, ran `makemigrations` & `migrate`; added CSRF and proper POST route.                                                 |
| `NoReverseMatch: 'newsletter-subscribe'`                                               | Added URL pattern `path('newsletter/subscribe/', ...)` and updated footer form `action`.                                                        |
| ImportError in sitemap after removing `Category` model                                 | Removed `CategorySitemap` and the `Category` import, kept `ProductSitemap` + static sitemap only.                                               |
| `TemplateSyntaxError` “block tag with name 'meta\_description' appears more than once” | Consolidated/renamed meta blocks in `base.html` (separate `meta_description` and `og_description`), leaving each block defined once.            |
| Sign-up template used Allauth routes (`account_signup`, `account_login`)               | Replaced with Django auth routes (`signup`, `login`) and updated form `action`/links.                                                           |
| CSRF 403 when posting forms                                                            | Audited templates to ensure `{% csrf_token %}` is present for all POST forms (login, newsletter, contact).                                      |
| Unwanted debug link printed above hero collage                                         | Removed stray debug anchor from the template and moved canonical URL to a `<link rel="canonical">` in `<head>`.                                 |
| Git push rejected (remote ahead)                                                       | Resolved via `git pull --rebase origin main`, then `git push`.                                                                                  |

## Features Testing

| Page            | User Action                         | Expected Result                                      | Status |
|-----------------|-------------------------------------|-----------------------------------------------------|--------|
| Home Page       | Click logo                          | Redirect to Home page                               | ✅ PASS |
|                 | Click Shop                          | Redirect to Shop page                               | ✅ PASS |
|                 | Click Login / Sign Up               | Redirect to auth pages                              | ✅ PASS |
| Shop Page       | View products                       | Products display with images and prices             | ✅ PASS |
|                 | Filter by brand/size/weight         | Filtered products shown correctly                  | ✅ PASS |
| Cart            | Add product to cart                 | Product added, confirmation message shown           | ✅ PASS |
|                 | Update quantity                     | Cart total updates correctly                        | ✅ PASS |
|                 | Remove product                      | Product removed from cart                           | ✅ PASS |
| Checkout        | Access checkout (logged in)         | Redirect to Stripe checkout                         | ✅ PASS |
|                 | Complete payment                    | Redirect to order success page                      | ✅ PASS |
| My Orders       | View order history                  | User sees only their own orders                     | ✅ PASS |
| Admin           | Manage products and orders          | CRUD operations available                           | ✅ PASS |
| Error Pages     | Enter invalid URL                   | Custom 404 page displayed                           | ✅ PASS |


| **Error Pages**     | Type invalid URL                                 | Custom 404 page appears                                      | ✅ PASS |

---
## Manual Testing
 * Core Features Tested — Fly Wheels (Django e-commerce)
1) User Registration & Login
  * Created a new account via /accounts/signup/ with valid username & password → user auto-logged in, toast shown.
  * Logged in via /accounts/login/ with valid credentials → success, redirect respected ?next=.
  * Invalid login (wrong password) → form errors rendered; CSRF token present; no redirect loop.
  * Logout POST → user session cleared; navbar swapped to Login/Sign Up.
2) Product Browsing & Filtering
  * Home and Shop pages load with product cards (image, name, price + “per item/pack” label).
  * Category routes: Alloy (/shop/alloy/) and Track Edition (/shop/track/) show correct subsets.
  * Filters:
  * Brand (/shop/brand/<brand>/) – BBS/OZ Racing/Enkei/Fox show expected products.
  * Size (/shop/size/17%22…20%22/) – correct size subsets.
  * Weight (/shop/weight/7-10…13-17/) – correct weight subsets.
  * Product details show: price, optional compare-at price, pack size label, long description, delivery estimate.
3) Cart — Add/Update/Remove
  * “Add to Cart” from listing & detail → non-blocking toast confirmation; cart badge updates.
  * Cart page shows each line: image, title, unit price + “per item/pack”, qty control, line subtotal, remove button.
  * Quantity update (± and direct input) → totals recalc immediately on submit; invalid values rejected safely.
  * Remove item → item row disappears, totals update; empty cart state handled.
4) Checkout (Stripe session)
  * “Checkout” launches create-checkout-session; redirects to Stripe.
  * Success flow returns to /shop/checkout/success/:
  * Order recorded (Order + CartItems), totals correct.
  * Success page shows order summary.
  * Email confirmation attempted; on SMTP failure, safe warning toast shown (order still succeeds).
  * Cancel flow returns to cart without creating an order.
5) Order History
  * /shop/my-orders/ requires auth → unauthenticated users redirected to login.
  * Authenticated users see a list of their orders only (date, item count, total).
  * Links to order detail (if present) show the correct items and totals.
6) Contact Form
  * /shop/contact/ accepts name, email, message.
  * Valid submission → success toast; record saved to DB (Contact model).
  * Invalid submission (missing fields) → field errors shown; no DB write.
  * (If SMTP configured) message email sent; failures don’t break request.
7) SEO & Static Assets
  * robots.txt served as text/plain with sitemap link.
  * sitemap.xml renders and includes product + static routes.
  * <head> contains descriptive meta tags, canonical URL, Open Graph tags.
  * Favicon served in production (verified after collectstatic).
  * WhiteNoise serves static files with hashed filenames; DEBUG=False works.
8) Security & CSRF
  * All POST forms include {% csrf_token %} (login, signup, cart actions, contact, newsletter if enabled).
  * Auth-only routes (order history, checkout success tied to session) aren’t accessible to anonymous users.
  * ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS include the Heroku domain.
  * Cookies use Secure + SameSite=Lax in production.
9) Responsiveness & UX
  * Navbar collapses on mobile; menus and dropdowns usable by touch.
  * Toast notifications appear position-fixed top-right and auto-hide; no layout shift.
  * Product grid reflows at typical breakpoints; buttons remain reachable.
10) Deployment Checks (Heroku)
  * Procfile: web: gunicorn fly_wheels.wsgi:application.
  * .python-version set; requirements.txt compatible (no platform-specific wheels).
  * SECRET_KEY, SMTP, Stripe keys set via Heroku Config Vars (no secrets in repo).
  * python manage.py collectstatic --noinput succeeds; app boots without DISABLE_COLLECTSTATIC.

  
### Return to [README](README.md)

---

Tested across latest Chrome, Firefox, and Safari browsers. Responsive tests done with dev tools and real devices.
