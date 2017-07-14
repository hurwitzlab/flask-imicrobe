export IMICROBE_FLASK_CONFIG=testing
export IMICROBE_DB_URI=sqlite:///test.db

python manage.py build_tables
python manage.py runserver
