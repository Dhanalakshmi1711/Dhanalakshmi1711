from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, how are u?!"

@app.route('/api')
def api():
    return jsonify({"message": "Hello, flask api!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
