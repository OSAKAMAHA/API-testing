from flask import Flask,request
from flask import jsonify
import requests
import json  
import redis
 
app = Flask(__name__) 

redis = redis.Redis()

def connect(name):
    url = "https://restcountries.eu/rest/v2/name/"
    c = url+name

    return c


def country_info(name: str = None):
    x = connect(name)
    response = requests.get(x).content

    if response is None:
        return "Error in Connection"
    else:
         redis.setex (name,60,str(response))
         
         
@app.route("/<string:name>")    
def fetch_cache_name(name: str = None):
    result = redis.get(name)
    if not result:
        country_info(name)
        result = redis.get(name)
        return str(result) + "new"
    else:
        return result



@app.route("/<string:name>/<info>")  
def Info(name: str = None,info = None): 
    x = connect(name)
    response = requests.get(x).content
    country = response
  
    result = redis.get(str(info))
    if not result:

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
            redis.setex (str(info),60,str(out))
            result = redis.get(str(info))
            return str(result) 
    else:
        return result      
    




if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode
    
    
    