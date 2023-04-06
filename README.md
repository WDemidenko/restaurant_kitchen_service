# Restaurant project

Django project for interaction between cooks, adding new dishes and types of dishes, to improve restaurant service

## Check it out

[Restaurant project deployed to Render](https://restaurant-kitchen-service-tuz3.onrender.com/)

You can log in as a test user to use the website:
* login: test_user
* password: 1234test

## Installation

Python3 must be installed

```shell
git clone https://github.com/WDemidenko/restaurant_kitchen_service
cd restaurant_kitchen_service
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver #starts Django server
```
The following environmental variables are used in the project:

* DJANGO_SECRET_KEY: This variable stores the secret key used by Django to sign cookies and other security features. 

* DATABASE_URL: This variable is used to configure the database connection in the project. 

* RENDER: If this variable is set in the environment, the project will run in production mode. If it is not set, the project will run in debug mode.

To set variable in your environment write in the console for example:
```
export DJANGO_SECRET_KEY="your_secret_key"
```

## Features

This project makes it easy to:
* Authentication for cooks and store or change information about them
* Create, update, delete dish types and dishes in your kitchen database 
* Allows for cooks to specify, cooks which are responsible for every dishes cooking.
* Convenient search at dish list or dish types list
* Informative list of cooks, with up-to-date information on the number of dishes that each of them is preparing at the moment
* Information about the amount of ingredients is used, and the possibility to add or remove them from the dish


## Demo
![Website Dish_Type details](demo_dish_details.jpg)
![Website Cook list](demo_cooks_list.png)
![Website Cook details](demo_cook_details.png)
