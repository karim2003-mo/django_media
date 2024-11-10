@echo off
cd E:\Naser Mansy\django_media\
call Scripts\activate
cd project
echo "http://127.0.0.1:8000/put_comment/"
python manage.py runserver
pause