# captcha_solver.py
import requests
import time

API_KEY = "31879aa5b4480c781a6b5b032ecc06e7"

def solve_recaptcha(site_key, url):
    print("[*] Solving CAPTCHA via 2Captcha...")
    response = requests.post("http://2captcha.com/in.php", data={
        'key': API_KEY,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url,
        'json': 1
    })
    request_id = response.json().get("request")

    # Poll for result
    for _ in range(20):
        time.sleep(5)
        result = requests.get(f"http://2captcha.com/res.php?key={API_KEY}&action=get&id={request_id}&json=1")
        if result.json().get("status") == 1:
            return result.json().get("request")
    return None
