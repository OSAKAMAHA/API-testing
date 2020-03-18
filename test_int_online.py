import requests
import COUNTRY


def test_valid_request():
    url = 'http://127.0.0.1:8080/egypt/capital'
    r   = requests.get(url)
    expec = {'capital':'Cairo'}
    assert r.json == expec 

def test_empty():
    url = 'http://127.0.0.1:8080/egypt/'
    r   = requests.get(url)                
    assert r.status_code == 400

def test_request_wrong():
    url = 'http://127.0.0.1:8080/egypt/capial'
    r   = requests.get(url)
    assert r.status_code == 400

def test_api_error():
    url = 'http://127.0.0.1:8080/egypt/capital'
    r   = requests.get(url)
    assert r.status_code == 500