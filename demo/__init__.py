from flask import Flask, session, g, render_template
from flask import Flask
from flaskext.mail import Mail
from flaskext.exceptional import Exceptional

app = Flask(__name__)

app = Flask(__name__)
app.config.from_object('config')
exceptional = Exceptional(app)
mail = Mail(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from demo.views import main
app.register_blueprint(main.mod)

