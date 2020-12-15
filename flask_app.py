#Title generator : https://bit.ly/381FdFn
from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/mamma")
def mamma(): 
    mammaText = "God Jul till dig Mamma. Tack för att du står ut med mig varje dag, även om jag kan bli jobbig ibland ❤️"
    mammaLinks = []
    return render_template("index.html", currentName="Mamma", imageLink=url_for('static', filename='mamma.png'), links=mammaLinks, personalMessage=mammaText)

@app.route("/pappa")
def pappa(): 
    pappaText = "God Jul till den bästa pappan som finns! Tack för allt du gör för mig, och för allt vi har gjort genom åren. ❤️"
    pappaLinks = ["https://bit.ly/34h7pTI","https://bit.ly/3qWRoMa","https://bit.ly/3qZQX3Z","https://bit.ly/37m64gl","https://bit.ly/3oXvLK5","https://bit.ly/2K8Jf6K","https://bit.ly/3oXvMh7"]
    return render_template("index.html", currentName="Pappa", imageLink=url_for('static',filename='pappa.png'), links=pappaLinks, personalMessage=pappaText)

@app.route("/linnea")
def linnea(): 
    linneaText = "God Jul till bästa storasystern!"
    linneaLinks = []
    return render_template("index.html", currentName="Linnea", imageLink=url_for('static',filename='linnea.png'), links=linneaLinks, personalMessage=linneaText)

@app.route("/oskar")
def oskar(): 
    oskarText = "God Jul till Oskar, och tack för att du tar hand om min stora-syster!"
    oskarLinks = []
    return render_template("index.html", currentName="Oskar", imageLink=url_for('static',filename='oskar.png'), links=oskarLinks, personalMessage=oskarText)

# if __name__ == "__main__":
#     try:
#         ipConfig = []
#         with open("private.txt","r+") as f:
#             for x in f.readlines():
#                 ipConfig.append(x.strip("\n"))
#         app.run(debug=False, host=ipConfig[0], port=ipConfig[1])
#     except FileNotFoundError:
#         input("ERROR : Could not find IP file, please create a file called 'ip.txt' in the root and put server ip and port")
#     except OSError:
#         input("ERROR : Incorrect IP")
#     else:
#         pass