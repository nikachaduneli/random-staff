# carrefour Applicants

Install required packages with:
    'pip install -r requirements.txt'

For database connection open carrefour/setting.py file, look for 'DATABASES' and change existing parametres.
Django can not create database itself so create database and then change parameters.

After changing database parameters run this commands to prepare database:      
    'python3 manage.py makemigrations'
    'python3 manage.py migrate'

To create admin user run this command:
    'python3 manage.py createsuperuser'

Run this command to collect all needed static files:
    'python3 manage.py collectstatic'

Before deploing in production in carrefour/setting.py find 'ALLOWED_HOSTS' and change 'localhost' with server domain name. 
Also find 'SECRET_KEY' and create environment variable with its value, then uncomment the line bellow, 
after testing if everything's working as it should, you can delete old line.

To test server run:
    'python3 manage.py runserver'

