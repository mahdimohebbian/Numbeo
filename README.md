# Numbeo

A web scraping project to retrieve cost of living data from https://www.numbeo.com website.


## Installation
* It's better to make a virtual environment
* Install required packages with command
    * ```$ install pip install -r requirements.txt```
* create .env file in the root of the project with this command ```$ vim .env``` then write your database information such as:

    * SECRET_KEY= 'my_django_secret_key'
    * DEBUG = 'True or False'
    * ALLOWED_HOSTS = 127.0.0.1, 192.168.1.1
    * DB_NAME= 'my_database'
    * DB_USER = 'my_username'
    * DB_PASSWORD = 'my_password'
    * DB_HOST = localhost
    * DB_PORT = 5432