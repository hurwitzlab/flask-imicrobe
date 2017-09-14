export IMICROBE_FLASK_CONFIG=testing
export IMICROBE_DB_URI=sqlite:///test.db

# __pycache__ may cause trouble when tests/imicrobe is a VM shared directory
rm -rf tests/imicrobe/__pycache__
python manage.py runserver -D > tests/testing_server_output.log 2> tests/testing_server_error.log &
python manage.py test
kill $!
