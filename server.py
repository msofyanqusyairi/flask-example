from flask import Flask, render_template, send_from_directory, request

from model import User

app = Flask(__name__)

# configure static files
@app.route('/<path:path>')
def staticfile(path):
    return send_from_directory('static', filename=path)

# render index
@app.route('/', methods=['GET'])
def index():
    title = "home"
    name = "tom"
    # instansiasi class User
    user = User(name)
    return render_template('index.html', title = title, user = user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug= True)