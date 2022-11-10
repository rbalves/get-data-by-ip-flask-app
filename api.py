from flask import Flask, render_template
import ipinfo
import requests
import json


app = Flask(__name__)

@app.route("/")
def home():
    access_token = 'ee7d16a127c251'
    handler = ipinfo.getHandler(access_token)

    ip_address = json.loads(requests.get("https://ip.seeip.org/jsonip?").text)["ip"]

    details = handler.getDetails(ip_address)

    dados = {
        'ip': ip_address,
        'city': details.city,
        'country': details.country_name
    }

    return render_template('home.html', dados=dados)