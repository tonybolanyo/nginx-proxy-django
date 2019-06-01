virtualenv env
source env/bin/activate
pip install django
pip install djangorestframework
django-admin startproject catalog
cd catalog
python manage.py startapp products
cd ..
django-admin startproject billing
cd billing
python manage.py startapp invoices
