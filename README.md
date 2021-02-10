# Getting started with Django

### 1. Install Django ###

a). Check if python and pip are installed

Django is a python webframework. To install it, based on the version you need python and pip already installed.

Pip is a package management system that simplifies installation and management of software packages written in Python such as those found in the Python Package Index (PyPI).

To check python3 version installed, run on the terminal:

`$ python3 --version`

If not installed, you can install python 3.6 with:

`$ sudo apt-get update`

`$ sudo apt-get install python3.6`
 
To install pip for python3. run:

`$ sudo apt update`

`$ sudo apt install python3-pip`
 
To check pip version:

`$ pip3 --version`

b). Create a virtual environment

The most convenient way to install Django is by using a virtual environment, which is a feature built into Python that allows you to keep a separate directory of installed packages for each of your projects so that they don’t interfere with each other.

If the python3-venv package is not installed install it with the following command.

`$ sudo apt-get install python3-venv`

It’s a good idea to keep all your virtual environments in one place, for example in **.virtualenvs/** in your home directory.

Create a new virtual environment by running:

`$ python3 -m venv ~/.virtualenvs/djangodev`

The path is where the new environment will be saved on your computer.

Then activate the virtual environment:

`$ source ~/.virtualenvs/djangodev/bin/activate`

Note: You have to activate the virtual environment whenever you open a new terminal

c). Install Django

After you’ve created and activated a virtual environment, enter the command::

`$ python -m pip install Django`

Check if Django is installed:

`$ python -m django --version`

### 2. Create a project ###

This is based on this [tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

a. cd into the directory you would like to store your code
b. if it is your first time using Django, will do initial setup, that is, autogenerate some code that established a Django project
 A Django project is a collection of settings for and instance of Django specific options and application-specific settings
 In the directory run:
 
 `$ django-admin startproject mysite`
 
 This will create **mysite** directory in your current directory
 
 What **startup project** created:
 
 `mysite/
    manage.py
    mysite/
      _init_.py
      settings.py
      urls.py
      usgi.py
      wsgi.py`
      
  These files are:
  - The outer **mysite/** root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
  - **manage.py**: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
  - The inner **mysite/** directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
  - **mysite/__init__.py**: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
  - **mysite/settings.py**: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
  - **mysite/urls.py**: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
  - **mysite/asgi.py**: An entry-point for ASGI-compatible web servers to serve your project.
  - **mysite/wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project. 
  
 Note: all these should be done in the virtual environment that you installed Django
 
#### The development server ####

change into the outher mysite directory and run:

`$ python manage.py runserver`

This starts a server on port 8000

The Django development server is a lightweight web server written purely in python. This has been included in Django so that you can develop things rapidly without having deal with configuring a production server like Apache until you are ready for production.

#### Creating the polls app ####

Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

`**Project vs apps**

an app is a web application that does something e.g a weblog system, a database of public records or a poll app.
a project is a collection of configuration and apps for a particular website.
a project can contain multiple apps
an app can be in multiple projects`

To create the polls app, make sure you are in the same directory as manage.py and type this command:

`$ python manage.py startapp polls`

This will create a directory polls like this:

`polls/
   _init_.py
   admin.py
   apps.py
   migrations/
     _init_.py
     admin.py
     migrations/
       _init_.py
     models.py
     tests.py
     views.py`

This directory structure will house the poll application.

a) writing the first veiw 

in django a view is a python function that takes a web request and returns a web response.

follow the [tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) to create the view

b) database setup

some applications in django (defined in INSTALLED_APPS section in settings.py) make use of atleast one databse table though so we need to create the tables in the database before we can use them. To do that, run:

`$ python manage.py migrate`

c) creating models

a model contains the essential fields and behaviours of the data you are storing
django follows the **dry principle:** the goal is to define your data model in one place and automatically derive things from it.


To use the app here, clone the repo, cd into the mysite directory, activate the environment with django then you can run the development server. Have fun! 


# Or

create the virtual environment:

cd to your directory

create tenant_env virtual environment

```virtualenv -p python3 tenant_env```

activate the environment

```source tenant_env/bin/activate```

install required packages

```pip3 install django django-tenants psycopg2-binary pillow```

start a django project

```django-admin startproject tenants_trial```

# About Django

at its core django is pyhton framework  for taking incoming HTTP requests and returning HTTP responses. What happens in between is up to you.

## Building a simple django app

we will start by using a single *hello.py* file

this file will contain all the code needed to run our django project

in order to have a full working project we will need to create a view to serve the root URL and the necessary settings to configure the Django environment.

## creating the view

Django is referres to as a *model-template-view* (MTV) framework.

the view portion inspects the incoming HTTP request and queries, or constructs the necessary data to send to the presentation layer

## the URL patterns

in order to tie our view into the site's structure, we will need to associate it with a URL pattern

django associates views with their URL by pairing a regular expression to match the URL and any callable argument to the view

## the settings

django settings detail everything from database and cache connections to internationalization features and static and uploaded resources

the full hello.py looks like this:

```
import sys
from django.conf import settings
settings.configure(
 DEBUG=True,
 SECRET_KEY='thisisthesecretkey',
 ROOT_URLCONF=__name__,
 MIDDLEWARE_CLASSES=(
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 ),
)
from django.conf.urls import url
from django.http import HttpResponse
def index(request):
 return HttpResponse('Hello World')
urlpatterns = (
 url(r'^$', index),
)
if __name__ == "__main__":
 from django.core.management import execute_from_command_line
 execute_from_command_line(sys.argv)
```
you can start the example in the command line:

``` python hello.py runserver ```

Note: You should be in a virtual environment where django is installed.

## improvements

the example shows some fundamental pieces of the django framework: writing views, creating settings and rum=nning management commands.

django also provides additional utilities for common tasks invoved in handling HTTP requests, such as rendering HTML, parsing form data, and persisting session state.

it is important to understand how these features can be used in your application in a lightweight manner. By doing so you gain a better understanding of the overall django the overall django framework and true capabilities.

## wsgi  application

currently our "Hello World" project runs through the runserver command. This is a simple server based on the socket server in the standard library. It has helpful utilities for local development such as auto-code reloading. While convenient for local development, runserver is not appropriate for production deployment security.

The Web Server Gateway Interface (WSGI) is the specification for how web servers communicate with application frameworks like django

There are various web servers that speak WSGI like Apache, Gunicorn, CherryPy, etc.

each of these servers needs a properly defines WSGI application to be used. Django has an easy interface for creating this application through *get_wsgi_application*

this would normally be in the *wsgi.py* file created by the startproject command.

for this case therefore will use gunicorn

## reusable template

it isn't difficult to transform this file into a reusable template to start future projects ucing the same base layout
