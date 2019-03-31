from flask import render_template, Blueprint

home_page = Blueprint(__name__, 'home_page', template_folder='app/templates')

@home_page.route('/')
def get():
    return render_template('index.html')
