find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

rm ./db.sqlite3

pip uninstall django
pip install django

python ./manage.py makemigrations worker
python ./manage.py migrate

python ./manage.py createsuperuser