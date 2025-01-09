# Terra Java

## Overview
Terra Java is a unique catalogue of all the world's finest coffee blends. Taking itss name from the rich coffee fields found on the island of Java in western Indonesia, it aims to showcase the very best coffees from around the globe.

Vendors are able to register themselves on the site and upload, edit and delete their coffees.
Visitors can filter the coffees by attibutes - region, bitterness, bean (Arabica, Robusta, Liberica, and Excelsa)


## UX Design Process

### Graphic design and visual assets:
[Colour pallate:](https://coolors.co/432818-34623f-ffee7d-c1b098-ffffff)

<img>LOGO IMAGE HERE</img>

The default coffee image is by <a href="https://unsplash.com/@wojtekpaczes?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Wojciech Pacześ</a> on <a href="https://unsplash.com/photos/a-pile-of-coffee-beans-sitting-next-to-each-other-lFJzbKZZ_NU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

The landing page image is by <a href="https://unsplash.com/@projetocafegatomourisco?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">PROJETO CAFÉ GATO-MOURISCO</a> on <a href="https://unsplash.com/photos/a-lush-green-hillside-covered-in-lots-of-trees-zOVRgigQMQA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

### User flow
  - [User flow and ERD document](https://miro.com/app/board/uXjVLwAu9aQ=/)

### User stories and Project board
  - [Add a link to the GitHub Projects kanban board.]

 <table border="1">
  <thead>
    <tr>
      <th>Title</th>
      <th>User Story</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Landing Page</td>
      <td>As a visitor, I want to see a landing page when I open the site so that I know what the site is about and can navigate to its features.</td>
    </tr>
    <tr>
      <td>Catalogue Button</td>
      <td>As a visitor, I want to see a button on the landing page that takes me to the catalogue so that I can browse the available coffees.</td>
    </tr>
    <tr>
      <td>Coffee Grid</td>
      <td>As a visitor, I want to see a list of coffees displayed in a paginated grid format so that I can browse the available products easily.</td>
    </tr>
    <tr>
      <td>Filter Coffees</td>
      <td>As a visitor, I want to filter the displayed coffees by product attributes (e.g., roast level, origin, price) so that I can find coffees that match my preferences.</td>
    </tr>
    <tr>
      <td>Coffee Details</td>
      <td>As a visitor, I want to click on a coffee product and see a detailed product page so that I can learn more about the coffee, including descriptions and attributes.</td>
    </tr>
    <tr>
      <td>Vendor Registration</td>
      <td>As a vendor, I want to register for an account from the site’s front-end so that I can manage my products.</td>
    </tr>
    <tr>
      <td>Vendor Login</td>
      <td>As a vendor, I want to log in to my account so that I can access my vendor dashboard.</td>
    </tr>
    <tr>
      <td>Adding Products</td>
      <td>As a vendor, I want to add new products to the catalogue so that customers can see and purchase my products.</td>
    </tr>
    <tr>
      <td>Editing Products</td>
      <td>As a vendor, I want to edit the details of my existing products so that I can keep product information up to date.</td>
    </tr>
    <tr>
      <td>Removing Products</td>
      <td>As a vendor, I want to remove products I no longer offer so that only current products are displayed in the catalogue.</td>
    </tr>
    <tr>
      <td>Manage Vendor Accounts</td>
      <td>As an admin (optional), I want to manage vendor accounts so that I can maintain the integrity of the marketplace.</td>
    </tr>
    <tr>
      <td>Moderate Product Listings</td>
      <td>As an admin (optional), I want to moderate product listings so that inappropriate or incorrect products can be removed.</td>
    </tr>
    <tr>
      <td>Site Analytics</td>
      <td>As an admin (optional), I want to view site analytics so that I can monitor site performance and user engagement.</td>
    </tr>
  </tbody>
</table>


- **Wireframes:**
  - [Attach or link to accessible wireframes used in the design process, ensuring high colour contrast and alt text for visual elements.]
  - [Explain the rationale behind the layout and design choices, focusing on usability and accessibility for all users, including those using assistive technologies.]
    
- **Design Rationale:**
  - [Explain key design decisions, such as layout, colour scheme, typography, and how accessibility guidelines (e.g., WCAG) were integrated.]
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]
 
- **Reasoning For Any Final Changes:**
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]

## Key Features
- **Feature 1:** [Briefly describe the implemented feature.]
- **Feature 2:** [Briefly describe the implemented feature.]
- **Inclusivity Notes:** 
  - [Mention how the features address the needs of diverse users, including those with SEND.]

## Deployment
- **Platform:** Heroku
- **High-Level Deployment Steps:** 
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
- **Verification and Validation:**
  - Steps taken to verify the deployed version matches the development version in functionality.
  - [Include any additional checks to ensure accessibility of the deployed application.]
- **Security Measures:**
  - Use of environment variables for sensitive data.
  - Ensured DEBUG mode is disabled in production.

## AI Implementation and Orchestration

### Use Cases and Reflections:
(Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.)

  - **Site Ideation:**
    - The name of the site was picked from a list of keyword provided by ChatGPT. DALLE was used to create the logo.
    - AI was also used to expand the user stories from the initial prompt describing the site's function.
       
  - **Content:** 
    - Once the ERD was complete, GPT was used to create a JSON file of content for the database. 

  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing:**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing:**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]

## Future Enhancements
- Users can register and leave reviews on coffee roasts where they comment and rate the coffee on different metrics.
- Add a webstore component to the site.
