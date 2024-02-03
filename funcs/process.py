# import time
# import json
# from funcs.get_reset import reset_hint
# from funcs.get_profile import get_profile
# from funcs.sb.lookup import *
# from funcs.sb.config import *
# from funcs.emails import find_matching_mails
# from funcs.confirm import confirm_mail
# from funcs.caps import uncapitalize_except_first

# def process_names(names, delay):
#     print(f'Waiting {delay}s between each search')
#     processed_names = set()

#     for current_name in names:
#         if current_name in processed_names:
#             continue

#         new_name = uncapitalize_except_first(current_name)
#         unique_passwords = set()
#         unique_hashes = set()

#         time.sleep(delay)
#         display_name = get_profile(current_name)
#         email_hint = reset_hint(current_name).get("email", "Email not found")

#         print(f'{new_name}: {email_hint} | {display_name} ')

#         if display_name and len(display_name) > 3:
#             emails_response = search_request({
#                 'terms': [str(display_name)],
#                 'types': ['name'],
#                 'wildcard': False
#             })

#             if outputSnusbaseLogs == True:
#                 with open(f'output/snusbase_{new_name}.txt', 'w+', encoding='utf-8') as file:
#                     file.write(str(emails_response))

#             emails = [entry['email'] for key, value in emails_response['results'].items() for entry in value if 'email' in entry]

#             if printSnusbaseLogs == True:
#                 print(f'{emails}\n\n')

#             try:
#                 matched_emails = find_matching_mails(emails, email_hint, debug=debug)
#             except Exception as e:
#                 print(e)
            
#             try:
#                 if printSnusbaseLogs == True:
#                     dumped_matched_emails = json.dumps(matched_emails, indent=2)
#                     print(f'Dumped matched_emails:\n{dumped_matched_emails}')
#             except Exception as e:
#                 print(e)
#                 continue

#             confirmed_emails = set()
#             possible_emails = []

#             for email in matched_emails:
#                 if confirm_mail(email) == 200:
#                     # print(f'Confirmed email: {email}')

#                     pw_hash_data = search_request({
#                         'terms': [str(email)],
#                         'types': ['email'],
#                         'wildcard': False
#                     })

#                     for key, value in pw_hash_data.get('results', {}).items():
#                         try:
#                             for entry in value:
#                                 if 'password' in entry:
#                                     password = entry['password']
#                                     password_combo = (email, password)
#                                     if password_combo not in unique_passwords:
#                                         unique_passwords.add(password_combo)
#                                         confirmed_emails.add(password_combo)
#                                         print(f'{new_name} - {email}:{password}')

#                                 elif 'hash' in entry:
#                                     hash = entry['hash']
#                                     if hash not in unique_hashes:
#                                         unique_hashes.add(hash)

#                         except Exception as e:
#                             if debug == True:
#                                 print(f"Error processing data for key {key}: {e}")

#                     for h in unique_hashes:
#                         hash_data_req = dehash({
#                             'terms': [h],
#                             'types': ['hash']
#                         })

#                         for key, value in hash_data_req.items():
#                             try:
#                                 password = value.get('password')
#                                 if password:
#                                     password_combo = (email, password)
#                                     if password_combo not in unique_passwords:
#                                         unique_passwords.add(password_combo)
#                                         confirmed_emails.add(password_combo)
#                                         print(f'{new_name} - {email}:{password}')
#                             except Exception as e:
#                                 if debug == True:
#                                     print(f"Error processing data for key {key}: {e}")

#                     with open(f'output/results_{new_name}.txt', 'w+', encoding='utf-8') as outputtedFile:
#                         outputtedFile.write(f'{new_name} Hint: {email_hint}\n\n')

#                         if confirmed_emails:
#                             outputtedFile.write('Confirmed Email:\n')
#                             outputtedFile.write(f'{email}')
#                             outputtedFile.write('\n\n')

#                         if unique_passwords:
#                             outputtedFile.write('Leaked Passwords:\n')
#                             outputtedFile.write('\n'.join([f'{password}' for _, password in unique_passwords]))

#                     break
#                 else:
#                     possible_emails.append(email)

#         elif debug == True:
#             print(f'Display name too short or not found - {new_name} | {display_name}')

#         processed_names.add(new_name)

