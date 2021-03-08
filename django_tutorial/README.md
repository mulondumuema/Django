Steps fro creating a django application:
1. django-admin startproject project name => start the project
2. cd project_name
3. python manage.py startapp application_name => start the app

Django project structure:
when you startproject it creates a folder with the required files to run the app. The folder has an inner folder too with the same name. that is:

project_name
    project_name
        __init__.py
        urls.py
        settings.py
        asgi.py
        wsgi.py
    application_name
        __init__.py
        views.py
        admin.py
        apps.py
        tests.py
    manage.py

you will always run the python manage.py startapp command while in the outer project_name directory (the one that has manage.py file)

we can have as many apps as we want inside the python project

the models.py help to relate to the database

in views.py we describe what is displayed to the user and how it should be displayed

Django follows MVT architecture, different from other backend frameworks which use MVC(C for controller) architecture

MVT:
M: models : Data : Database
V: View : Business logic
T: Template : Presentation Logic

in apps.py you register the apps
in test.py you test you write tests for the application

when you run python manage.py runserver for the first time it displays the start default page on the browser with the url: http://localhost:8000

8000 is the port number

Views
a view is a place where we put the logic of our application
types of views available:
- function based views
- class based views

a view function or 'view'is a python function that takes a web request and returns a web response

NB: you use a view to create web pages. there4 u need to associate a view to a URL to see it as a webpage

urls.py: configure url patterns related to our views

when a user sends a request(url), it goes to the view then the view sends bach the response

therefore we have:
application : views.py
project : urls.py : url patterns related to views

types of resposes:
html
images
video files
redirected
xml
json

we will see how to:
-configure views at project level
- configure views at application level

Steps to create Django Proect and develop views

1. Create project using following command

$ django-admin startproject project_name

$ django-admin startproject fourth_project

2. create appication

$ cd project_name

$ cd fourth_project

$ python manage.py startapp testapp1

3. Define views inside views.py

4. configure url patterns for our views inside urls.py either at project level or at application level

5. start server

6. open browser and send request, i.e url

if you just want to call the various application views in the project, import them with as then use dot notation

e.g:
from testapp1 import views as v1
from testapp2 import views as v2

urlspattern = [
    ..... // admin
    path('home/', v1.homePageView)
]

the best way to define views is to create urls.py files in the app folder then include them to the project urls.py

Class Based Views
- Class based generic views are advanced set on built-in views which are used for implementation of selective views strategies such as Create, Retrieve, Update, Delete

- class based views simplify the use of separating GET, POST requests for a view

They do not replace function based views but have certain differences and advantages when compared to function-based views i.e:
   - organization of code related to specific HTTP methods (GET, POST) instead of conditional branching like in function views
   - Object oriented techniquessuch as mixins (multiple inheritance) can be used to factor code into reusable components

will create a form that a a new user can register and the data to be added in a database

the form will have:

- first name:
- last name:
- city :
- email :

- register button

so will create a class in the models.py  i.e class Registration(models.Model) then register the class in the admin in the admin.py.

the registration class will have the data from the form then add it to the database therefore to add it to the database we will add the app in the settings.py then run:

python manage.py makemigrations
python manage.py migrate

then will create a super user to access the admin:

python manage.py createsuperuser

then will create one ui to access/ see all the registratione => List v
View

Detail View gives for particular is

Update view updated existing data e.g change email

Delete view => when you want to delete a specific data

will use django forms and templates for all these

Create View
create view refers to a view(logic) to create an instance of a table in the database
class based vies automatically setup everything. one just needs to specify which model to create view for and the fields
then class based createView will automatically try to find a template in templates/appname/modelname_form.html

note: you have to specify the templates in the settings.py

Working with template files
it is never recommended to place html files inside views.py because views.py is a python file and we should only place python related code

a template file is a html file which represents presentation logic

presentation logic is the logic responsible to display user interface to the end user

we create a templates 

structure

fifth_project
  fifth_project - do modifivations to tell django that we have the html files in  the templates folder
  manage.py
  templates
    testapp1 - will have .html files
    testapp2 - .html

it is easy to maintain code when working with templates

Working with static files
this means working with external style sheets, images and javascript files

we need to do modifications in settings.py file to work with static files

static files may be available in form of:
- css : external styles, third party styles
- javascript : external javascript
- images

create the sixth project and start testapp1 & testapp2

structure:

sixth_project
  sixth_project
  manage.py
  templates
    testapp1
      *.html
  static
    css => .css
    js => .js
    images => .jpg

 
{% %} : jinja2 template - this is what allows us to work with static files


flow of content

http://localhost:8000/home => urls.py => views.py => template file (static content, dynamic content)

syntax to define template tags or dynamic data:
{{ key }}

the key and its value is defined in a dictionary in views.py

create seventh_project with testapp1

structure:

seventh_project
  seventh_project
  manage.py
  templates
   testapp1 => *.html
  static
    css
    images
    js


Django Template Language
A django template language is designes to strike a balance between power and ease. It's designed to feel comfortable to those used to working with HTML

Built-in-template tags and filters

Tags
- Tags look like {% %}
they are more complex than variables
- some create text in the output, some control flow by performing loops or logic and some load external information into the template to be used by later variables
-some tags require beginning and ending tags i.e:
{% tag %} ... tag contents ... {% endtag %}

for 
- loop over eac item in an array, making the item available in a context variable

{% for obj in list %}

- you can loop over a list in reverse by using

{% for obj in list reversed %}

for ...empty

- the for tag take an optional {% empty %} clause whose text is displayed if the given array is empty or could not be found

if
the {% if %} tag evaluates a variable and if that variable is true the contents pf the block are output

block
defines a block that can be overriden by child templates

structure

testpro1
  testproj1
  manage.py
  testapp2
  static
    css
    js
    images
  templates
    testapp1

then add te templates and static paths in the settings.py file

Admin Interface
for each project django will provide some built-in apps behind the scenes which are responsible to perform various operations on our project like database operations, authentication, session management, etc

in order to make use of these apps in our project we need to use the following command:

$ python manage.py migrate

once we execute above command all built-in and user-defined apps will be installed

and we canstart working with admin interface

to work with admin interface first we need to create super user using the following command:

python manage.py createsuperuser

on executing the above command we need to enter username, password and email

open browser window and use the following command to access admin interface

http://localhost:8000/admin