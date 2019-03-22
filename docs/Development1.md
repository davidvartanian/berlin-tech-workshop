# Development Process - Part 1

## Documentation
* https://www.django-rest-framework.org/
* https://www.anaconda.com/distribution/
* https://pipenv.readthedocs.io/en/latest/
* https://www.jetbrains.com/pycharm/download/
* https://www.getpostman.com/downloads/

## What is already done

### Boilerplate CLI Commands
1. Create a directory for your project: $`mkdir berlin-tech-workshop`
1. Create a Pipenv project: $`pipenv shell`
1. Install base packages: $`pipenv install django djangorestframework django-rest-knox`
1. Create Django project: $`django-admin startproject linkshortener`
1. Change to project directory: $`cd linkshortener`
1. Create Django app: $`python manage.py startapp shortener`

## Environment Preparation
1. Make sure you have Python 3.6+ installed ([download here](https://www.anaconda.com/distribution/))
1. Install Pipenv if you don't have it already ([download here](https://pipenv.readthedocs.io/en/latest/)): $`pip install pipenv`
1. Setup IDE ([download PyCharm Community here](https://www.jetbrains.com/pycharm/download/))
1. Install Postman ([download here](https://www.getpostman.com/downloads/))
1. Clone this project: $`git clone https://github.com/davidvartanian/berlin-tech-workshop.git`
1. Change to project directory: $`cd berlin-tech-workshop`
1. Run: $`pipenv install`

## App Configuration

### Add your app to the project
* find the file settings.py inside project directory
* find variable INSTALLED_APPS
* add your app name `shortener` and `rest_framework` to the list

## App Implementation

### Model Creation
* Find the file `shortener/models.py`
* Complete the implementation of the `Link` model class
* Run command: $`python manage.py makemigrations shortener`
* Run command: $`python manage.py migrate`

### Serializer Creation
* Find the file `shortener/serializers.py`
* Complete the implementation of the `LinkSerializer` serializer class

### API Creation
* Find the file `shortener/api.py`
* Complete the implementation of the `LinkViewSet` view set class
* Find the file `linkshortener/urls.py`
* Complete app router declaration
* Find the file `shortener/urls.py`
* Add endpoint URLs to app router

### Run it!
* Run $`python manage.py runserver`
* Browse `http://127.0.0.1:8000/api/links/`

### Add First Link
* Create a POST request in Postman
* Add URL `http://127.0.0.1:8000/api/links/`
* Add Body (raw, json): 
```json
{
    "name": "Some link name",
    "token": "unique-token",
    "url": "https://google.de"
}
```
* Click `Submit`
