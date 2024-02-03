from .config import api
import requests, json

def search_request(body=None):
    headers = {
        'Auth': api,
        'Content-Type': 'application/json',
    }

    method = 'POST' if body else 'GET'
    data = json.dumps(body) if body else None
    response = requests.request(method, 'https://api-experimental.snusbase.com/data/search', headers=headers, data=data)
    return response.json()

def whois(body=None):
    headers = {
        'Auth': api,
        'Content-Type': 'application/json',
    }

    method = 'POST' if body else 'GET'
    data = json.dumps(body) if body else None
    response = requests.request(method, 'https://api-experimental.snusbase.com/tools/ip-whois', headers=headers, data=data)
    return response.json()

def dehash(body=None):
    headers = {
        'Auth': api,  # Assuming 'api' is defined somewhere in your code
        'Content-Type': 'application/json',
    }

    method = 'POST' if body else 'GET'
    data = json.dumps(body) if body else None
    response = requests.request(method, 'https://api-experimental.snusbase.com/tools/hash-lookup', headers=headers, data=data)

    jsoned = response.json()
    if 'results' in jsoned and jsoned['results']:
        # Creating the base dictionary
        result_dict = {}

        # Adding 'result_1' and 'result_2' keys if available
        if '0001_HASHES_ORG_1913M_2021' in jsoned['results']:
            result_dict['HASHES_ORG'] = {
                'hash': jsoned['results']['0001_HASHES_ORG_1913M_2021'][0]['hash'],
                'password': jsoned['results']['0001_HASHES_ORG_1913M_2021'][0]['password']
            }
        if '0002_HASHMOB_NET_2976M_082023' in jsoned['results']:
            result_dict['HASHMOB_NET'] = {
                'hash': jsoned['results']['0002_HASHMOB_NET_2976M_082023'][0]['hash'],
                'password': jsoned['results']['0002_HASHMOB_NET_2976M_082023'][0]['password']
            }

        return result_dict
    else:
        return jsoned