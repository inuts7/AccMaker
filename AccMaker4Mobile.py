import os

try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
try:
    from autopy import alert
except ImportError:
    os.system('pip install autopy')
    from autopy import alert
try:
    import secrets
except ImportError:
    os.system('pip install secrets')
    import secrets

clear = lambda: os.system('cls')


def close():
    input("- Press enter To exit !\n")
    exit()

clear()

banner = """
   ____    ____        _  __     _                     __  
  / __ \  |___ \__   _(_)/ /_   | |__   ___ _ __ ___   \ \ 
 / / _` |   __) \ \ / / | '_ \  | '_ \ / _ \ '__/ _ \ (_) |
| | (_| |  / __/ \ V /| | (_) | | | | |  __/ | |  __/  _| |
 \ \__,_| |_____| \_/_/ |\___/  |_| |_|\___|_|  \___| (_) |
  \____/            |__/                               /_/ 

"""


def reg():
    print("- Making The User now , just wait !")

    email = secrets.token_urlsafe(10) + '@gmail.com'

    password = secrets.token_urlsafe(7)

    target = secrets.token_urlsafe(7)

    cookie = secrets.token_hex(8) * 2

    uid = uuid4()

    url = 'https://i.instagram.com/api/v1/accounts/create/'

    regdata = {
        'phone_id': uid,
        'device_id': uid,
        "ds_user_id=": password,
        'email': email,
        'password': password,
        'username': target,
        'first_name': ''
    }
    head = {
        'user-agent': 'Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)',
        'x-csrftoken': 'missing',
        'mid': cookie
    }
    register = requests.post(url, headers=head, data=regdata)
    if 'challenge' in register.text:
        open(f'@{target}.txt', 'a').write(f'user : {target},\npass : {password},\nemail : {email},\nNeed Phone Number !\nCoded By @2vj6 Enjoy !')
        print("Done Making Account , info Saved in A File !")
        exit()
    elif '"account_created": true' in register.text:
        open(f'@{target}.txt', 'a').write(f'user : {target},\npass : {password},\nemail : {email},\nNo Number Need !\nCoded By @2vj6 Enjoy !')
        print("Done Making Account , info Saved in A File !")
        exit()
    elif 'signup_block' or 'Please wait a few minutes before you try again.' in register.text:
        print("You Got blocked , Try Again After 10 - 15m Please !")
        close()
    elif "username_is_taken" or "username_held_by_others" in register.text:
        reg()
    else:
        print(f"some error happened , check the response > \n{register.text}")


print(banner + "                 - Account Maker .")
reg()
