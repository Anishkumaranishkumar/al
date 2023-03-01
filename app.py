from flask import Flask, render_template
import requests
r = requests.get('https://google.com/').text

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return r                             
if __name__=='__main__':         
 app.run(host="::" ,port='2222') 
