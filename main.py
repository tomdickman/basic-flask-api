from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/<name>', methods=['GET'])
def hello_world(name):
    return jsonify({"message": f"Hello {name.capitalize()}!"}), 200

if __name__ == "__main__":
    app.run()