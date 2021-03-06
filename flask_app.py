# Title generator : https://bit.ly/381FdFn
from flask import Flask,render_template,request,redirect,url_for
from flask_mobility import Mobility
from random import shuffle
import os
app = Flask(__name__)
Mobility(app)
@app.route("/<linkInput>")
def main(linkInput):
    try:
        linkInput = linkInput.lower()
        selected=("mamma","pappa","linneaoskar").index(linkInput)
        personalText=[
            "God Jul till dig Mamma. Tack för att du står ut med mig varje dag, även om jag kan bli jobbig ibland. ❤️",
            "God Jul till den bästa pappan som finns! Tack för allt du gör för mig, och för allt kul vi har gjort tillsammans genom åren. ❤️",
            "God Jul till er båda! Ni är bäst! ❤️"
        ][selected]
        titleNames=["Mamma", "Pappa", "Linnea, Oskar och Rio"][selected]
        myImages=[f"static/{linkInput}/{x}" for x in os.listdir(f"Jul2020/static/{linkInput}")]
        shuffle(myImages)
        return render_template("index.html", currentName=titleNames, titleImage=f"static/{linkInput}.png", images=myImages, personalMessage=personalText)
    except Exception as e:
        return render_template("error.html", errorMessage=str(e))