from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)

@app.route('/tests/endpoint', methods=['POST'])
def get_bot_mission():
    input_json = request.get_json(force=True)
    print 'data from client:', input_json
    dictToReturn = {'answer':42}
    return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(debug=True)
