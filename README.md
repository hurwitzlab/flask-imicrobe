# flask-imicrobe
A demonstration iMicrobe app server built with Flask.

## Install

  1. clone this repository
  2. add this line to the imicrobe-vm Vagrantfile to forward port 5000 on the host to the imicrobe-vm:
      `config.vm.network "forwarded_port", host: 5000, guest: 5000`
  3. add a line such as this to the imicrobe-vm Vagrantfile to mount the flask-imicrobe directory inside the vm:
      `config.vm.synced_folder "/Users/jlynch/project/imicrobe/flask-imicrobe", "/flask-imicrobe"`
  4. start the imicrobe-vm with `vagrant up`
  5. ssh into the imicrobe-vm with `vagrant ssh`
  6. define the following environment variables:
      ```
      export IMICROBE_FLASK_CONFIG=development
      export IMICROBE_DB_URI=mysql+pymysql://imicrobe:<password>@127.0.0.1/imicrobe
      ```
  7. install Python 3.6:
      ```
      $ sudo yum -y update
      $ sudo yum -y install yum-utils
      $ sudo yum -y groupinstall development
      $ sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
      $ sudo yum -y install python36u python36u-pip python36u-devel
      ```
  8. create a virtual environment for the app server:
      ```
      $ python3.6 -m venv ~/venv/flim
      $ source ~/venv/flim/bin/activate
      (flim)$ pip install sqlalchemy pymysql flask flask-sqlalchemy flask-script
      ```
  9. run the development app server and allow connections from outside with `--host 0.0.0.0`:
      ```
      (flim)$ cd /flask-imicrobe
      (flim)$ python manage.py runserver --host 0.0.0.0
      ```
 10. visit http://localhost:5000/api/v1.0.0/project/ from a browser on the host system
