# imicrobe-admin-console
A Flask-Admin interface to the iMicrobe database.

## Requirements
A Python 3.6+ interpreter is required. Please use a virtual environment. For example:

```
$ python3.6 -m venv ~/venv/flim
$ source ~/venv/flim/bin/activate
(flim) $
```

The following environment variables must be defined:

  + IMICROBE_DB_URI=mysql+pymysql://imicrobe:{password}@127.0.0.1/imicrobe
  + IMICROBE_FLASK_CONFIG=production
  + IMICROBE_ADMIN_CONSOLE_UN=imicrobe-admin
  + IMICROBE_ADMIN_CONSOLE_PW={random strings are best}
  + IMICROBE_ADMIN_CONSOLE_SESSION_SECRET_KEY={a UUID is a good choice}

## Install
Download or clone the repository and install with `pip`. The ORM classes must be generated by the `write_models.py` script. For example:
```
(flim) $ git clone <this repository>
(flim) $ cd imicrobe-admin-console
(flim) $ pip install -r requirements.txt
(flim) $ python write_models.py
```

## Run
```
(flim) $ python manage.py runserver --port 5000 --host 0.0.0.0
```
