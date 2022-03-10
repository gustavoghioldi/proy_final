import requests

class DolarService:

    @staticmethod
    def get_usd_ccl()->float:
        r = requests.get("https://criptoya.com/api/dolar")
        return r.json()['ccl']