# futchamp

To start running the app, do the following:

First install the latest python 3.6 version

Install pip
    sudo apt install python-pip -y

Install virtualenv
    pip install virtualenv

Create the virtualenv folder
    python -m venv venv

Activate virtualenv
    run the script called "activate" inside the \venv\Scripts folder

install requirements
    pip install -r requirements.txt

Set the environment
    for the test environment (the one that uses a sqlite file on your machine): python constants.py set_constants test
    for the dev environment (the one that uses postgres on heroku server): python constants.py set_constants dev

Run
    python manage.py run


for simple usage check the Makefile
