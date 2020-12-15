from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route("/")
def mainpage(): #STARTPAGE
    return render_template("index.html")

@app.route("/pappa")
def pappa(): 
    return render_template("pappa.html")


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