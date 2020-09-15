
# Music Service 

## Basic Information

Appliaction for sharing music and texts of songs once.

### Project Structure

```bash
.
├── account
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── album
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── comment
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── playlist
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── rating
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── asgi.py
├── settings.py
├── urls.py
├── utils.py
└── wsgi.py
```

### Shell / Bash Files

#### ../packages.sh

This file have every python virtual environment requirements for application run

#### ../migrate.sh

This file migrate every models with database in app and generate UML

#### ../run.sh

This file running application

## UML

### Class Diagram

![class_diagram](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12abb353-ab91-4433-96d3-b5d9c5847254/de1x3ts-af1f9daf-1aad-439a-87e4-891ea7934b90.png/v1/fill/w_1280,h_1199,strp/music_service_class_diagram_by_00x097_de1x3ts-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD0xMTk5IiwicGF0aCI6IlwvZlwvMTJhYmIzNTMtYWI5MS00NDMzLTk2ZDMtYjVkOWM1ODQ3MjU0XC9kZTF4M3RzLWFmMWY5ZGFmLTFhYWQtNDM5YS04N2U0LTg5MWVhNzkzNGI5MC5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.MQ8Y8G1kYVZE4WzlAbs_iAx_8fztG-uhhTMvzVO6Ovw)

### Class Diagram By Apps

![class_diagram_by_apps](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12abb353-ab91-4433-96d3-b5d9c5847254/de1x3sf-d977ce0b-fca5-498c-84ce-f899375491ba.png/v1/fill/w_1280,h_811,q_80,strp/music_service_class_diagram_by_apps_by_00x097_de1x3sf-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD04MTEiLCJwYXRoIjoiXC9mXC8xMmFiYjM1My1hYjkxLTQ0MzMtOTZkMy1iNWQ5YzU4NDcyNTRcL2RlMXgzc2YtZDk3N2NlMGItZmNhNS00OThjLTg0Y2UtZjg5OTM3NTQ5MWJhLnBuZyIsIndpZHRoIjoiPD0xMjgwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.sJmLVbWBIkyd846m3I6vfYhQpdJiOzfe1KOSUKQBP9c)
