Installation
Install all required packages from requirements.txt

py -m venv env
env\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
pip install pillow
pip install xhtml2pdf
pip install django_jazzmin
