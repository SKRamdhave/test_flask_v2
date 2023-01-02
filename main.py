"""
render_template() --> To execute the specified html file code
abort()  -->  To change the status code of request and provide status code as parameter
                e.g :: abort(404)
"""

from flask import Flask, render_template, abort
from models.dal import db

app = Flask(__name__)



@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]      # db = List  & card = dictionary
        return render_template("card.html", card=card, index=index)

    except IndexError:
        abort(404)




# Output Examples ::
#     1. http://127.0.0.1:5000/
#     2. http://127.0.0.1:5000/card/1
#     3. http://127.0.0.1:5000/card/2 ...