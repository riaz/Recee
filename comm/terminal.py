from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post', methods = ['GET','POST'])
def post():
    # Get the parsed contents of the form data
    json = request.json
    print json
    # Render template
    return "Hello"

if __name__ == '__main__':
    app.run()
