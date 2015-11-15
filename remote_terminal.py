from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print 
    #lat = request.form['lat']
    #long = request.form['long']
    
    #return 'lat :' + lat
    return 'Hello'

if __name__ == '__main__':
    app.run()
