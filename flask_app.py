#Title generator : https://bit.ly/381FdFn
from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/<linkInput>")
def goToPage(linkInput):
    try:
        from random import shuffle
        selected=("mamma","pappa","linnea","oskar","linneaoskar").index(linkInput)
        allText=[
            "God Jul till dig Mamma. Tack för att du står ut med mig varje dag, även om jag kan bli jobbig ibland ❤️",
            "God Jul till den bästa pappan som finns! Tack för allt du gör för mig, och för allt vi har gjort genom åren. ❤️",
            "God Jul till bästa storasystern! Du finns alltid där för mig! Älskar dig!",
            "God Jul till Oskar, och tack för att du tar så bra hand om min stora-syster!",
            "Ni är bäst!"
        ]
        


        allImages=[
            ["https://bit.ly/3r0wuvV","https://bit.ly/3nphEg7","https://bit.ly/3mmh4P1","https://bit.ly/3oVWmau","https://bit.ly/37kq1nN","https://bit.ly/3qXpik3"],
            ["https://bit.ly/34h7pTI","https://bit.ly/3qWRoMa","https://bit.ly/3qZQX3Z","https://bit.ly/37m64gl","https://bit.ly/3oXvLK5","https://bit.ly/2K8Jf6K","https://bit.ly/3oXvMh7"],
            ["https://bit.ly/2LxBibD"],
            ["https://bit.ly/2LxBibD"],
            [f"static/{linkInput}/{x}.png"for x in range(9)] + ["https://bit.ly/2LxBibD"]
        ]


        import os
        #theDir = os.listdir(f"static/{linkInput}")
        
        raise os.getcwd()
        # for filename in theDir:
        #     if filename.endswith(".png"):
        #         # print(os.path.join(directory, filename))
        #         continue
        #     else:
        #         continue

        allNames=[
            "Mamma",
            "Pappa",
            "Linnea",
            "Oskar",
            "Linnea och Oskar"
        ]
        for x in allImages:
            shuffle(x)
        return render_template("index.html", currentName=allNames[selected], imageLink=url_for('static',filename=linkInput+'.png'), links=allImages[selected], personalMessage=allText[selected])
    except Exception as e:
        return render_template("error.html",errormessage=str(e))