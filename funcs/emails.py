import json
import fnmatch
from funcs.sb.config import debug

def load_real_mails(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data['emails']

def find_matching_mails(real_emails, hinted_email, debug=debug):
    matches = []

    hinted_username, hinted_domain = hinted_email.split('@')
    hinted_username_chars = [c for c in hinted_username if c != '*']
    hinted_domain_chars = [c for c in hinted_domain if c != '*']
    
    hinted_username_pattern = '*'.join(hinted_username_chars)
    hinted_domain_pattern = '*'.join(hinted_domain_chars)

    for real_email in real_emails:
        if '@' in real_email:
            real_username, real_domain = real_email.split('@')
            
            if debug:
                print(f"Comparing {real_email} with {hinted_email}")
                print(f"Real Username: {real_username}")
                print(f"Real Domain: {real_domain}")

            try:
                username_match = fnmatch.fnmatch(real_username, hinted_username_pattern)
                domain_match = fnmatch.fnmatch(real_domain, hinted_domain_pattern)

                if username_match and domain_match:
                    matches.append(real_email)

            except Exception as e:
                if debug:
                    print(f"Error comparing {real_email} with {hinted_email}: {e}")

    return matches