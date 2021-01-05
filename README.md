# Getting started with Django

1. Install Django

a). Check if python and pip are installed

Django is a python webframework. To install it, based on the version you need python and pip already installed.

Pip is a package management system that simplifies installation and management of software packages written in Python such as those found in the Python Package Index (PyPI).

To check python3 version installed, run on the terminal:

`$ python3 --version`

If not installed, you can install python 3.6 with:

`$ sudo apt-get update
 $ sudo apt-get install python3.6`
 
To install pip for python3. run:

`$ sudo apt update
 $ sudo apt install python3-pip`
 
To check pip version:

`$ pip3 --version`

b). Create a virtual environment

The most convenient way to install Django is by using a virtual environment, which is a feature built into Python that allows you to keep a separate directory of installed packages for each of your projects so that they don’t interfere with each other.

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

2. Create a project

