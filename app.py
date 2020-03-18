from flask import Flask
from flask import jsonify
import requests
import json  

  
  
app = Flask(__name__) 

@app.route("/<string:name>/<info>")  
def Info(name: str = None,info = None): 

    url = "https://restcountries.eu/rest/v2/name/"
    c = url+name
    info = info.split(",")
    out = "{"
    websiteinfo = json.loads(requests.get(c).content)[0]
    for s in info:
        out += s+":"+str(websiteinfo[s])+ ","
    out += "}"
    return out
  
if __name__ =="__main__":  
    app.run(debug = True)  