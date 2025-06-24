import requests

def load_lottieurl(url):
    lottieurl = requests.get(url)
    if lottieurl.status_code != 200:
        return None
    return lottieurl.json()