# 4chan imports
import requests
import json
from pprint import pprint
from datetime import datetime as dt
import re

# Flask page setup
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

# This stores a given board endpoint data in json form to the r variable
# In this case we are storing /biz/ data
dump = requests.get('https://a.4cdn.org/biz/catalog.json')
dump = dump.json()

#--------------------------Extracts all comments from /biz/ and stores them------------------------------#
for page in dump:
    for comment in page['threads']:
        try:
            commentsub = re.sub('<[^<]+?>', ' ', comment['sub'])
            print(re.sub(r'http\S+', '', re.sub(r'[0-9]+', '', re.sub('&[^>]+;','',commentsub))))
            print('')
        except KeyError:
            pass
        try:
            comment3 = re.sub('<[^<]+?>', ' ', comment['com'])
            print(re.sub(r'http\S+', '', re.sub(r'[0-9]+', '', re.sub('&[^>]+;','',comment3))))
            print('')
        except KeyError:
            pass
        try:
            for reply in comment['last_replies']:
                try:
                    reply = re.sub('<[^<]+?>', ' ', reply['com'])
                    print(re.sub(r'http\S+', '', re.sub(r'[0-9]+', '', re.sub('&[^>]+;','',reply))))
                    print('')
                except KeyError:
                    pass
        except KeyError:
            pass
#--------------------------------------------------------------------------------------------------------#
