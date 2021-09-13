# Noffle My Needs

![GitHub contributors](https://img.shields.io/github/contributors/abibubble/noffle-my-needs)
![GitHub last commit](https://img.shields.io/github/last-commit/abibubble/noffle-my-needs)
![GitHub language count](https://img.shields.io/github/languages/count/abibubble/noffle-my-needs)
![GitHub top language](https://img.shields.io/github/languages/top/abibubble/noffle-my-needs)
![Font Awesome version](https://img.shields.io/badge/Font%20Awesome-v5.15.1-blue)
![GitHub forks](https://img.shields.io/github/forks/abibubble/noffle-my-needs?style=social)

[Here is a link to the final project](https://noffle-my-needs.herokuapp.com/)

This project was built for the [Trust In SODA](https://www.trustinsoda.com/) and [Code Institute](https://codeinstitute.net/) Hackathon in September 2021, by the team A11y Allies. The theme is 'Building An Accessible Workplace', and we were tasked with creating a tool that helps employers create a truly accessible workspace, or improve their recruitment and onboarding experience for every person. It is designed to be responsive on a wide range of devices, whilst also being easy to navigate through, and fully accessible.

![Final project image home page](static/docs/img/finalsite.png)

## Contents

* [Definition](#definition)

* [User Experience (UX)](#user-experience-(ux))
  * [Initial Discussion](#initial-discussion)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [User Journey](#user-journey)
  * [Features](#features)
  * [Audio](#audio)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

* [Deployment](#deployment)
  * [Initial Deployment](#initial-deployment)
  * [How to Fork it](#how-to-fork-it)
  * [How to Clone it](#how-to-clone-it)
  * [Making a Local Clone](#making-a-local-clone)

* [Testing](#testing)
  * [W3C Validator](#w3c-validator)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
  * [Further Testing](#further-testing)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)
  * [Lighthouse](#lighthouse)
    * [Performance](#performance)
    * [Accessibility](#accessibility)
    * [Best Practices](#best-practices)
    * [SEO](#seo)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

---

## Definition

**Noffle**  
_noun_  
A state of need of a particular person  
Usage: "I've set a 'Please Speak Up' Noffle on my work system so that everyone knows I may be hard of hearing."  
Similar: State, Need, Setting, Status

---

## User Experience (UX)

### Initial Discussion

* The theme for this Hackathon is 'Building An Accessible Workplace', and we were tasked with creating a tool that helps employers create a truly accessible workspace, or improve their recruitment and onboarding experience for every person.
* We chose to work on the former, ensuring that all employees can feel that their needs are met every day while they're at work.
* This site should be fully inclusive for all employees, not just those with visible disabilities, but also including those with mental health disabilities, as well as all neurotypical and able-bodied employees.

### User Stories

#### First Time Visitor Goals

As a first time visitor to this site, a user should be able to :

* Easily navigate the site.
* Intuitively and easily understand what to do.
* Register for an account.
* Set my Noffles.
* Get visual feedback when an action on the site is completed.

#### Returning Visitor Goals

In addition to the First Time Visitor Goals, a Returning Visitor should be able to :

* Log in.
* Update their state.
* See the public states of other users.
* Be confident that their password is be stored securely.
* Navigate intuitively, with no need to use the browser's back button.

#### Admin Goals

In addition to the First Time and Returning Visitor Goals, as an administrator of this site, an admin user should be able to:

* Be confident that a user can't to brute force their way into the restricted pages.
* Edit or delete any user.
* Add a new state.
* Edit or delete any state.
* Give or remove admin rights.

[Back to Top](#noffle-my-needs)

---

## Design

### Overall

* We wanted to make this a fun way to start your workday. So when you first log in, we wanted to ensure that the user was met with a welcome relating to the time of day.
* We also decided to call the individual need states 'Noffles' for the same reason. We can't say it without a little giggle, and we wanted it to brighten everyone's day, leading to a happier and more inclusive workspace overall.
* This led into the name of this project, 'Noffle My Needs'. It provides a small description of what this site is targeting - the needs of each employee in the business, whilst also giving them that little smile or giggle from the word 'Noffle'.

### Color Scheme

* We have used a pastel color scheme for the site, so as to be fully WCAG AAA compliant with color contrasts throughout the site.
* We created CSS variables and our own custom button classes to ensure our site stayed within the color scheme.
* All text is black, or dark brown, to ensure that users don't have difficulty with color contrasts.
* We checked all color contrasts with [WebAIM's Contrast Checker](https://webaim.org/resources/contrastchecker/).
* We checked this site on [Toptal Color Blind Filter](https://www.toptal.com/designers/colorfilter/) to ensure that color blind users wouldn't have difficulty.
* The colors we used are as follows:
  * alto - #D0D0D0
  * gallery - #ECECEC
  * wild-sand - #F5F5F5
  * pastel-yellow - #FEF3D2
  * pastel-red - #FBE6E6
  * pastel-green - #E3F1D4
  * pastel-blue - #D7EFF5

![Colors used in this site](static/docs/img/colors.png)

### Typography

* After a lengthy discussion, we decided to stick with the HTML standard fonts.
* This is because they're sans-serif fonts, which are easy to read for dyslexic and visually impaired users.
* As the standard HTML font size is 16px, we kept it at that, ensuring to not have any fonts smaller than that, to aid visually impaired users. The recommended smallest font size for accessible websites is 12px, so we're happy being above that.

### Imagery

* The icons used are simple icons from Font Awesome, to add meaning to items.
* These icons do not convey any meaning that text doesn't also convey, so they didn't require aria-labels.
* The avatars were chosen so as to be gender-less, age-less, race-less, and non-human, so as to avoid excluding any users.
* The avatars are simple designs of basic colors, so as to not be too jarring for users with ADHD.

### Wireframes

[Here are the wireframes for desktop, mobile and tablet for this project](static/docs/wireframes.pdf).

### User Journey

![User journey map](static/docs/img/user-journey.png)

### Features

* Update a Noffle.
* Create and Delete a profile.
* Create, Edit and Delete a Noffle for admin users only.
* Edit admin rights and delete a user for admin users only.
* Confirm to delete modal.
* Auto-updating copyright year.

### Future Features

* Email verification before a user can set their Noffles.
* Enter user's password to delete user account.
* Dynamic desk movement to allow for different office layouts.

### Audio

* No audio is used on this site, so that users who are hard of hearing are not missing out on any features.

### Navigation bar

The navigation bar changes depending on user status and screen size:

| Nav Link | Logged Out | Logged In (User) | Logged In (Admin) |
|-------|-----|-----|-----|
| Logo (Office page if logged in, Landing Page if not) | &#9989; | &#9989; | &#9989; |
| Log In | &#9989; | &#10060; | &#10060; |
| Register | &#9989; | &#10060; | &#10060; |
| Set My Noffles | &#10060; | &#9989; | &#9989; |
| Office Page | &#10060; | &#9989; | &#9989; |
| Profile | &#10060; | &#9989; | &#9989; |
| Manage Noffles | &#10060; | &#10060; | &#9989; |
| Manage Users | &#10060; | &#10060; | &#9989; |
| Log Out | &#10060; | &#9989; | &#9989; |

[Back to Top](#noffle-my-needs)

---

## Database Design

MongoDB was used to store data for this site in a database. The data has been set out in two collections, which are described below:

| Users |    |    |
|---|---|---|
| _id | ObjectId |    |
| username | string |    |
| password | string |    |
| first_name | string |    |
| last_name | string |    |
| image_no | int |    |
| pronouns| string |    |
| is_admin | boolean |    |
| noffles | array | noffles._id |
| panic | boolean |    |

| Noffles |    |
|---|---|
| _id | ObjectId |
| name | string |
| description | string |
| permanent | boolean |
| private | boolean |
| icon | string |

![Overall Database](static/docs/img/noffledb-overall.png)

![Users Database Example](static/docs/img/usersdb.png)

![Noffles Database Example](static/docs/img/nofflesdb.png)

[Back to Top](#noffle-my-needs)

---

## Technologies Used

### Languages Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3#:~:text=CSS3%20is%20the%20latest%20evolution,flexible%20box%20or%20grid%20layouts.)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

### Workspace

#### GitPod

[GitPod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.

### Version Control

#### Git

[Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.

#### GitHub

[GitHub](https://github.com/) is used to store the code for this project after being pushed from Git.

### Wireframing

#### Balsamiq

[Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.

### Responsive Design

#### Am I Responsive Design

[Am I Responsive Design](http://ami.responsivedesign.is/#) was used to check the responsive design of the site, and to create the final site image.

#### Responsinator

[Responsinator](http://www.responsinator.com/) was used to help improve the responsive design on a variety of devices.

### Documentation

#### Shields.io

[Shields.io](https://shields.io/) was used to create the GitHub badges for the top of this README.md file.

### Site Design

#### Font Awesome

[Font Awesome](https://fontawesome.com/) was used on all pages to add the icons.

#### Adobe Online

[Adobe Online](https://spark.adobe.com/tools/remove-background) was used to make the favicon image background transparent.

#### Favicon.io

[favicon.io](https://favicon.io/) used to create a site favicon.

### Database Design Technologies

#### MongoDB

[MongoDB](https://www.mongodb.com/) was used to store the contents of the database, and allow full CRUD functionality.

#### Flask-PyMongo

[Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) was used to connect this Python / Flask app to MongoDB.

### Frameworks, Libraries and Others

#### Heroku

[Heroku](https://www.heroku.com) was used to deploy the live site.

#### Google DevTools

[Google DevTools](https://developer.chrome.com/docs/devtools/) was used to help find what code correlated to which feature.

#### Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to ensure that the code was as performant as possible, confirming to best practices, and SEO and Accessibility guidelines.

#### Flask

[Flask](https://flask.palletsprojects.com/en/2.0.x/) was used to help create the templating for this site.

#### Bootstrap

[Bootstrap](https://getbootstrap.com/) was used to create a beautiful, responsive website.

#### jQuery

[jQuery](https://jquery.com/) was used to make the DOM traversal easier within the JavaScript.

#### Jinja

[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used to auto-populate the site with the contents of the database.

#### RandomKeygen

[RandomKeygen](https://randomkeygen.com/) was used to generate a strong `SECRET_KEY`.

#### Flask-paginate

[Flask-paginate](https://pythonhosted.org/Flask-paginate/) was used to add pagination to the homepage.

#### pip

[pip](https://pip.pypa.io/en/stable/) was used to install the required dependancies for this site.

#### dnspython

[dnspython](https://pypi.org/project/dnspython/) was used to provide access to DNS.

[Back to Top](#noffle-my-needs)

---

## Deployment

### Requirements for Deployment

* Python
* MongoDB account and database
* GitHub account
* Heroku account

### Initial Deployment

MONGO_DBNAME - This is the name of the database you need to connect to in MongoDB.

MONGO_URI - This can be found on the MongoDB website by following these steps:
    * In the clusters tab of your database, click connect on the associated cluster.
    * Click 'Connect', then 'Connect your application'.
    * Copy the string, then substitute the password (from Database access NOT your MongoDB password) and change "myFirstDatabase" to your MONGO_DBNAME.

SECRET_KEY - This is a custom string set up to keep sessions secure. We recommend using a 'Fork Knox' level password generated by [RandomKeygen](https://randomkeygen.com/).

This site was deployed to Heroku by following these steps:

1. Heroku needs to be told what the requirements are for this project, so go into your GitPod terminal, and create files to explain the requirements by using the following commands:
    * `pip3 freeze --local > requirements.txt`
    * `echo web: python run.py > Procfile` - Ensure there is no blank line after the contents of this file
2. Push these changes to your repository.
3. Ensure you have a .gitignore file in your repository, and if not, create one.
4. Add `env.py` and `__pycache__/` into your .gitignore file, and save the file. This is to avoid any sensitive information being added into your repository.
5. Create an env.py file, and add the following information to it, updating the '## x ##' values with your own values:

    ``` python
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", " ## YOUR SECRET_KEY ## ")
    os.environ.setdefault("MONGO_URI", " ## YOUR MONGO_URI ## ")
    os.environ.setdefault("MONGO_DB", " ## YOUR MONGO_DBNAME ## ")
    ```

6. Login or sign up to [Heroku](https://www.heroku.com).
7. Select 'Create New App' in the top right of your dashboard.
8. Choose a unique app name, and select the region closest to you, before clicking 'Create App'.
9. Go to the 'Deploy' tab, find 'Deployment Method' and select 'GitHub'.
10. Search to find your GitHub repository, and click 'Connect'. Don't enable automatic deployment yet, as this can cause errors.
11. Go to the 'Settings' tab, find 'Config Vars', and click 'Reveal Config Vars'.
12. Enter key value pairs that match those in your env.py file, displayed like this :

    | Key | Value |
    |---|---|
    | IP | 0.0.0.0 |
    | PORT | 5000 |
    | MONGO_DBNAME | ## YOUR DATABASE NAME ## |
    | MONGO_URI | ## YOUR MONGO_URI ## |
    | SECRET_KEY | ## YOUR SECRET_KEY ## |

13. Go to the 'Deploy' tab, and click 'Enable Automatic Deployment'.
14. In 'Manual Deploy', choose which branch you'd like to deploy from (We chose 'main' branch, this is also known as 'master').
15. Click 'Deploy Branch' to deploy your app onto the Heroku servers.
16. Once the app has finished building, click 'Open App' to open your site.

### How to Fork it

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [Abibubble/noffle-my-needs](https://github.com/Abibubble/noffle-my-needs).
3. In the top right, click "Fork".
4. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
5. You will also need to install all of the project requirements. This can be done using the command `pip3 install -r requirements.txt`.
6. Type `python3 app.py` in your GitPod terminal to run your local site of this project.

### Making a Local Clone

1. Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/Abibubble/noffle-my-needs) for this site.
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should clone the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL that was copied in Step 4.
8. Press Enter, and your local clone will be created.
9. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
10. You will also need to install all of the project requirements. This can be done using the command `pip3 install -r requirements.txt`.
11. Type `python3 app.py` in your GitPod terminal to run your local site of this project.

For a more detailed version of these steps, go to the [Github Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) page on this topic.

[Back to Top](#noffle-my-needs)

---

## Testing

### W3C Validator

The W3C Markup Validator, W3C CSS Validator and JSHint were used to validate the project to ensure there were no syntax errors within the site.

1. W3C Markup Validator
    * [HTML Results](https://validator.w3.org/nu/?doc=http%3A%2F%2Fnoffle-my-needs.herokuapp.com)
    * The only error is that sections lack headings.
    * This is due to the templating, as every page does have a header.

2. W3C CSS Validator
    * [CSS Results](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fnoffle-my-needs.herokuapp.com&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * The only errors found here are due to Bootstrap.

3. markdownlint GitPod Extension
    * [markdownlint Extension](https://open-vsx.org/vscode/item?itemName=DavidAnson.vscode-markdownlint)
    * There were no Markdown errors reported on the markdownlint extension.

4. JSHint GitPod Extension
    * [JSHint Extension](https://open-vsx.org/vscode/item?itemName=dbaeumer.jshint)
    * There were no JavaScript errors reported on the JSHint extension.

5. PyLint Extension
    * [PyLint Extension](https://pypi.org/project/pylint/)
    * There were no Python errors reported on the PyLint extension.

[Back to Top](#noffle-my-needs)

### Testing User Stories

#### First Time Visitor

##### Easily navigate the site

* The navigation bar is easily visible on every page of the site.
* This displays differently depending on what access the user has.
* The navigation bar is easy to understand and always there for ease of navigation on the site.
* The logo at the top left of the page takes the user back to the home page at any given point.

##### Intuitively and easily understand what to do

* All buttons are clearly labelled.
* All links and buttons have descriptive text.
* Upon landing on the site, the user is greeted and can clearly see what the site is about by the small description under the 'About Noffle My Needs' heading.
* Clicking on the button below this section takes a user directly to where they need to by in order to begin selecting their Noffles on the 'Set My Noffles' page.
* Each page and each step taken by a user, leeds a user through the site to the appropriate pages.

##### Register for an account

* The Register button is visible for all users who aren't logged in.
* The register form is clear and easy to follow.
* There are validation messages if you don't enter the correct format of information.
* A user is able to register an acount by clicking the 'Register' link in the Menu, or by clicking the Register button at the bottom of the landing page.
* A form will be presented to the user to complete and a message is displayed to welcome the new user if everything was successful.

##### Set my Noffles

* Upon registration or logging in, a user is immediately taken to the 'Set My Noffles' page.
* The user can click on as many Noffles as they wish, along with setting them to 'private' mode.
* In this case the Noffles are only diplayed to those with administration rights.

##### Get visual feedback when an action on the site is completed

* Whenever an action on the site occurs, a message is displayed to the user.
* This message is clear, at the top of whichever page that the user is on.

#### Returning Visitor

##### Log in

* The Log In button is visible for all users who aren't logged in.
* The Log In button is positioned on the navbar.
* The form is clear and easy to follow.

##### Update their Noffles

* Upon registration or logging in, a user is immediately taken to the 'Set My Noffles' page.
* The user can then set any Noffles they like, or remove current Noffles.
* All non-permanent Noffles are also removed from the user when they log out.

##### See the public Noffles of other users

* Public Noffles of all users are displayed on the Office page.
* Regular users can only see public Noffles on the Office page, while admin users can see all Noffles of all users.

##### Be confident that their password is be stored securely

* Werkzeug's password hashing methods have been used to store all user's passwords in a secure and safe way.

##### Navigate intuitively, with no need to use the browser's back button

* The navigation bar is constantly visible across the top of the site.
* This is either the full navigation bar, or the condensed burger icon menu bar on smaller screen sizes.

#### Admin

##### Be confident that a user can't to brute force their way into the restricted pages

* Admin users are set with an is_admin toggle in the database, so that it doesn't rely on usernames.
* If a user without access rights tries to access a restricted page, it presents them with the 404 page, with a navigation bar at the top to take them back to the pages they're allowed to access.

##### Edit or delete any user

* Admin users are set with an is_admin toggle in the database, so that it doesn't rely on usernames.
* If the user has the is_admin toggle set to true, then they will have access to the Manage Users page.
* This enables the admin to edit or delete any user.

##### Add a new Noffle

* Admin users are set with an is_admin toggle in the database, so that it doesn't rely on usernames.
* If the user has the is_admin toggle set to true, then they will have access to the Manage Noffles page.
* This enables the admin to add a new Noffle.

##### Edit or delete any Noffle

* Admin users are set with an is_admin toggle in the database, so that it doesn't rely on usernames.
* If the user has the is_admin toggle set to true, then they will have access to the Manage Noffles page.
* This enables the admin to edit or delete any Noffle.

##### Give or remove admin rights

* Admin users are set with an is_admin toggle in the database, so that it doesn't rely on usernames.
* If the user has the is_admin toggle set to true, then they have access to the Manage Users page.
* From there, any user can be deleted, or have their admin rights switched on or off.
* The only user that cannot be edited is the main admin account, to ensure the site isn't left without an admin user by mistake.

[Back to Top](#noffle-my-needs)

### Full Testing

#### Desktop / Laptop

1. Google Chrome
    * All tested and working correctly.

2. Microsoft Edge
    * All tested and working correctly.

3. Mozilla Firefox
    * All tested and working correctly.

4. Safari
    * All tested and working correctly.

#### Tablet

1. Safari
    * All tested and working correctly.

#### Mobile

1. Google Chrome
    * All tested and working correctly.

2. Safari
    * All tested and working correctly.

3. Samsung Internet
    * All tested and working correctly.

### Further Testing

* The website was tested on Google Chrome, Firefox, Microsoft Edge, Safari and Samsung Internet browsers.
* Testing was not done on Internet Explorer due to it being depreciated in favour of Microsoft Edge.
* The website was viewed on a variety of devices, including:
  * Custom built desktop PC, running Windows 10
  * Acer Aspire V Nitro Laptop, running Windows 10
  * Lenovo B51 IntelCore i7 Laptop, running Ubuntu 16.04 LTS
  * MacBook Pro (15-inch, 2017), running macOS Catalina
  * MacBookAir7,2 (13-inch, 2017)
  * iPad 6,11 5th generation, running iOS 10.3
  * Amazon Fire tablet 7
  * iPhone 7
  * iPhone X
  * iPhone 12
  * OPPO Find X2
  * OPPO Find X2 Lite
  * Samsung Galaxy A70
  * Samsung Galaxy S9
  * Samsung Galaxy S10+
  * Samsung A20
  * xBox One

A large amount of testing was done to ensure that all pages were visible or hidden correctly, all buttons worked as they should, and the site worked as it should.
Friends, family members, and other developers were asked to review the site and documentation to point out any bugs and/or user experience issues that they came across.

[Back to Top](#noffle-my-needs)

### Solved Bugs

1. Adding Noffles to the Noffles list in the user database was a challenge.
    * We tried to add the entire Noffle object into the user database, but quickly realised we'd be better off just adding in the Noffle id.
    * As it was a list, we tried to append the Noffle id when a user adds a new Noffle.
    * Unfortunately, it would always replace the previous Noffle that was already there.
    * The solution was to use the $pull and $push the functionality of MongoDB.
2. Displaying each noffle on the profile page wasn't working.
    * Due to bug #1, we were referring to the Noffles in the user database by Noffle id.
    * As we have a list of Noffle ids as our Noffles we couldn't simply display it.
    * The solution was to get the user from the database, and iterate through the Noffles list using the Noffle id.
    * We then used this id to find the respective Noffle in the database, append it to a list, and then iterate through this list in the front end.
3. Displaying the noffle icons on the Office page for each individual user wasn't working.
    * Definitely the harder challenge in the project, as all users are present on the Office page.
    * It was hard to figure out how to separate the noffles of each user.
    * The solution was to create a dictionary with the key-value equal to the username and the value itself with a list of the Noffles of that user.
    * Then in the front end, we had to iterate through this dictionary to display what we need.
    * With this dictionary, we could apply the same logic for each user modal with the information of their Noffles.
4. Displaying permanent Noffles separately from temporary Noffles on Set My Noffle page.
    * We tried different approaches to try to display the Noffles separately.
    * We tried to pass all the Noffles to the Set My Noffles page and iterate through them.
    * Then with an if statement to separate between temporary and permanent Noffles.
    * This didn't work because we would have to create a new row for each Noffle.
    * We came up with the solution of separating them into two arrays in the set_noffles function and passing this to the front end with the Noffles already separated.

### Known Bugs

* The site breaks when the user clicks the 'Back' button on their browser.
* A11y Allies are unaware of any other bugs left in this code. If you find any, please let us know at one of our GitHubs, which you can find below in [Credits](#credits)

### Lighthouse Testing

We tested this website using DevTools Lighthouse feature, and got these results:

#### Desktop Lighthouse

![Lighthouse desktop first try](static/docs/img/lighthouse.png)

#### Mobile Lighthouse

![Lighthouse mobile first try](static/docs/img/lighthousemobile.png)

#### Performance

* We were happy with this score, as it was only knocked down due to the use of Bootstrap.

#### Accessibility

* We were happy with this score.
* All headings are sequential.
* All images have alt text.
* All icons have text nearby to explain use, so the icons are not required for UX.
* All tap targets are correctly sized at a minimum of 48px by 48px, with an 8px gap between them, and aren't overlapping other content.

#### Best Practices

* We were happy with this score, as it was only knocked down due to the use of Bootstrap.

#### SEO

* We were happy with this score.
* All relevant meta tags have been included for this site.

[Back to Top](#noffle-my-needs)

---

## Credits

### Code

* [Font Awesome](https://fontawesome.com/): Library of icons used for social media and download links.
* [Autoprefixer CSS online](https://autoprefixer.github.io/): To aid in the CSS prefixing.
* [Boostrap](https://getbootstrap.com/): Throughout the site, to create a beautiful responsive site, without taking too much time.

### Content

* All content was created by the [Code Institute](https://codeinstitute.net/) September 2021 Hackathon team A11y Allies.

### Media

* [Georgie Cobbs on Unsplash](https://unsplash.com/photos/bKjHgo_Lbpo) provided the hero image on the landing page. This image is free to use.
* The user avatars were found on [Shutterstock](https://www.shutterstock.com/image-vector/abstract-characters-geometric-comic-creature-emotions-1953566236), which we have an account for, and thus we able to get commercial licence to use the images.

### Research

* [The A11y Project](https://www.a11yproject.com/)
* [Daniel Britton - Dyslexia](http://danielbritton.info/dyslexia)
* [User Zoom](https://www.userzoom.com/ux-library/five-ways-to-make-usable-websites-for-people-with-dyslexia/)
* [Allana Bailey](https://allanabailey.github.io/color-blind-project1/)
* [ERC Dancing](https://ercdancing.maynoothuniversity.ie/)

### Acknowledgements

* The team at [Code Institute](https://codeinstitute.net/), for teaching us the necessary skills to create this site.
* The [Code Institute](https://codeinstitute.net/) Hackathon team A11y Allies, who created this page. This team consists of :
  * [Abi Harrison](https://github.com/Abibubble)
  * [Andrew Dempsey](https://github.com/andrewdempsey2018)
  * [Carla Buongiorno](https://github.com/CarlaBuongiorno)
  * [Henrique Peroni](https://github.com/Henriqueperoni)
  * [Monika Hrda](https://github.com/monika-hrda)
* Our team facilitator [Megan Armstrong](https://www.linkedin.com/in/megan-armstrong4/).

[Back to Top](#noffle-my-needs)
