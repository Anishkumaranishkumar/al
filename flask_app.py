from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
     return render_template('Search.html')

@app.route('/Home')
def Home():
    return render_template('memes.html')
              
@app.route('/Search')
def Search(): 
    return render_template('Search.html')
            


if __name__=='__main__':
 app.run(host='127.0.0.1',port='5353')
                           
