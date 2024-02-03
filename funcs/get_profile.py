import requests
import json
from lxml import html

with open('data/profile_headers.json', 'r') as profile_headers:
    headers = json.load(profile_headers)

with open('data/profile_cookies.json', 'r') as profile_cookies:
    cookies = json.load(profile_cookies)

def get_profile(username):
    try:
        response = requests.get(f'https://www.chess.com/member/{username}', cookies=cookies, headers=headers)
        response.raise_for_status()

        page = html.fromstring(response.text)
        profile_name_element = page.xpath('/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]')
        if profile_name_element:
            profile_name_text = profile_name_element[0].text_content().strip()
            return profile_name_text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error during request for {username}: {e}")
        return None
    except Exception as e:
        print(f"Error processing {username}: {e}")
        return None