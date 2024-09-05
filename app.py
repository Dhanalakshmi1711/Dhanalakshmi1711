from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "succeedddd..."

@app.route('/api')
def api():
    return jsonify({"jeichitom mara..."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
