import requests
import json
import time
from funcs.sb.config import delay, debug

with open('data/confirm_headers.json', 'r') as confirm_headers:
    headers = json.load(confirm_headers)

with open('data/confirm_cookies.json', 'r') as confirm_cookies:
    cookies = json.load(confirm_cookies)

def confirm_mail(mail):
    time.sleep(delay)
    response = requests.get(f'https://www.chess.com/callback/email/exist?email={mail}', cookies=cookies, headers=headers)

    if response.status_code == 200:
        if debug == True:
            print(mail, response.status_code)
        return 200
    elif response.status_code == 429:
        if debug == True:
            print(mail, response.status_code)
        return 429
    elif response.status_code == 404:
        if debug == True:
            print(mail, response.status_code)
        return 404
    else:
        if debug == True:
            print(mail, response.status_code)
        return 0