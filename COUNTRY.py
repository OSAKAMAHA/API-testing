from flask import Flask,request
from flask import jsonify
import requests
import json  
 
app = Flask(__name__) 


def connect(name):
    url = "https://restcountries.eu/rest/v2/name/"
    c = url+name

    return c


@app.route("/<string:name>")
def country_info(name: str = None):
    x = connect(name)
    response = requests.get(x).content

    if response is None:
        return "Error in Connection"
    else:
        return response
    


@app.route("/<string:name>/<info>")  
def Info(name: str = None,info = None): 
      
    country = country_info(name)
    info = info.split(",")
    out = "{"
    
    websiteinfo = json.loads(country)[0]
    if websiteinfo is None:
        return "error in name"
    else:  
        for s in info:
            try:
                out += s+":"+str(websiteinfo[s])+ ","
            except KeyError:
                return "wrong info"
        out += "}"

        return out
    
if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode