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
  * [Features left to implement](#features-left-to-implement)
  * [Testing](#testing)
  * [Bugs](#bugs)
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
  * Sign Up:
    * Users can register their account by clicking on the sign up button showing
      on the navbar.
  * Login:
    * Users can login by clicking on the button showing on the navbar next to 
      sign up so that they can enjoy the functionalities of the website.
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
  * Read the post:
    * Users can read the postblog by clicking on the title link showing below the
      image of the post.
    * Read the category postblog:
      * Users can read the category post by clicking on the category link showing
        next to the time of post created.
  * Edit or Update the post:
    * Users can edit or update the post by clicking on the edit button showing below 
      the image of the post.
  * Delete the post:
    * Users can delete the post by clicking on the delete button showing below the
      image of the post.
    * Users cannot delete the others post. If they try to delete the others post
      then a message will be displayed showing "sorry, you are not allowed to 
      delete this post"

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

 ## Features left to implement
  

# Testing
  I have manually tested this project by doing the following:
  * Passed the code through a PEP8 linter and confirmed there are no problems
  * Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
  * Tested in my local terminal and the Code Institute Heroku terminal

 ## Validator Testing
   * PEP8
     * No errors were returned from [PEP8 checker](http://pep8online.com/)    

   [Back to top](#)

  ## Bugs
   ### solved bugs

 ## Unfixed Bugs
   * No unfixed bugs.
   
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
   * Cloudinary is used in this project for images and videos purposes.

 ## Acknowledgements
   * My mentor who guided me througout the project.

 [Back to top](#)