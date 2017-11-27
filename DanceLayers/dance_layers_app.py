from flask import Flask, render_template
from dance_layers import get_parts
import json
from copy import copy


app = Flask(__name__)
ELEMENTS_FILE = "/home/saoili/DanceLayers/DanceLayers/dance_elements.json"
START_WITH_FEET = True


def load_json():
    with open(ELEMENTS_FILE, 'r') as inputs:
        file_contents = inputs.read()
        return json.loads(file_contents)

dance_elements = load_json()


@app.route("/")
def index():
    first, second, third = get_parts(
        copy(dance_elements), START_WITH_FEET)
    return render_template(
        'index.html',
        first=first, second=second, third=third)
