import json
from flask import Flask, render_template, jsonify, request, redirect
import requests
from requests.structures import CaseInsensitiveDict
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime 
import pytz
import os
app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])
def ipn():
    if request.method == 'POST':
        content = request.get_json()
        amount = str(content["data"]["amount"])
        user = content["data"]["tx_ref"]
        txid = content["data"]["flw_ref"]
        app_fee = content["data"]["app_fee"]
        print(content)
        data = '{ "amount": "'+str(amount)+'", "fee": "'+str(app_fee)+'", "user_id": "'+str(user)+'", "txid": "'+str(txid)+'"}'
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"
        resp = requests.post("https://api.telebotcreator.com/new-webhook?bot_id=4282074&for=1350180828&access_token=oMP8rbxG&command=/getNariaDeposit", headers=headers, data=data)
        requests.get(f"https://api.telegram.org/bot5261738411:AAHp2-zORf8QYZ3i_vBksIN9hdjNB06CSQw/sendMessage?chat_id=-1001757222480&text={requests.utils.quote(str(content))}").content
        return 'Successful'
    else:
        return ("This")
