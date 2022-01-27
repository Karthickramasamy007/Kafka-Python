from flask import Flask
import random_data as random
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    while 1==1:
        time.sleep(5)
        return random.get_registered_user()
        #return 'Hello, Docker'