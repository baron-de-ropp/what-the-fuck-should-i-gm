from flask import Flask, render_template, url_for
import random
from models.FuckingCampaign import FuckingCampaign

app = Flask(__name__)

@app.route("/")
def index():
    campaign = FuckingCampaign()
    return render_template("index.html",campaign=campaign)


if __name__ == "__main__":
    app.run(debug=True)