# import time
# import json
# from funcs.get_reset import reset_hint
# from funcs.get_profile import get_profile
# from funcs.sb.lookup import *
# from funcs.sb.config import *
# from funcs.emails import find_matching_mails
# from funcs.confirm import confirm_mail
# from funcs.caps import uncapitalize_except_first

# def process_names(names, delay):
#     print(f'Waiting {delay}s between each search')
#     processed_names = set()

#     for current_name in names:
#         if current_name in processed_names:
#             continue

#         new_name = uncapitalize_except_first(current_name)
#         unique_passwords = set()
#         unique_hashes = set()

#         time.sleep(delay)
#         display_name = get_profile(current_name)
#         email_hint = reset_hint(current_name).get("email", "Email not found")

#         print(f'{new_name}: {email_hint} | {display_name} ')

#         if display_name and len(display_name) > 3:
#             emails_response = search_request({
#                 'terms': [str(display_name)],
#                 'types': ['name'],
#                 'wildcard': False
#             })

#             if outputSnusbaseLogs == True:
#                 with open(f'output/snusbase_{new_name}.txt', 'w+', encoding='utf-8') as file:
#                     file.write(str(emails_response))

#             emails = [entry['email'] for key, value in emails_response.get('results', {}).items() for entry in value if 'email' in entry]

#             if printSnusbaseLogs == True:
#                 print(f'{emails}\n\n')

#             try:
#                 matched_emails = find_matching_mails(emails, email_hint, debug=debug)
#             except Exception as e:
#                 print(e)
            
#             try:
#                 if printSnusbaseLogs == True:
#                     dumped_matched_emails = json.dumps(matched_emails, indent=2)
#                     print(f'Dumped matched_emails:\n{dumped_matched_emails}')
#             except Exception as e:
#                 print(e)
#                 continue

#             confirmed_emails = set()
#             possible_emails = []

#             for email in matched_emails:
#                 if confirm_mail(email) == 200:
#                     pw_hash_data = search_request({
#                         'terms': [str(email)],
#                         'types': ['email'],
#                         'wildcard': False
#                     })

#                     print(f"pw_hash_data: {pw_hash_data}")

#                     if 'results' in pw_hash_data:
#                         for key, value in pw_hash_data['results'].items():
#                             try:
#                                 for entry in value:
#                                     if 'password' in entry:
#                                         password = entry['password']
#                                         password_combo = (email, password)
#                                         if password_combo not in unique_passwords:
#                                             unique_passwords.add(password_combo)
#                                             confirmed_emails.add(password_combo)
#                                             print(f'{new_name} - {email}:{password}')

#                                     elif 'hash' in entry:
#                                         hash = entry['hash']
#                                         if hash not in unique_hashes:
#                                             unique_hashes.add(hash)
#                             except Exception as e:
#                                 if debug == True:
#                                     print(f"Error processing data for key {key}: {e}")

#                         for h in unique_hashes:
#                             hash_data_req = dehash({
#                                 'terms': [h],
#                                 'types': ['hash']
#                             })

#                             print(f"hash_data_req: {hash_data_req}")

#                             if 'results' in hash_data_req:
#                                 for key, value in hash_data_req['results'].items():
#                                     try:
#                                         password = value.get('password')
#                                         if password:
#                                             password_combo = (email, password)
#                                             if password_combo not in unique_passwords:
#                                                 unique_passwords.add(password_combo)
#                                                 confirmed_emails.add(password_combo)
#                                                 print(f'{new_name} - {email}:{password}')
#                                     except Exception as e:
#                                         if debug == True:
#                                             print(f"Error processing data for key {key}: {e}")

#                         with open(f'output/results_{new_name}.txt', 'w+', encoding='utf-8') as outputtedFile:
#                             outputtedFile.write(f'{new_name} Hint: {email_hint}\n\n')

#                             if confirmed_emails:
#                                 outputtedFile.write('Confirmed Email:\n')
#                                 outputtedFile.write(f'{email}')
#                                 outputtedFile.write('\n\n')

#                             if unique_passwords:
#                                 outputtedFile.write('Leaked Passwords:\n')
#                                 outputtedFile.write('\n'.join([f'{password}' for _, password in unique_passwords]))

#                     break
#                 else:
#                     possible_emails.append(email)

#         elif debug == True:
#             print(f'Display name too short or not found - {new_name} | {display_name}')

#         processed_names.add(new_name)

