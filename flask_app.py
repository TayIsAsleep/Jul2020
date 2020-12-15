from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route("/")
def mainpage(): #STARTPAGE
    return render_template("index.html")

@app.route("/mamma")
def mamma(): 
    return render_template("mamma.html")

@app.route("/pappa")
def pappa(): 
    pappaLinks = ["https://bit.ly/34h7pTI","https://bit.ly/3qWRoMa","https://bit.ly/3qZQX3Z","https://bit.ly/37m64gl","https://bit.ly/3oXvLK5","https://bit.ly/2K8Jf6K","https://bit.ly/3oXvMh7"]
    return render_template("pappa.html",currentName="Pappa", imageLink="pappa",links=pappaLinks)

@app.route("/linnea")
def linnea(): 
    return render_template("linnea.html")

@app.route("/oskar")
def oskar(): 
    return render_template("oskar.html")




if __name__ == "__main__":
    try:
        ipConfig = []
        with open("private.txt","r+") as f:
            for x in f.readlines():
                ipConfig.append(x.strip("\n"))
        app.run(debug=False, host=ipConfig[0], port=ipConfig[1])
    except FileNotFoundError:
        input("ERROR : Could not find IP file, please create a file called 'ip.txt' in the root and put server ip and port")
    except OSError:
        input("ERROR : Incorrect IP")
    else:
        pass