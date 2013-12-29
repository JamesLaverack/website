from flask import Flask
from james_laverack import james_laverack

app = Flask(__name__)
app.register_blueprint(james_laverack)

if __name__ == '__main__':
    app.debug = True
    app.run()
