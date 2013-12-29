from flask import Blueprint, render_template

james_laverack = Blueprint('james_laverack',
                           __name__,
                           template_folder = 'templates',
                           static_folder = './static',
                           static_url_path = '/%s' % __name__)

@james_laverack.route('/')
def index():
    return render_template("index.html",
                           name = "James Laverack")
