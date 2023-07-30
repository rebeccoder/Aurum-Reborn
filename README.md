# Aurum Reborn

Welcome to Aurum Reborn - An Elegant Jewelry Website!

Aurum Reborn is an elegant online jewelry store, showcasing ethically sourced gold jewelry. This website serves as my portfolio project, demonstrating my skills and passion for web development and design.

Enjoy exploring our curated collection of exquisite jewelry pieces that reflect timeless beauty and ethical values. The website offers a seamless and user-friendly experience, whether you're on a desktop or a mobile device.

Thank you for visiting Aurum Reborn. Feel free to reach out with any feedback or inquiries.

1. [UX](#ux)
    - [Goals](#goals)
        - [Project Goals](#project-goals)
        - [Visitor Goals](#visitor-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#exisiting-features)

    - [Future Goals](#future-goals)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Storage](#data-storage)

4. [Technology Used](#technology-used)

5. [Testing](#testing)

6. [Deployment](#deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Disclaimer](#disclaimer)

# UX

## Goals


### Project Goals
- Develop a responsive and visually appealing e-commerce website for Aurum Reborn Jewelry that showcases their exquisite collection of ethical gold jewellery.
- Implement a user-friendly and secure authentication system that allows customers to create accounts, log in, and view their previous orders, making it convenient for them to track their purchase history.
-  a seamless and intuitive shopping experience with easy navigation, sorting options, and a shopping bag functionality that enables customers to add and manage items before proceeding to checkout.
- Incorporate a dynamic product management system for the admin, allowing them to add, edit, and remove jewellery products from the website easily and efficiently.
- Integrate a secure payment gateway, Stripe, to facilitate smooth and secure online transactions for customers, instilling trust in the website's payment process.
- Implement a robust search functionality, enabling users to quickly find specific jewelry items based on various criteria like category, price range, and keywords.
- Provide a platform for customers to write testimonials about their purchase experiences.
- Create a mobile-responsive design to cater to customers accessing the website from various devices, ensuring a consistent and enjoyable experience across different screen sizes.
- Enable users to register for an account on the website, providing a streamlined registration process that includes email verification for enhanced security and communication.
- Implement a creator showcase section where the admin can add and display information about talented jewelry designers and artisans, fostering a sense of community and appreciation for their craft.
- Offer users the option to subscribe to the Aurum Reborn newsletter, providing valuable updates on new product launches, exclusive offers, and industry trends to keep customers engaged and informed.


### Visitor Goals

- Discover Exquisite Jewellery: Visitors aim to explore the curated collections of stunning and elegant jewellery pieces crafted from ethically sourced gold.
- Find Ethical Jewellery Options: Visitors are seeking jewellerey that aligns with their values and supports ethical sourcing and sustainability.
- Easily Navigate the Website: Visitors intend to effortlessly navigate through the website to find the information they need, from product details to policies.
- Stay Updated with New Arrivals: Visitors aim to stay informed about the latest additions to the jewellery collections, ensuring they don't miss out on new and exciting pieces.
- Follow on Social Media: Visitors may seek to connect with the brand through social media to stay updated on promotions, events, and behind-the-scenes insights.
- Read Testimonials: Visitors wish to read testimonials and reviews from other customers to gain trust and confidence in their potential purchase.
- Create an Account and View Previous Orders: Visitors aim to register an account on the website to have a personalized shopping experience and easily access their order history.
- Write, Edit, and Delete Testimonials: Visitors want the ability to share their experiences with the jewellery and the brand by writing testimonials. They also desire the option to edit or delete their testimonials if they wish to update their feedback or remove it later.


### User Stories

#### Customers 

- As a new visitor, I want to easily navigate through different jewelry categories, so I can quickly find the type of jewelry I am interested in.
- As a potential customer, I want to view detailed product images and descriptions, so I can make informed decisions about which jewelry piece to purchase.
- As a fashion enthusiast, I want to filter products by price and style, so I can explore jewelry options that fit my budget and match my preferences.
- As a returning customer, I want to log in to my account and view my previous orders, so I can refer to my purchase history.
- As a socially responsible consumer, I want to learn about the brand's commitment to ethical sourcing and sustainability, so I can feel confident about my jewellery choices.
- As a satisfied customer, I want to share my positive experience by writing a testimonial, so others can learn about the quality and service provided by the website.
- As a busy professional, I want a straightforward and secure checkout process, so I can complete my purchase quickly and without any hassle.
- As a mobile user, I want the website to be responsive and mobile-friendly, so I can browse and shop for jewelry conveniently from my smartphone or tablet.

#### Admin

- As an admin user i want to be able to add, edit and delete products easily.
- As an admin user i want to be able to manage orders in a simple and easy manner.
- As an admin user i want to be able to add, edit and delete users easily.

### Design Choices 

The design choices for Aurum Reborn's website were inspired by a wide range research of other high-end jewellery websites. I sought to create a minimalistic and elegant platform, exuding a touch of luxury and femininity. The choice of a refined gold and rosey color palette adds a sense of opulence, while maintaining a balanced and sophisticated look throughout the site. By observing successful design elements from the industry and infusing my own artistic touch, the websites aim to offer visitors an immersive and captivating experience that beautifully showcases the collection of exquisite jewellery pieces.


#### Colours
![Colour Pallet](media/readme/colour-pallet.png)

#FFFFF0 was the chosen background colour as well as header and footer colour for the website.

#8B5A2B and #D4AF37 were the two main colours used for any titles or paragraphs

#CDA3A3 was used for the delivery banner and as a accent colour for buttons and hovering

#699C6B was also used as an accent colour for buttons and hovering

#### Fonts
- Playfair (Serif): Used for various headings and logo fonts. It provides an elegant and traditional look.
- Raleway (Sans-serif): Used for some descriptive text. Raleway is a clean and modern sans-serif font.
- Josefin Sans (Sans-serif): Used for the main buttons. Josefin Sans is a geometric sans-serif font with a friendly appearance.
- Cormorant Garamond (Serif): Used for the home title. It is a stylish and versatile serif font with a touch of modernity.

#### Layout and Imagery

The website follows a responsive layout, ensuring a seamless user experience across various devices and screen sizes.
To maintain a sense of femininity and glamour, carefully curated images of exquisite jewellery pieces and feminine, beautiful women are showcased with hover effects to enhance user engagement.
The minimalist design approach ensures that the focus remains on the products, allowing users to explore the jewellery collection effortlessly.

#### Inspiration

The design choices for Aurum Reborn were influenced by extensive research and analysis of other high-end jewellery websites. By observing successful design elements in the industry, the website's aesthetics were refined to align with contemporary standards.

#### Wireframes

<details>
  <summary>Home Page</summary>

  ![Home Page Wireframe](media/wireframes/home-wireframe.png)
</details>
<details>
  <summary>Products Page</summary>

  ![Products Page Wireframe](media/wireframes/productspage-wireframe.png)
</details>
<details>
  <summary>Product Detail</summary>

  ![Product Detail Wireframe](media/wireframes/productdetail-wireframe.png)
</details>
<details>
  <summary>Checkout</summary>

  ![Checkout Wireframe](media/wireframes/checkout-wireframe.png)
</details>
<details>
  <summary>Shopping Bag</summary>

  ![Shopping Bag Wireframe](media/wireframes/shoppingbag-wireframe.png)
</details>


### Features

#### Existing Features

<details>
  <summary>The stunning homepage for Aurum Reborn has an allure of conscious luxury. Where users can discover the shops collections, meet the talented creators, read the testimonials, and subscribe to the newsletter for the latest updates. This beautiful design reflects the brands commitment to timeless elegance and ethical values.
   </summary>

  ![Homepage](media/readme/homepage.jpg)
</details>

<details>
  <summary>The navigation bar is a pivotal element of the Aurum Reborn website, providing users with a seamless and intuitive way to explore the various sections of the platform. Designed with user-friendliness in mind, the navigation bar offers easy access to essential pages and functionalities, enhancing the overall browsing experience.
  The design for the navigation bar is super minimalistic yet effective. The links links have hover effects with our signiture acent tones as well as drop down menus. It's the right balance of functional and beautiful. The banner above also has a closing action available.
   </summary>

  ![Navigaion Bar](media/readme/navigation-bar.jpg)
</details>

<details>
  <summary> The Footer is designed to be elegant and minimalist, ensuring a seamless user experience while providing essential information and links. It features prominent links to the company's social media platforms, allowing visitors to connect and stay updated with our latest designs and promotions. Additionally, the Footer includes quick access to important pages, such as the Careers page for potential job opportunities, and links to our comprehensive Terms and Conditions and Return Policy to foster transparency and trust with our customers. Notably, the Footer also showcases a logo that symbolizes the company's commitment to environmental consciousness, underlining our dedication to sustainable practices in crafting exquisite jewellery pieces. </summary>
  
  ![Footer](media/readme/footer.jpg)
</details>

<details>
  <summary>Browse a range of stunning jewellery collections distributed into navigatable cateogires including necklaces, earrings, bracelets, and rings or just view all the products together. There is also the option to sort the products by price and by name</summary>

  ![Product Categories](media/readme/product-categories.jpg)
</details>

<details>
  <summary>The Creators Page celebrates talented artisans and jewellery designers. Through this feature, customers can explore a diverse array of creators, each with their unique styles and craftsmanship. The page showcases the creators' names, where they're from, and a brief description, giving customers a valuable sense of community.
  For administrators, the Creators Page offers tools for managing the content. They can easily add new creators to the platform, allowing the website to continuously feature fresh talents. Moreover, admin has the ability to edit existing creator profiles, ensuring that all information remains up-to-date and accurate. Should the need arise, administrators can also remove creators from the page, maintaining a curated and relevant selection
  .</summary>

  ![Creators Page](media/readme/creators-page.jpg)
</details>

<details>
  <summary>The Testimonials page is a dedicated space where customers can share their experiences and satisfaction with our jewellery collection. It prominently displays a curated selection of short and positive testimonies from our happy customers. Users have the ability to rate their experience on a scale of 1 to 5 stars and even edit or delete their testimonials if they wish to update their feedback over time. Furthermore, the page also features an intuitive "Add Testimony" button that allows customers to contribute their own reviews and let others know about their delightful shopping experience with us.</summary>

  ![Testimonials](media/readme/testimonials-page.jpg)
</details>

<details>
  <summary>The Profile Page is a personalized hub for customers, offering a seamless and engaging experience. Users can access a pre-filled form displaying their details, including name, contact information, and shipping address, making it easy to review and edit their personal information as needed. Moreover, the Profile Page also presents users with their order history, showcasing a comprehensive list of their previous purchases, ensuring they can conveniently track their past transactions and reorder favorite pieces. This feature empowers customers with full control over their account and enables them to maintain up-to-date details, enhancing their overall shopping journey.</summary>

  ![Profile Page](media/readme/profile-page.jpg)
</details>

<details>
  <summary>The Shopping Bag feature is a vital component for our customers during their shopping experience. When adding products to their bag, users can easily review a visually appealing display of the items they've selected, complete with product images and essential information, such as product names, prices, and quantities. This convenient setup allows users to effortlessly adjust the quantity of each item or remove products they no longer wish to purchase. With options to proceed to a secure checkout for a seamless transaction or continue shopping to explore more products, the Shopping Bag feature ensures a smooth and enjoyable journey for every shopper, making the jewelry purchasing process a breeze. </summary>

  ![Shopping Bag](media/readme/shopping-bag.jpg)
</details>

<details>
  <summary>The Checkout App is the final stop on Aurum Reborn's user-friendly shopping journey. Seamlessly integrating with the website, the Checkout App streamlines the purchasing process with an intuitive and pre-filled checkout form for existing users. New users can easily provide their details for a swift and hassle-free checkout. As customers review their order summary, the Checkout App automatically applies any shipping cost reductions or discounts, ensuring transparency and accuracy in the final purchase amount. To guarantee secure and efficient transactions, the app leverages Stripe Payments, allowing customers to confidently complete their purchases. Once payment is processed successfully, customers are directed to a Success Page, assuring them that their order has been confirmed.</summary>
  
  ![Testimonials](media/readme/checkout.jpg)
</details>


