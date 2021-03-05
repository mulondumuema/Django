Steps fro creating a django application:
1. django-admin startproject project name => start the project
2. cd project_name
3. python manage.py startapp application_name => start the app

Django project structure:
when you startproject ir creates a folder with the required files to run the app. The folder has an inner folder too with the same name. that is:

project_name
    project_name
        __init__.py
        urls.py
        settings.py
        asgi.py
        wsgi.py
    applicatio_name
        __init__.py
        views.py
        admin.py
        apps.py
        tests.py
    manage.py

you will always run the python manage.py startproject commnd while in the outer project_name directory (the one that has manage.py file)

we can have as many apps as we want inside the python project

the models.py help to relate to the database

in views.py we describe what is displayed to the user and how it should be displayed

Django follows MVT architecture, different from other backend frameworks which use MVC architecture

MVT:
M: models : Data : Database
V: View : Business logic
T: Template : Presentation Logic

in apps.py you register the apps
in test.py you test you write tests for the application

when you run python anage.py runserver for the first time it displays the start default page on the browser with the url: http://localhost:8000

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

