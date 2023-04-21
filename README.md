# Django CRM Website (Beginner Project)

### [View Live Project](http://kalyanvelu.pythonanywhere.com/record/1)

## Tech Stack

This project uses:
 - **Django** python web framework
 - **MySQL** for Database

## Set up a django project from sctrach

1. **Creating a virtual environment**:

To create a Virtual Envionment

```bash
# install virtualenv
pip install virtualenv

# create a virtual env. with any name 
virtualenv environment_name

# activate virtual env
# for git bash/cmd
source environment_name/bin/activate

# deactivate
(virtualenv_name)$ deactivate
```
2. Install Dependencies

```bash
# install django to your v.env
pipenv install django

# to use mysql you have to install mysql
pipenv install mysql

# also install this
pip install mysql-python

# install mysql-connector
pip install mysql-connector

# if above doesn't work use this
pip install mysql-connector-python
```
3. Create a django app

```bash
django-admin startproject dcrm
```
4. Create a app named website
```bash
python manage.py startapp website
```
5. Install `autopep8` to auto format Python code.

```bash
pip install -U autopep8
```
6. Create a `mydb.py` file to create a database.

```python
import mysql.connector

dataBase=mysql.connector.connect(
    host=<your_hostname>,
    user=<database_username>,
    passwd=<database_password>
)

#prepare cursor object

cursorObject=dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE  <DATABASE_NAME>")

print ("All Done")
```
7. Execute this file using `python mydb.py`.
8. Then create a superuser to login to django site as admin.
```bash
winpty python manage.py createsuperuser
```
9. Make changes to your site and run your server `python manage.py runserver`.

## Points to be noted:
1. After creating a table you have to migrate it to make changes in your server.
```bash
python manage.py makemigrations
python manage.py migrate
```

## Deploying A Django Site to [Python Anywhere](https://www.pythonanywhere.com/)

You can deploy only one free website as a begineer in [Python Anywhere](https://www.pythonanywhere.com/).

### Steps:

1. Login or Signup.
2. Then you should be able to access the `Dashboard` .[here](https://www.pythonanywhere.com).
   >Make sure you have a github repository of your project to deploy.
3. In the dashboard you should see a console tab. Click on `$ bash`, it will open a console.

On the console type `pwd` to make sure you are here `/home/<your_username>`

```bash
pwd
```

 - Then clone your github repository
```bash
git clone https://github.com/<your_github_username>/<your_Reposity_name>
```
 - In pythonAnywhere, We need to create a virtual environment.
```bash
# use any python version >=3.10
mkvirtualenv --python=/usr/bin/python3.9
```
 - Then install your dependencies.
```bash
# insatll django
pip install django
# syntax
pip install <dependency_name>
```
4. Open `Web` Tab.
 - Click on add a new web app.
 - Then click next.
 - Then Select `Manual configuration` in python web framework. click next.
 - Select `Python Version`. We selected `3.9`. click next
 - `Manual Configuration` .Click next.
 - [Web App setup is done]
5. Then Scroll Down in `Web` tab in your app.
 - Navigate to `Virtualenv`.
 - There add your `virtual environment name`.
6. Then Scroll Up to `Code`.
 - Click on `WSGI configuration file`.
 - It will open a editor.
 - Edit and save the file with following code.
```python
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/kalyanvelu/django-crm/mysite/settings.py'
## and your manage.py is is at '/home/kalyanvelu/django-crm/manage.py'
path = '/home/kalyanvelu/django-crm'
if path not in sys.path:
    sys.path.append(path)
# also change this from mysite.setting to your folder where your setting exist
os.environ['DJANGO_SETTINGS_MODULE'] = 'dcrm.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```
 - you have to get the path of your application from your bash console in [Python Anywhere](https://www.pythonanywhere.com/)

