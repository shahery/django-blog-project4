# Blog web
  Blogweb is the blogpost website made for the educational purposes for the milestone project.
  This website is created for the users who love social media. In this blogweb website, there 
  are a lot of functionalities for the users like, users can create the posts with the images, can 
  add or select the category for the post, read the post, edit or update the post, delete the post,
  can like the post and can leave a comment on the post.
  


  The deployed link can be found here: 

# Table of contents
  * [Users stories](#users-stories)
  * [Existing Features](#existing-features)
  * [Technology Used](#technology-used)
  * [Agile Technique](#agile-technique)
  * [Features left to implement](#features-left-to-implement)
  * [Testing](#testing)
  * [Bugs](#bugs)
  * [Project visualization](#project-visualiztion)
  * [Colour](#colour)
  * [Deployment](#deployment)
  * [Credits](#credits)

# Users stories:
  * As a user I can read the blogposts
  * As a user I can select the category to read that kind of posts
  * As a user I can create the post
  * As a user I can add the category for the post
  * As a user I can edit or update the post
  * As a user I can delete the post
  * As a user I can like the post
  * As a user I can comment on the post
 												

  [Back to top](#)

# Existing Features
  * Navbar:
    * Users can read the categories, sign up and login using the links showing on the navbar.
    ![navbar2](https://user-images.githubusercontent.com/95220937/178305659-02981b1a-e294-48c2-8391-fe6757f64e40.png)
  * After login Navbar:
    * Users can read the categories, add post, add category and logout using the links showing on the navbar.
    ![navbar1](https://user-images.githubusercontent.com/95220937/178306003-a1296450-fda7-4370-a607-168fadb4bb56.png)
  * Read the category postblog:
    * Users can read the category post by clicking on the categories dropdown link showing
      on the navbar.
      ![pic4](https://user-images.githubusercontent.com/95220937/178114876-34f59cbe-f780-4f8b-85d5-a204c154b0d3.png)
  * Sign Up:
    * Users can register their account by clicking on the sign up button showing
      on the navbar.
      ![pic6](https://user-images.githubusercontent.com/95220937/178114614-83477fe7-537d-48ea-8184-798dffbf5e09.png)
  * Login:
    * Users can login by clicking on the button showing on the navbar next to 
      sign up so that they can enjoy the functionalities of the website.
      ![pic7](https://user-images.githubusercontent.com/95220937/178114651-2f843ebf-1064-4074-bc66-4fcec72ffd3f.png)
    * Note:
          Users can only create, edit and delete the post by creating their account
          on the website.
       
  * Add the post:
    * Users can create the posts along with uploading images
    * steps to create the posts are as below
      * First put the title in the title field for your post.
      * Put the title tag for your post in the slug field.
      * As you have logged in so, you can select your name as the author for the post.
      * You can select the category by clicking on the category field or you can add
       the category by clicking on the 'Add Category' option showing on the navbar
       for the post according to your choice.
      * You can add the content for your post and style it using the editor showing
       in the content field.
      * You can also upload the image using the upload image field for your post.
      * If users don't upload the image for their post, then default image will be
        shown for their post.
        ![pic11](https://user-images.githubusercontent.com/95220937/178114736-135f608b-a98c-40f6-abb6-c5daf9f66041.png)
        ![pic12](https://user-images.githubusercontent.com/95220937/178114768-fd5cf1d1-4ecb-424e-9095-3904b9f442a9.png)
  * Read the post:
    * Users can read the postblog by clicking on the title link showing below the
      image of the post.
      ![pic3](https://user-images.githubusercontent.com/95220937/178114802-3ee61823-a93f-4495-9b31-c9fe5f0e55da.png)
  * Like the post:
    * Users can like the post.
     ![pic16](https://user-images.githubusercontent.com/95220937/178115174-7f189379-7c2d-45d8-b334-c7aea5e82ae9.png)
  * Comment on the post:
    * Users can comment on the post.
    ![pic10](https://user-images.githubusercontent.com/95220937/178115272-a8a26f05-54f6-4d5b-a3f6-d034d46fa6cc.png)
  * Edit or Update the post:
    * Users can edit or update the post by clicking on the edit button showing below 
      the image of the post.
      ![pic13](https://user-images.githubusercontent.com/95220937/178114930-3b96ec0b-013c-4041-8469-ffcd8320f339.png)
      ![pic14](https://user-images.githubusercontent.com/95220937/178114952-785cf8b7-5768-4857-b7fa-9daf737fe819.png)
  * Delete the post:
    * Users can delete the post by clicking on the delete button showing below the
      image of the post.
    * Users cannot delete the others post. If they try to delete the others post
      then a message will be displayed showing "sorry, you are not allowed to 
      delete this post"
      ![pic15](https://user-images.githubusercontent.com/95220937/178114998-f78c3cd1-1e72-4874-83ef-0ab155081c59.png)
  * Site pagination:
    * Site is paginated for 10 posts at one page when posts will be more than 10, it will display on the next page.
  * Footer:
    * Footer displays the social links and purpose of post.
      ![pic17](https://user-images.githubusercontent.com/95220937/178115076-2f020272-6143-49fb-870f-a79223d43f21.png)

   [Back to top](#)

# Technology Used 
  * [Html](https://en.wikipedia.org/wiki/HTML)
  * [Css](https://en.wikipedia.org/wiki/CSS)
  * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  * [Boostrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
  * [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [GitHub](https://github.com)
  * [Gitpod](https://www.gitpod.io)
  * [Heroku](https://en.wikipedia.org/wiki/Heroku) 

   [Back to top](#)

# Agile Technique:
  * Agile technique is used in this project. You can have a look here
    [Agile](https://github.com/users/shahery/projects/4) 

 ## Features left to implement
  * I will add the user profile with image upload option in the future for the users who create 
  the account and also edit profile option so they can edit the profile.
  
# Testing
  I have manually tested this project by doing the following:
  * Passed the code through a PEP8 linter and confirmed there are no problems
  * Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
  * Tested in my local terminal and the Code Institute Heroku terminal
 ## Python and Javascript Testing:
  * automated tests for python and javascript were undertaken to check the functioning of the codes and it were all passed.
  ![Python-test](https://user-images.githubusercontent.com/95220937/178474580-cbe19091-6625-4829-87a4-65f8e51c60fc.png)
  ![js-test](https://user-images.githubusercontent.com/95220937/178474501-a6d41196-1658-4d5c-b913-6d01e29772f0.png)

 ## Validator Testing
   * PEP8
     * No errors were returned from [PEP8 checker](http://pep8online.com/)    

   [Back to top](#)

  ## Bugs
   ### solved bugs
    * While creating the project I faced the bug of relation does not exist error, which actually took a lot of my time to solve. It was actually the migrations error because I accidentally deleted some migrations in my project.
    * Steps I took to solve:
      * Firstly, I deleted all the migrations in my apps except __init__.py file
      * Then I deleted the db.sqlite3 file showing in the files
      * Because the database I was using connected with heroku so I had to reset the database in the heroku platform and also I deleted the heroku postgres and added the new one and also added the new DATABASE_URL in the env.py file
      * Then I commented out the admin.py, forms.py, models.py, views.py, urls.py files and also one line in the urls of blogweb in which blog app was connected
      * Then I ran the command python3 manage.py makemigrations and python3 manage.py migrate
      * After that I uncommented the models.py file and ran the commands python3 manage.py makemigrations blog and python3 manage.py migrate blog for my models
      * And finally I uncommented all the files which I commented out before and ran the server using the command python3 manage.py runserver and the bug was fixed in this way.

 ## Unfixed Bugs
   * No unfixed bugs.
   
   [Back to top](#)

# Project visualization:
  ![pic18](https://user-images.githubusercontent.com/95220937/178124755-509cbf85-e1ae-4355-993b-fe0803381fea.png)

  [Back to top](#)

# Colour
  * #d85428, #2a4878, #abbdd9, #a3cfc7, black, #e8e2d8, white, #0A66C2, lightgray, combination 
   of these colours were used in the website for foreground and background.

  [Back to top](#)
# Deployment
 This project was deployed using the code institute's mock terminal for heroku.
   * Steps for automatic deployment:
     * Fork or clone this repository
     * Create a new heroku app
     * Set the buildpacks to Python and NodeJS in that order
     * Link the heroku app to the repository
     * Click on Deploy 

   * Steps for manual deployment:
     * Create the env.py file, requirements.txt file and Procfile in the github for the
       project you want to deploy
     * Make it sure, you dont leave any empty newline in the Procfile
     * Create a new heroku app
     * Click on the resources in the heroku and add heroku postgres database for the project
     * Heroku postgres will create the database_url in the config vars, just copy that and 
       paste in the env.py file of your project in the github.
     * If you are using the cloudinary for your project then you will have to copy
       the cloudinary_url and paste in the env.py file same like database_url.
     * In the config vars, you have to create the Port: 8000 and secret key for your project
       and also copy and paste that secret key in env.py file of your project
     * After all this done, click on the deploy tab and connect your repository you want to 
       deploy with the heroku and click on the deploy branch
     * Thats it, you are good to go, your project has been deployed, you can see your project
       clicking on the open app button.

  [Back to top](#)
# Credits
 ## Content
   * The Idea of README.md file and the codes used for the website were also learnt from [Code Institute](https://codeinstitute.net)
   * Few codes were also learnt from [codemy.com](https://codemy.com/)

 ## Media
   * Cloudinary is used in this project for images purposes.

 ## Acknowledgements
   * My mentor who guided me througout the project.

 [Back to top](#)