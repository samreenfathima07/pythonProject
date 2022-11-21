import requests


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : '9538665762',
        'message' : 'hey, goog morning',
        'key' : 'textbelt',
    })
    print(resp.json())


# not completed
