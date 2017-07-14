export IMICROBE_FLASK_CONFIG=testing
export IMICROBE_DB_URI=sqlite:///test.db

python manage.py runserver -D > tests/testing_server_output.log 2> tests/testing_server_error.log &
python manage.py test
kill $!