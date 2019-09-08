from flask import Flask, render_template, url_for
import random
from models.FuckingCampaign import FuckingCampaign
from models.FuckingMonster import FuckingMonster

app = Flask(__name__)

@app.route("/")
def index():
    campaign = FuckingCampaign()
    return render_template("campaign.html",campaign=campaign)


@app.route("/fucking-monster")
def fucking_monster():
    monster = FuckingMonster()
    return render_template("monster.html",monster=monster)


if __name__ == "__main__":
    app.run(debug=True)