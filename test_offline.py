import offlineapi
import json
jsoninfo = offlineapi.openJsonFile("countrydata.txt")
egyptinfo = offlineapi.openJsonFile("egyptdata.txt")
def test_getcountry_1():
#capital letter
    assert offlineapi.getcountry(jsoninfo,"Egypt")["name"] == "Egypt"

def test_getcountry_2():
        # small letter
    assert offlineapi.getcountry(jsoninfo,"egypt")["name"] == "Egypt"
def test_getcountry_3():
        #wrong country name
    assert offlineapi.getcountry(jsoninfo,"asdfae") == None
def test_getInfo_1():
    assert offlineapi.getInfo(egyptinfo,{"capital"}) == '{capital:Cairo,}'
def test_getInfo_2():
    assert offlineapi.getInfo(egyptinfo,{"capital","population"}) == '{capital:Cairo,population:91290000,}'
def test_getInfo_3():
    assert offlineapi.getInfo(egyptinfo,{"capital","poption"}) == None
def test_getInfo_4():
    assert offlineapi.getInfo(egyptinfo,{"capal","poption"}) == None
def test_integrated_success1():
    assert offlineapi.main("Egypt","capital") == '{capital:Cairo,}'
def test_integrated_success2():
    assert offlineapi.main("Egypt","capital,population") == '{capital:Cairo,population:91290000,}'
def test_integrated_wrongcountry():
    assert offlineapi.main("dsdfasdf","capital,population") == "this is not a right country name"
def test_integrated_wronginfo():
    assert offlineapi.main("Egypt","capitaadf,population") == "invalid info name" 