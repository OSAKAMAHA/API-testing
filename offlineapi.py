from flask import Flask
from flask import jsonify
import json
app = Flask(__name__) 
@app.route("/")
def countryError():
    return "please enter country name and info"
@app.route("/<country>") 
def infoError(country = None):
    return "please enter the info you want for "+country
@app.route("/<string:name>/<info>")  
def main(name: str = None,info = None): 
    info = info.split(",")
    data = openJsonFile('countrydata.txt')
    cdata = getcountry(data,name)
    if cdata is None:
        return "this is not a right country name"
    out = getInfo(cdata,info)
    if out is not None:
        return out
    else:
        return "invalid info name"   
def getcountry(data:json,name:str):
    for i in data:
        if str(i["name"]).lower() == name.lower():
            return i
    return None
def openJsonFile(filename):
     with open(filename,encoding="utf8") as json_file:
        return json.load(json_file)
def getInfo(countryData,info):
    out = "{"
    for s in info:
        try:
            out += s+":"+str(countryData[s])+ ","
        except KeyError :
            return None
    out += "}"
    return out
if __name__ =="__main__":  
    app.run(debug = True)  