# BINCOM--DJANGO---Second-Stage
Election Results Web App - Easy Setup Guide
What This App Does
This is a simple web app that:

Shows election results for a single polling unit.
Shows total results for all polling units in a selected Local Government Area (LGA) in Delta State.
Lets you add results for a new polling unit.

What You Need

A computer with Python 3 installed (download from python.org if needed).
MySQL (a free database program; download from mysql.com).
The bincom_test.sql file (included in the project folder).
A web browser (like Chrome or Firefox).

Easy Setup Steps

Unzip the Project:

Unzip the election_results.zip file to a folder on your computer.


Set Up the Database:

Open MySQL (you’ll need your MySQL username and password).
Create a database by typing this in MySQL:CREATE DATABASE bincomphptest;


Load the data by running this in your computer’s command prompt or terminal:mysql -u yourusername -p bincomphptest < bincom_test.sql

Replace yourusername with your MySQL username. Enter your password when asked.


Update the Settings:

Open the file election_results/settings.py in a text editor (like Notepad).
Find the DATABASES section and update it with your MySQL username and password:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bincomphptest',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


Make sure results is in the INSTALLED_APPS list in the same file:INSTALLED_APPS = [
    ...
    'results',
]




Install Required Tools:

Open your command prompt or terminal and type:pip install django mysql-connector-python




Prepare the App:

In the command prompt, go to the election_results folder:cd path/to/election_results


Run these commands:python manage.py makemigrations
python manage.py migrate




Start the App:

Run this command:python manage.py runserver


Open your web browser and go to http://localhost:8000.



How to Use the App

View Polling Unit Results: Go to http://localhost:8000/polling_unit/8/ (replace 8 with any polling unit ID from the database).
View LGA Results: Go to http://localhost:8000/lga_results/, pick an LGA (like Aniocha North) from the dropdown, and see total results for Delta State.
Add a New Polling Unit: Go to http://localhost:8000/new_pol8/, fill in the form, and save.

Files in the Project

bincom_test.sql: The database file with election data.
election_results/urls.py: Sets up the main website links.
results/models.py, views.py, forms.py, urls.py: App logic.
results/templates/results/*.html: Web pages for the app.
This README.md: Instructions you’re reading now.

Notes

The app only shows LGAs in Delta State.
If you see errors, check your MySQL username/password or ensure bincom_test.sql is loaded.
