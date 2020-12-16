#Title generator : https://bit.ly/381FdFn
from flask import Flask,render_template,request,redirect,url_for
from random import shuffle
import os
app = Flask(__name__)
@app.route("/<linkInput>")
def goToPage(linkInput):
    try:
        selected=("mamma","pappa","linneaoskar").index(linkInput)
        allText=[
            "God Jul till dig Mamma. Tack för att du står ut med mig varje dag, även om jag kan bli jobbig ibland ❤️",
            "God Jul till den bästa pappan som finns! Tack för allt du gör för mig, och för allt vi har gjort genom åren. ❤️",
            "Ni är bäst! ❤️"
        ]
        allNames=["Mamma", "Pappa", "Linnea och Oskar"]
        myImages=[f"static/{linkInput}/{x}" for x in os.listdir(f"Jul2020/static/{linkInput}")]
        shuffle(myImages)
        return render_template("index.html", currentName=allNames[selected], titleImage=f"static/{linkInput}.png", images=myImages, personalMessage=allText[selected])
    except Exception as e:
        return render_template("error.html", errormessage=str(e))