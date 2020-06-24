# Teacher-Directory Django project

Install base dependencies:

```
pipenv install django==2.2
pipenv install pylint-django
pipenv install django-tastypie
```

## Local development
In the project folder "teacherdir" clone the project

## Admin Panel
Admin panel will add the user authentication and teacher profile.

```
http://127.0.0.1:8000/admin/

User Name: admin
Password: 123456
```

## Home Page
This will load the all Teacher are save in SQLite database.
Click the item to see the details of the teacher

```
http://127.0.0.1:8000/teacher/
```

## Rest API
This simple Rest APl will load all the teachers.
it can search by unique ID

```
http://127.0.0.1:8000/api/teacher/
http://127.0.0.1:8000/api/teacher/1
```

## RUn the project

```
python manage.py runserver
```

