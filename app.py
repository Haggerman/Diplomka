from flask import Flask, render_template
import requests
import json
import time
app = Flask(__name__)

@app.route("/")
def get_text():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    time.sleep(2.4)
    text_json = r.json()

    text = {
        'name': text_json[0]['name'],
        'abv': text_json[0]['abv'],
        'foodpair': text_json[0]['food_pairing'][0]
    }

    return render_template('index.html', text=text, name="CHleba")
