python manage.py makemigrations
python manage.py migrate
python manage.py graph_models -a -g -o class_diagram_by_apps.png
python manage.py graph_models -a -o class_diagram.png

# directory structure
# tree -I '.git|__pycache__|migrations|__init__.py'