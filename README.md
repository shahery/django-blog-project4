# Blog web
  Blogweb is the blogpost website made for the educational purposes for the milestone project.
  This website is created for the users who love social media. In this blogweb website, there 
  are a lot of functionalities for the users like, users can create the posts with the images, can 
  add or select the category for the post, read the post, edit or update the post, delete the post,
  can like the post and can leave a comment on the post.

  ![Am-i-responsive](https://user-images.githubusercontent.com/95220937/193538746-044b7f86-16a4-4ebb-8fb8-42625e7662ce.png)
  


  The deployed link can be found here: [Live Site](https://blogweb786.herokuapp.com/)

# Table of contents
  * [Ux design](#ux-design)
  * [Existing Features](#existing-features)
  * [Technology Used](#technology-used)
  * [Agile Technique](#agile-technique)
  * [Features left to implement](#features-left-to-implement)
  * [Testing](#testing)
  * [Bugs](#bugs)
  * [Deployment](#deployment)
  * [Credits](#credits)


# Ux design:
  ## Strategy:
   * Blogweb is the blogpost website created for the purpose of creating blogposts and share information to the users.
   The key points while creating this website are following below:
     * Create an online presence
     * Interact with users who share information through blogs/posts
     * Create a category posts/blogs
     * Create a user friendly environment
     * Display key information to the users
     * Attract more users
     * Quick and intuitive navigation
     * Easy access to key information
     * Quick and hassle-free processes
     * Create entertainment environment

  ## User stories(Scope):
   * User stories were created for the project by keeping in mind the story points and moscow method to complete the website accordingly.

      ![User-stories](https://user-images.githubusercontent.com/95220937/193207666-97896a81-c525-4f2e-8627-00572343aee9.png)
 												

  ## Wireframes(Skeleton):
   * Wireframes were created for the project for the purpose of ux planning and designing of the website.
  
     * Home page desktop:

       ![Home-page-desktop](https://user-images.githubusercontent.com/95220937/192646130-9ec6ec8e-6627-45f7-8f7a-a19e8bc4d2a1.png)

     * Home page mobile:

       ![Home-page-mobile](https://user-images.githubusercontent.com/95220937/192149712-a23df7eb-d310-4083-ad7f-1d5cdf7082d1.png)

     * Post detail page:

       ![Post-detail-page](https://user-images.githubusercontent.com/95220937/192646135-d247fa7e-cf4a-4a80-8fa8-a1fb55f2ef30.png)

     * Add post page:

       ![Add-post-page](https://user-images.githubusercontent.com/95220937/192646532-dd8ad193-9f6d-4071-987b-4c5c44f1e3c6.png)

     * Add category page:

       ![Add-category-page](https://user-images.githubusercontent.com/95220937/192646139-e7880de4-9d2a-4b34-b241-7252b23dcef7.png)

     * Edit post page:

       ![Edit-post-page](https://user-images.githubusercontent.com/95220937/192646820-c630c5e4-e0a3-474a-9df6-ef29420716ff.png)

     * Sign up page:

       ![Sign-up-page](https://user-images.githubusercontent.com/95220937/192646530-612d8ccc-5654-48f5-93c2-b1cc2ff49d39.png)

     * Sign in page:

       ![Login-page](https://user-images.githubusercontent.com/95220937/192646822-f97a023c-4cab-4e25-af12-337755cd65df.png)

     * Delete post page:

       ![Delete-post-page](https://user-images.githubusercontent.com/95220937/192646506-2dbe91b2-05ce-47e9-9842-6653f06ebf49.png)

  ## Surface:
   * Colours:
     * #d85428, #ffff00, #2a4878, #abbdd9, #a3cfc7, black, #e8e2d8, white, #0A66C2, lightgray, combination 
      of these colours were used in the website for foreground and background.
   * Typograpghy:
     * The fonts chosen for this project were taken from [google fonts](https://fonts.google.com/)
       * font-family: 'Lato'
       * font-family: 'Roboto'
   * Icons:
     * The icons in the website were all taken from [Font awesome](https://fontawesome.com/)
   * Images:
     * [Cloudinary](https://cloudinary.com/) is used in this project for images purposes.

  ## Structure:
   * Information Architecture:
     * The navigation for this website was designed to be user-friendly and intuitive. Grouping pages according to relationships and functionality as shown below.

   * Entity Relationship Model(database schema):
     * The ERM design demonstrates how the information will be stored while the data is at rest. Here we can see one-to-many relationships between the User model and the Comment and/or Post model. The same relationship is established between the Post model and the Comment. The rest of the relationships are derived from Django built-in models such as User, AbstractUser, Session etc.

     ![pic18](https://user-images.githubusercontent.com/95220937/178124755-509cbf85-e1ae-4355-993b-fe0803381fea.png)



  [Back to top](#)

# Existing Features
  * Navbar:
    * Users can read the category blogs by clicking on the category in the dropdown of categories, sign up and login using the links showing on the navbar.

      ![navbar1](https://user-images.githubusercontent.com/95220937/193478681-8e7b9c32-f0a2-4c16-82cd-f064b6d00182.png)
  * After login Navbar:
    * Users can read the categories, add post, add category and logout using the links showing on the navbar.

      ![navbar2](https://user-images.githubusercontent.com/95220937/193478682-a1e40e0e-280c-41ae-b5e1-35866c88affe.png)
  * Read the category blogpost:
    * Users can read the category post by clicking on the categories dropdown link showing
      on the navbar.

      ![category-post](https://user-images.githubusercontent.com/95220937/193479296-1e2f918e-1230-4e99-8784-0e027b80d5cb.png)
  * Add category:
    * Users can add the category through the form below to create the desired category posts.

      ![Add-category](https://user-images.githubusercontent.com/95220937/193478800-0b2c1c45-038f-49aa-981f-840218ca8acf.png)
  * Sign Up:
    * Users can register their account by clicking on the sign up button showing
      on the navbar.

      ![sign-up](https://user-images.githubusercontent.com/95220937/193479218-bcb31a26-d450-4932-a2cd-995b8a4399d1.png)
  * Login:
    * Users can login by clicking on the button showing on the navbar next to 
      sign up so that they can enjoy the functionalities of the website.

      ![sign-in](https://user-images.githubusercontent.com/95220937/193479219-b163f1a9-f5e8-442f-9b2b-ee3f9b683e42.png)
    * Note:
          Users can only create, edit and delete the post by registering their account
          on the website.
  * Logout:
    * Users logout/sigout page should look like the image below:

      ![logout](https://user-images.githubusercontent.com/95220937/193478799-e1d40c04-6bc5-437a-a054-5f75c32c00f6.png)
 
  * Add the post:
    * Users can create the posts along with uploading images
    * steps to create the posts are as below
      * First put the title in the title field for your post.
      * Put the title tag for your post in the slug field.
      * You can select the category by clicking on the category field or you can add
       the category by clicking on the 'Add Category' option showing on the navbar
       for the post according to your choice.
      * You can add the content for your post and style it using the editor showing
       in the content field.
      * You can also upload the image using the upload image field for your post.
      * If users don't upload the image for their post, then default image will be
        shown for their post.

        ![Add-post1](https://user-images.githubusercontent.com/95220937/193478749-aeb14594-f83c-4107-ac2c-13ef4598c337.png)
        ![Add-post2](https://user-images.githubusercontent.com/95220937/193478747-5e28878e-5fbd-4713-b14d-4ba8e20e8660.png)
  * Read the post:
    * Users can read the postblog by clicking on the title link showing below the
      image of the post.

      ![read-post](https://user-images.githubusercontent.com/95220937/193479061-095e0171-0755-4721-af32-99ff5b895c31.png)
  * Like the post:
    * Users can like the post by clicking on the icon of thumbs up.

      ![like-post](https://user-images.githubusercontent.com/95220937/193479059-e3aa2539-b434-4205-bafe-bcf817c48823.png)
  * Comment on the post:
    * Users can comment on the post by writing in the body field showing.

      ![comment-post](https://user-images.githubusercontent.com/95220937/193479058-033a0203-3925-42e5-b07b-febf98f0966d.png)
  * Edit or Update the post:
    * Users can edit or update the post by clicking on the edit button showing below 
      the image of the post.

      ![edit-post1](https://user-images.githubusercontent.com/95220937/193479134-51b2c611-8043-40e7-b2fd-f0abd74f60aa.png)
      ![edit-post2](https://user-images.githubusercontent.com/95220937/193479131-51687bb2-adbe-4197-8573-3c55367eb97e.png)
  * Delete the post:
    * Users can delete the post by clicking on the delete button showing below the
      image of the post.
    * Users cannot delete the others post. If they try to delete the others post
      then a message will be displayed showing "sorry, you are not allowed to 
      delete this post"

      ![delete-post](https://user-images.githubusercontent.com/95220937/193479130-eeaecfd1-91dd-44f7-b634-ed1798bc1d85.png)
  * Site pagination:
    * Site is paginated for 10 posts at one page when posts will be more than 10, it will display on the next page.
  * Footer:
    * Footer displays the social link and purpose of post.

      ![footer](https://user-images.githubusercontent.com/95220937/178717236-931bd07e-13ce-4d01-9bf3-bd333a8df6f7.png)

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
    [Agile](https://github.com/users/shahery/projects/10/views/1) 

  * Kanban board was used in this project to handle user stories.

    ![Kanban-board](https://user-images.githubusercontent.com/95220937/192648324-20ec45ad-93c6-4d84-bbf1-0ca55d2c496a.png)

  * User stories were created for following the agile technique

  * MOSCOW method was used to prioritize the task using the label of MustHave, ShouldHave, CouldHave and WontHave.

    ![moscow1](https://user-images.githubusercontent.com/95220937/192648976-f62fa0bc-c126-413a-94b2-435528745fc6.png)
    ![moscow2](https://user-images.githubusercontent.com/95220937/192648989-b908e76c-4000-4d57-b999-8a4d27b12586.png)

  * Milestones were created for the project to complete the tasks.

    ![Milestones](https://user-images.githubusercontent.com/95220937/192647997-13c21095-9ea6-4c82-a45e-8bf528381ffe.png)

 ## Features left to implement
  * I will add the user profile with image upload option in the future for the users who create 
  the account and also edit profile option so they can edit the profile.
  
# Testing
 ## Python and Javascript Testing:
  * automated tests for python and javascript were undertaken to check the functioning of the codes and it were all passed.
  ![Python-test](https://user-images.githubusercontent.com/95220937/178474580-cbe19091-6625-4829-87a4-65f8e51c60fc.png)
  ![js-test](https://user-images.githubusercontent.com/95220937/178474501-a6d41196-1658-4d5c-b913-6d01e29772f0.png)

 ## Validator Testing
   I have manually tested this project by doing the following:
   * Passed the code through a PEP8 linter and confirmed there are no problems
   * PEP8
     * No errors were returned from [PEP8 checker](http://pep8online.com/)
     * All the errors were removed from the files to fulfil the requirements of PEP8 and was made sure by checking the errors using the command "python3 -m flake8". Only those few errors were left who creates the problems in the website by adjusting like in env.py file or setting.py etc.

       ![blog-views](https://user-images.githubusercontent.com/95220937/192090690-a6107b0f-682c-400c-964e-c2eed3afc084.png)
       ![Flake8](https://user-images.githubusercontent.com/95220937/193208646-68870d87-42d4-44b8-bbbb-0954c19dd7f0.png)

       [blog-test-models](https://user-images.githubusercontent.com/95220937/192090743-7d8b4cd2-aa3e-4ef1-96a7-7409a657680f.png), [blog-test-views](https://user-images.githubusercontent.com/95220937/192090744-61b69697-5015-4296-8c74-ce9f38ac3c39.png), [blog-urls](https://user-images.githubusercontent.com/95220937/192090746-9508f15b-36f4-4e3d-9f62-5c884940bcd8.png), [blog-models](https://user-images.githubusercontent.com/95220937/192090806-2ac27262-2592-4472-a754-2f5c50d71b9e.png), [blog-test-forms](https://user-images.githubusercontent.com/95220937/192090807-d86e2345-0184-4246-93d3-b05459613307.png), [blog-admin](https://user-images.githubusercontent.com/95220937/192090844-95663ca7-fb9f-47c9-9dd3-40417cd80581.png), [blog-apps](https://user-images.githubusercontent.com/95220937/192090845-d8930cbb-6881-4535-b3ae-2afe279081c9.png), [blog-forms](https://user-images.githubusercontent.com/95220937/192090846-4aa22320-2303-420e-b2d7-03df02af9b58.png), [blogweb-wsgi](https://user-images.githubusercontent.com/95220937/192090912-1e7088bd-6c9a-40a3-b99f-36da26a5bd4b.png), [blogweb-urls](https://user-images.githubusercontent.com/95220937/192090914-51511ec7-d14e-4fd1-a6df-55577de0ddd8.png), [blogweb-asgi](https://user-images.githubusercontent.com/95220937/192090915-09d451dd-5d5d-40fe-b969-04402f86789c.png)
   * Html checker:
     * No errors were returned from [W3C Html](https://validator.w3.org/)

       ![home](https://user-images.githubusercontent.com/95220937/192063473-431a7ab5-f96f-4028-ab5a-6182de3466a5.png)

       [Add-category](https://user-images.githubusercontent.com/95220937/192063569-60df50f3-6871-4c72-b868-ff532ac05572.png), [Post-detail](https://user-images.githubusercontent.com/95220937/192063571-d05cbf03-e19d-49d3-b21b-0741e39ce086.png), [Signup](https://user-images.githubusercontent.com/95220937/192063573-f3229377-7ce0-48a4-92d4-21456c1bd7e2.png), [Sign-in](https://user-images.githubusercontent.com/95220937/192063773-2990d71e-7e39-44ce-a611-07e5f22b6379.png), [Categories-page](https://user-images.githubusercontent.com/95220937/192063769-74b894c2-a0d8-4bef-b8d3-1280be1be066.png), [Delete-post](https://user-images.githubusercontent.com/95220937/192063767-d5aad0fa-17eb-4429-ac8f-dab5bea9a5e6.png)

   * CSS checker:
     * No errors were returned from [W3C CSS](https://jigsaw.w3.org/css-validator/)

       ![css-check](https://user-images.githubusercontent.com/95220937/192064149-c809b0af-a68e-45fd-b38d-4060eb2db801.png)
   * JS checker:
     * No errors were returned from [JS HINT](https://jshint.com/)
      
       ![Timeout](https://user-images.githubusercontent.com/95220937/192065319-56e2a796-dce2-42cf-951b-e4d129315947.png)

       [js-1](https://user-images.githubusercontent.com/95220937/192065387-f5fd7f0c-3683-41d4-a3df-88022bbbecb7.png),  [js-2](https://user-images.githubusercontent.com/95220937/192065388-7440c96b-039f-438c-b295-2e6503d510fe.png)

   * Accessiblity:
     * I confirmed that colours and font chosen are easy to read and accessible by running it through lighthouse
     in devtools.
     * Generated report is here below
     ![Home-desktop](https://user-images.githubusercontent.com/95220937/193547647-6375387e-d9c7-414e-8651-73532adf5f3b.png)  

     * Desktop:
       * [Add-post-desktop](https://user-images.githubusercontent.com/95220937/193548464-2ab749e2-6fba-46d9-b206-fdbb10feb130.png), [Add-category-desktop](https://user-images.githubusercontent.com/95220937/193548699-162ae308-b06c-49c0-877f-fe9e646d05b2.png), [Sign-out-desktop](https://user-images.githubusercontent.com/95220937/193548843-2de0d226-ea86-4d9e-b7a5-5d9a03ec132b.png), [Category-postblog-desktop](https://user-images.githubusercontent.com/95220937/193549013-4fbce616-60e5-4193-972b-631e0a54a493.png), [edit-post-desktop](https://user-images.githubusercontent.com/95220937/193549189-6a14784d-a78e-4e51-98e6-10fc714aa09b.png), [delete-post-desktop](https://user-images.githubusercontent.com/95220937/193549358-8a4d3f49-5fb3-4bc2-93eb-f9831cfe35ec.png), [Sign-up-desktop](https://user-images.githubusercontent.com/95220937/193549595-20bcb4b6-225e-4276-9f85-863a4c296007.png), [Login-desktop](https://user-images.githubusercontent.com/95220937/193549756-9113c788-bd68-4e40-ad0b-bf457cb4dab0.png)


     * Mobile:
       * [Home-mobile](https://user-images.githubusercontent.com/95220937/193547654-31056df9-b43f-4b62-b7b3-b4365163a077.png), [Add-post-mobile](https://user-images.githubusercontent.com/95220937/193548457-afe94076-bb96-44fd-8a3c-01669584de62.png), [Add-category-mobile](https://user-images.githubusercontent.com/95220937/193548692-acd0e832-4a5c-4d89-80de-9770f9b68365.png), [Sign-out-mobile](https://user-images.githubusercontent.com/95220937/193548841-03e3be4f-2acb-438b-8366-44e47a92de85.png), [Category-postblog-mobile](https://user-images.githubusercontent.com/95220937/193549009-44d4a05d-41ef-40e1-9282-a469c31fd2bf.png), [edit-post-mobile](https://user-images.githubusercontent.com/95220937/193549186-64348763-2343-4fa0-9e84-5465829f120e.png), [delete-post-mobile](https://user-images.githubusercontent.com/95220937/193549361-f848387e-fb66-46b6-99ae-e86956762365.png), [Sign-up-mobile](https://user-images.githubusercontent.com/95220937/193549597-193411d7-aa47-4855-b174-482fb5ca2971.png), [Login-mobile](https://user-images.githubusercontent.com/95220937/193549751-51ed8daa-9ffc-432c-bdcd-7b248f68e945.png)

   [Back to top](#)

# Bugs:
 ## Fixed bugs:
  * While creating the project I faced the bug of relation does not exist error, which actually took a lot of my time to solve. It was actually the migrations error because I accidentally deleted some migrations in my project.
  * Steps I took to solve:
    * Firstly, I deleted all the migrations in my apps except __init__.py file
    * Then I deleted the db.sqlite3 file showing in the files
    * Because the database I was using connected with heroku so I had to reset the database in the heroku platform and also I deleted the heroku postgres and added the new one and also added the new DATABASE_URL in the env.py file 
    * Then I commented out the admin.py, forms.py, models.py, views.py, urls.py files and also one line in the urls of blogweb in which blog app was connected
    * Then I ran the command python3 manage.py makemigrations and python3 manage.py migrate
    * After that I uncommented the models.py file and ran the commands python3 manage.py makemigrations blog and python3 manage.py migrate blog for my models
    * And finally I uncommented all the files which I commented out before and ran the server using the command python3 manage.py runserver and the bug was fixed in this way.

 ## Unfixed Bugs:
   * No unfixed bugs.
   
   [Back to top](#)

# Deployment:
 This project was deployed using the code institute's mock terminal for heroku. Following steps were taken for the deployment of the project:
  * Login to Heroku and Create a New App
  * Give the App a name, it must be unique and select a region closest to you
  * Click on 'Create App' and now you can see the project dashboard
  * Click on the 'Resources' tab and search for 'Heroku Postgres' as this is the add-on you will use for the deployed database
  * Click on the 'Settings' tab at the top of the page.
  * Scroll down to 'Config Vars' and click 'Reveal Config Vars'. Here the database URL is stored, it is the connection to the database, so this must be copied and stored within env.py as a root level file. The env.py file is where the project secret environment variables are stored. This file is then added to a .gitignore file so it isn't stored publicly within the project repository.
  * The secret key needs to be created within the projects env.py file on GitPod and then added to the Config Vars on Heroku. Once added, go to the settings.py file on GitPod.
  * Within the settings.py file you need to import several libraries:
    * import os
    * import dj_database_url
    * from django.contrib.messages import constants as messages
    * if os.path.isfile('env.py'):
      * import env
  * Then, we need to replace the current insecure secret key with os.environ.get('SECRET_KEY)', that we set within the env.py file.
  * Once the secret key is replaced, scroll down to DATABASES to connect to the Postgres database. Comment out the current databases and add the following:
    * DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }
  * The next step is to connect the project to WhiteNoise, which is where the static files will be stored. You can find a full explanation of how to install WhiteNoise [here](https://whitenoise.evans.io/en/stable/)
  * Then on Heroku add to the Config Vars, DISABLE_COLLECTSTATIC = 1, as a temporary measure to enable deployment without any static files, this will be removed when it is time to deploy the full project.
  * Next we need to tell Django where to store the media and static files. Towards the bottom of settings.py file we can add:
    * STATIC_URL = '/static/'
    * STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    * STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    * MEDIA_URL = '/media/'
  * Then we need to tell Django where the templates will be stored. At the top of settings.py, under BASE_DIR (the base directory), add a templates directory and then scroll down to TEMPLATES and add the templates directory variable to 'DIRS': [].
  * Now we have to add our Heroku Host Name into allowed hosts in settings.py file:
    * ALLOWED_HOSTS = ['YOUR-APP-NAME-HERE', 'localhost']
  * Finally, to complete the first deployment set up of the skeleton app, create a Procfile so that Heroku knows how to run the project. Within this file add the following: web: gunicorn APP-NAME.wsgi Web tells Heroku to allow web traffic, whilst gunicorn is the server installed earlier, a web services gateway interface server (wsgi). This is a standard that allows Python services to integrate with web servers.
  * Now go to the 'Deploy' Tab on Heroku. Find the 'Deployment Method' section and choose GitHub. Connect to your GitHub account and find the repo you want to deploy.
  * Scroll down to the Automatic and Manual Deploys sections. Click 'Deploy Branch' in the Manual Deploy section and waited as Heroku installed all dependencies and deployed the code.
  * Once the project is finished deploying, click 'Open App' to see the newly deployed project.
  * Before deploying the final draft of your project you must:
    * Remove DISABLE_COLLECTSTATIC=1 from congifvars within Heroku
    * Ensure DEBUG is set to false in settings.py file


  [Back to top](#)
# Credits:
 ## Content:
   * The Idea of README.md file and the codes used for the website were also learnt from [Code Institute](https://codeinstitute.net)
   * Few codes were also learnt from [Codemy.com](https://codemy.com/)
   * Few codes were taken from [Stack Overflow](https://stackoverflow.com/)

 ## Acknowledgements:
   * My mentor who guided me througout the project.

 [Back to top](#)