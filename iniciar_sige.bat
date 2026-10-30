@echo off

cd /d C:\Users\Van\projetoSIGE

call venv\Scripts\activate

start http://127.0.0.1:8000

python manage.py runserver