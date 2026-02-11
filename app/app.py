from flask import Flask, render_template
from ids_engine import start_ids, alerts

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    start_ids()
    app.run(debug=True)
