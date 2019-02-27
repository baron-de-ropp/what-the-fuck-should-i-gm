from flask import Flask, render_template, url_for
import random
from models.FuckingCampaign import FuckingCampaign
from models.FuckingEncounter import FuckingEncounter
from models.FuckingAdventure import FuckingAdventure

app = Flask(__name__)

@app.route("/")
@app.route("/campaign")
def campaign():
    campaign = FuckingCampaign()
    return render_template("campaign.html",campaign=campaign)

@app.route("/adventure")
def adventure():
    adventure = FuckingAdventure()
    return render_template("adventure.html", adventure=adventure)

@app.route("/encounter")
@app.route(("/encounter/<terrain>"))
def encounter(terrain=random.choice(["arctic","coastal","desert","forest","grassland","hills","mountian","swamp","underdark","underwater"])):
    terrain = terrain.lower()
    encounter = FuckingEncounter(terrain)
    return render_template("encounter.html",encounter=encounter)


if __name__ == "__main__":
    app.run(debug=True)