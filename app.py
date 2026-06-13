from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Jenkins Shared Library Project &welcome to DevOps"

app.run(host="0.0.0.0",port=80)
