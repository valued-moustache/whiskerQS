from . import SequelDAO
from flask import Flask
import re
from markupsafe import escape

app = Flask(__name__)

@app.route('/product_count/<item>')
def get_part_count(item):
    item_name = escape(item).strip()
    response = None
    if re.match('^[\w-]+$', item_name):
        response = SequelDAO.get_item_count(str(item_name))
        if response:
            return f'<p>Item: {response[0]}\n' \
                   f'Count: {response[1]}</p>'

    return "<p>Item not found</p>"

@app.route('/')
def index():
    print("Request For Index")
    return "<p> Welcome to the index. </p>"

def get_app() -> Flask:
    return app
