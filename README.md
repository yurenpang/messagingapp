# messagingapp
This app uses Django (MVC) and Python to create a messaging app.

### Introduction 

The app lets any visitor sign up for an account or sign into their account. Only a signed-in user can send messages to other registered users. 
A message can be saved as a draft and edited on before sending. This is a easy version of messenger. It mainly uses Python, Django framework, and Bulma on front-end.

### Prerequisites

Python 3.0+ and Django 2.0+

### Installing

<ul>
  <li> Clone this repo, open your terminal and direct to this folder
  <li> Create virtual environments
  
  ```
  # On macOS and Linux
  python3 -m pip install --user virtualenv
  source venv/bin/activate
  # On Windows
  py -3 -m pip install --user virtualenv
  venv\Scripts\activate
  ```
  
  <li>Make sure you have django 
  ```
  pip install django
  ```
  <li>Run the app
  ```
  python manage.py runserver
  ```
</ul>

