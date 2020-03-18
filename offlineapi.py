from flask import Flask
from flask import jsonify
import json
app = Flask(__name__) 

@app.route("/<string:name>/<info>")  
def Info(name: str = None,info = None): 
    if name is None :
        return "please enter the country"
    if info is None:
        return "please enter the country info and try again"
    with open('countrydata.txt',encoding="utf8") as json_file:
        data = json.load(json_file)
    info = info.split(",")
    cdata = getcountry(data,name)
    if cdata is None:
        return "this is not a right country name"
    out = "{"
    for s in info:
        if cdata[s] is not None:
            out += s+":"+str(cdata[s])+ ","
        else :
            return s+"is not a right info for a country"
    out += "}"
    return out
def getcountry(data:json,name:str):
    for i in data:
        if str(i["name"]).lower() == name.lower():
            return i
    return None
if __name__ =="__main__":  
    app.run(debug = True)  