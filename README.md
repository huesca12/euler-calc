# euler-calc

calculator
1. complex plane
2. polar coordinates
3. 2D and 3D cartesian

## How to test the Django project locally

With python installed in your terminal and in the root repository directory run:
```Bash
python manage.py runserver
```

## How to add your own app to the project

Each Django project consists of several apps that are each structured as a Python package.

With python installed in your terminal and in the root repository directory run:
```Bash
python manage.py startapp <app name>
```

## How to appease the heroku database migration demon

After deploying a version of euler-calc with new migrations for an app run:
```Bash
heroku run python manage.py migrate --app euler-calc
```

## Stuff to note

max_length is set to 130 characters on the request model