import time
import json
from funcs.get_reset import reset_hint
from funcs.get_profile import get_profile
from funcs.sb.lookup import *
from funcs.sb.config import *
from funcs.emails import find_matching_mails
from funcs.confirm import confirm_mail
from funcs.caps import uncapitalize_except_first

def process_names(names, delay):
    print(f'Waiting {delay}s between each search')
    processed_names = set()

    for current_name in names:
        if current_name in processed_names:
            continue

        new_name = uncapitalize_except_first(current_name)
        unique_passwords = set()
        unique_hashes = set()

        time.sleep(delay)
        display_name = get_profile(current_name)
        email_hint = reset_hint(current_name).get("email", "Email not found")

        print(f'{new_name}: {email_hint} | {display_name} ')

        if display_name and len(display_name) > 3:
            emails_response = search_request({
                'terms': [str(display_name)],
                'types': ['name'],
                'wildcard': False
            })

            if outputSnusbaseLogs == True:
                with open(f'output/snusbase_{new_name}.txt', 'w+', encoding='utf-8') as file:
                    file.write(str(emails_response))

            emails = [entry['email'] for key, value in emails_response.get('results', {}).items() for entry in value if 'email' in entry]

            if printSnusbaseLogs == True:
                print(f'{emails}\n\n')

            try:
                matched_emails = list(set(find_matching_mails(emails, email_hint, debug=debug)))
            except Exception as e:
                print(e)
                continue
            
            try:
                if printSnusbaseLogs == True:
                    dumped_matched_emails = json.dumps(matched_emails, indent=2)
                    print(f'Dumped matched_emails:\n{dumped_matched_emails}')
            except Exception as e:
                print(e)
                continue

            confirmed_emails = set()
            possible_emails = []

            for email in matched_emails:
                if confirm_mail(email) == 200:
                    pw_hash_data = search_request({
                        'terms': [str(email)],
                        'types': ['email'],
                        'wildcard': False
                    })

                    print(pw_hash_data)

                    if 'results' in pw_hash_data:
                        for key, value in pw_hash_data['results'].items():
                            try:
                                for entry in value:
                                    if 'password' in entry:
                                        password = entry['password']
                                        password_combo = (email, password)
                                        if password_combo not in unique_passwords:
                                            unique_passwords.add(password_combo)
                                            confirmed_emails.add(password_combo)
                                            print(f'{new_name} - {email}:{password}')

                                    elif 'hash' in entry:
                                        hash_value = entry['hash']
                                        if hash_value not in unique_hashes:
                                            unique_hashes.add(hash_value)
                            except Exception as e:
                                if debug == True:
                                    print(f"Error processing data for key {key}: {e}")

                    if not unique_passwords and unique_hashes:  # Check if passwords were found
                        for hash_value in unique_hashes:
                            hash_data_req = dehash({
                                'terms': [hash_value],
                                'types': ['hash']
                            })

                            print(f"hash_data_req: {hash_data_req}")

                            if 'results' in hash_data_req and isinstance(hash_data_req['results'], dict):
                                for key, value in hash_data_req['results'].items():
                                    try:
                                        password = value.get('password')
                                        if password:
                                            password_combo = (email, password)
                                            if password_combo not in unique_passwords:
                                                unique_passwords.add(password_combo)
                                                confirmed_emails.add(password_combo)
                                                print(f'{new_name} - {email}:{password}')
                                    except Exception as e:
                                        if debug == True:
                                            print(f"Error processing data for key {key}: {e}")
                            else:
                                print("No results found in hash_data_req.")


                    with open(f'output/results_{new_name}.txt', 'w+', encoding='utf-8') as outputtedFile:
                        outputtedFile.write(f'{new_name}\n{confirmed_emails}\n\n')

                        # if confirmed_emails:
                        #     outputtedFile.write('Confirmed Emails:\n')
                        #     for email, password in confirmed_emails:
                        #         outputtedFile.write(f'{email}:{password}\n')
                        #     outputtedFile.write('\n\n')

                        if unique_passwords:
                            outputtedFile.write('Leaked Passwords:\n')
                            outputtedFile.write('\n'.join([f'{password}' for _, password in unique_passwords]))


                    break
                else:
                    possible_emails.append(email)

        elif debug == True:
            print(f'Display name too short or not found - {new_name} | {display_name}')

        processed_names.add(new_name)
