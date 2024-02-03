import requests
import json

with open('data/reset_headers.json', 'r') as reset_headers:
    headers = json.load(reset_headers)

with open('data/reset_cookies.json', 'r') as reset_cookies:
    cookies = json.load(reset_cookies)

def reset_hint(username):
    try:
        response = requests.get(f'https://www.chess.com/callback/recover-password-data/{username}', cookies=cookies, headers=headers)
        response.raise_for_status()

        if "An error occurred" in response.text:
            return {"error": True, "error_message": "Invalid username"}
        elif "Resource not found" in response.text:
            return {"error": True, "error_message": "Invalid username"}
        else:
            response_data = json.loads(response.text)
            email_value = response_data.get("email")
            
            if email_value is not None:
                return {"email": email_value}
            else:
                return {"error": True, "error_message": "Email not found in the response"}
    except requests.exceptions.RequestException as e:
        return {"error": True, "error_message": f"Request error for {username}: {e}"}
    except Exception as e:
        return {"error": True, "error_message": f"Error processing {username}: {e}"}