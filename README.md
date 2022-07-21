# django-views-function
<img src="https://github.com/wsvincent/awesome-django/raw/main/assets/django-logo.svg">
<ul>
<h2>Contents</h2>
<li><a href="#info"><h3>Info</h3></a>Information about the resources used in this project</li>
<li><a href="#automania"><h3>AUTOMANIA</h3></a>Website for booking screenings at the cinema</li>
<li><a href="#clone_project"><h3>Clone and Run a Django Project</h3></a>how run projects in your computer</li>
</ul>
<hr>

<center><h1>INFO</h1></center>
<h4>Information about the additional library, external Api used in this project and general information</h4>
<ul>
<li><strong>context_processors</strong><p>
in this application I use my own processor context to check unread message and show it to user wherever user is in website
</p></li>
<li><strong>django-dotenv</strong>
<p>using for hide SECRET_KEY from repositories
</p></li>
<li><strong>Views</strong>
<p>I write it with using functions views, it's my own personal choice for this particular application 
</p>
</li>
<li><strong>Tests</strong>
<p>i used django TestCase to testing my application</p>
<p> run test using command <code>python manage.py test automania</code> and <code>python manage.py test accounts</code></p> to test accounts app</li> </p></li>
</ul>
<hr>
<center><h1 id="automania">AUTOMANIA <span style='font-size:80px;'>&#128664;</span></h1></center>
<h3>website for the sale of cars and car parts</h3>
<p>You can see all offers but can't contact with seller without login in</p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/174436609-a5fcab77-c60e-493b-80dc-296586201284.png" width="350" >
</p>
<p>When you click 'watch car' you will see all information about car, of course sellers very often just lied about his car, be careful.
And the another one problem is too short descriptions but you have solution for this problem <span style="font-size:20px">⬇</span><br>
You can contact with seller with using message and got an answer.
 </p>

  <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/174436563-46972048-bbc1-4049-9fbc-9d8c2c3b5c10.png" width="350">
</p>
<p>When you receive the message you will be informed about it <span style="font-size:30px">&#9993;</span>.New message will have a red color<span style="font-size:30px; color:red">&#9993;</span>, when you press a text message, it will immediately change color</p> 
    <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/177140406-a50cda01-79d3-4b1e-bac0-8f910c1ee3d6.png" width="350">
    
</p>
<p>Your own posts you will have a user page, you can change it, or delete, in this page also you will have your orders which sent to the store exists there until the moment realization in that case you will be informed that you order in progress</p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/172058911-50fe82c8-4b25-419c-a3e4-f598cfd67ad1.png" width="350">
</p>
<p>You can leave opinion in this site, with stars <span style="font-size:20px">⭐</span>, but only login in user</p>
    <p align="center">
  <img src="https://user-images.githubusercontent.com/97242088/172058927-67b15e0e-1d8e-4f8a-9772-f255e59dc913.png" width="350">
</p>
  <hr>
<h3 id="clone_project">Clone and Run a Django Project</h3>

Before diving let’s look at the things we are required to install in our system.

To run Django prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source env/bin/activate`

Installing Django:-

`pip install django`

Now, we need to clone project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Install the project dependencies:

`pip install -r requirements.txt`

Now go to the setting.py and change the SECRET_KEY.
from
`SECRET_KEY = os.environ.get('SECRET_KEY')`
to
`SECRET_KEY = 'your own secret key'`

create admin account (**remember you must be at the main application folder with file manage.py, and do this steps for
each application in this repository!!!!**)

`python manage.py createsuperuser`

then

`python manage.py makemigrations`

then again run

`python manage.py migrate`


to start the development server

`python manage.py runserver`

and open localhost:8000 on your browser to view the app.

Have fun
<p style="font-size:100px">&#129409;</p>


