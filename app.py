from flask import Flask,request,Response,render_template
from backend import weather_bknd
from backend import pest
from backend import pano_threesixty

app = Flask(__name__)

apiKey = 'a3785d5747aad2626db38e5df40e91db'


@app.route('/')
def home():


    return render_template('index.html',panoraj=pano_threesixty.fetch())

@app.route('/weather')
def weather(city=None):

    if city:
        pass
    else:
        city = "raipur"

    callClass = weather_bknd.weather(apiKey,city,debug=False)
    callClassFunctionCurrent = callClass.weatherPresent()

    callClassFunctionForcast = callClass.forcastFuture()

    print(callClassFunctionCurrent)

    print("[-] Weather")

    return render_template('weather.html',
                           region = callClassFunctionCurrent[2],
                           temp = callClassFunctionCurrent[3],
                           comment = callClassFunctionCurrent[4],
                           ico1 = callClassFunctionCurrent[6],
                           
                           w1TimeMain= (str("12:00 PM "))+ callClassFunctionForcast[1][0],
                           w1TempMain= callClassFunctionForcast[0][0],
                           w1CommentMain= callClassFunctionForcast[3][0].title(),
                           
                           w2Time= (str("12:00 PM "))+ callClassFunctionForcast[1][1],
                           w2Temp= callClassFunctionForcast[0][1],
                           w2Comment= callClassFunctionForcast[3][1].title(),
                           
                           w3Time=(str("12:00 PM "))+ callClassFunctionForcast[1][2],
                           w3Temp=callClassFunctionForcast[0][2],
                           w3Comment=callClassFunctionForcast[3][2].title(),

                           w4Time= (str("12:00 PM "))+ callClassFunctionForcast[1][3],
                           w4Temp= callClassFunctionForcast[0][3],
                           w4Comment= callClassFunctionForcast[3][3].title(),
                           
                           w5Time= (str("12:00 PM  "))+ callClassFunctionForcast[1][4],
                           w5Temp= callClassFunctionForcast[0][4],
                           w5Comment= callClassFunctionForcast[3][4].title()                                                                              
                           )

@app.route('/actionSearch', methods =["GET", "POST"])
def actionSearch():
    if request.method == "POST":
       print("[*] ",request.form.get("searchcity"))
    return weather(request.form.get("searchcity"))


@app.route('/pest')
def pest1():
  
    return render_template("pest.html",content=pest.returnContent())

@app.route('/soil')
def soil():
    print("soil")

    
    return render_template("soil.html")

@app.route('/govplus')
def gov():
    return render_template("govtplus.html")

@app.route('/resource')
def res():
    return render_template("resource1.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)