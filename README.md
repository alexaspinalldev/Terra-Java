# Terra Java

## Overview
Terra Java is a boutique catalogue of all the world's finest coffee blends. Taking its name from the rich coffee fields found on the island of Java in western Indonesia, it aims to showcase the very best coffees from around the globe.

Vendors are able to register themselves on the site and upload, edit and delete their coffees.
Visitors can filter the coffees by attibutes - region, bitterness, bean (Arabica, Robusta, Liberica, and Excelsa)


## UX Design Process

### Graphic design and visual assets:
[Selected colour pallate](https://coolors.co/4f3221-34623f-ffee7d-c1b098-ffffff)

Logo:<br>
<img src="static/images/tj-logo.png" style="border: 1px solid white; padding: 10px; width: 50%"></img>

Image credits:<br>
[Ashlyn Ciara](https://unsplash.com/@ashlynciara?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-man-in-a-hat-picking-berries-from-a-bush-4rbWwrtMQ1c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

[wojtal78](https://www.istockphoto.com/portfolio/wojtal78?mediatype=photography) on [iStockPhoto](https://www.istockphoto.com/photo/coffee-bag-gm509212479-45793256?searchscope=image%2Cfilm)

[PROJETO CAFÉ GATO-MOURISCO](https://unsplash.com/@projetocafegatomourisco?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-lush-green-hillside-covered-in-lots-of-trees-zOVRgigQMQA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

[Nitin Khajotia on Pexels](https://www.pexels.com/video/a-view-of-a-lush-green-valley-with-mountains-in-the-background-19669269/)

### User flow and ERD
  - [Link to Miro](https://miro.com/app/board/uXjVLuC7tmQ=/?share_link_id=877125417995)

### User stories and Project board
  - [Terra Java project board](https://github.com/users/alexaspinalldev/projects/10)

### Wireframes:
<img src="static/images/README/Landing.png" style="width: 33%"></img>
<img src="static/images/README/Catalogue.png" style="width: 33%"></img>
<img src="static/images/README/CoffeeDetail.png" style="width: 33%"></img>
    
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
  - **Site Ideation:**
    - The name of the site was picked from a list of keyword provided by ChatGPT. DALLE was used to create the logo.
    - AI was also used to expand the user stories from the initial prompt describing the site's functions.
       
  - **Content:** 
    - Once the ERD was complete, GPT was used to create a JSON import scripts for the lists of Vendors and Coffees.

  - **Code Creation:** 
    - GPT was used to cross-examine my proposed ERD, suggesting new fields, and then create the model objects.

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
