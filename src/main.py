import json
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from fake_useragent import UserAgent
from config import MAIL, PASSWORD

# def login():
#     # basic = HTTPBasicAuth('sham1996@yandex.ru', 'sham1996')
#     # URL = "https://api.ishkola.com/api/v1/login"
#     # r = requests.get(URL, auth=basic)
#     #
#     # soup = BeautifulSoup(r.text, "html.parser")
#     # print(soup.prettify())

def login(mail: str, password: str):
    print(UserAgent())
    headers = {
               "Authorization": "Bearer 5959|cUX1x3nac8sLwqrG3F4a9qDHYxPLtJkI8z7pD65z",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    URL = "https://api.ishkola.com/api/v1/login"
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=100,
        pool_maxsize=100)
    s = requests.session()
    payload = {"email": mail,
               "password": password,
               "device_name": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
               }

    res = s.post(url=URL, json=payload)
    print(res.text)
    if res.status_code != 204:
        res.headers.update({'Authorization': json.loads(res.content)["token"]})
    r = s.get("https://api.ishkola.com/api/v1/teacher/dashboard/statistics", headers=headers)
    print(r.text)
    return s


if __name__ == "__main__":

    session = login(MAIL, PASSWORD)

    # soup = BeautifulSoup(r.content, "html.parser")
    # print(soup.prettify())
    # print(soup.findAll("div", {"class": "nav-item"}))
# "'Set-Cookie': 'XSRF-TOKEN=eyJpdiI6InpFZ3ZjOUJZb0dnQjVwRXBJTURXakE9PSIsInZhbHVlIjoibERpaWpJZVBJYnhOZ2p1UHlkZkYzdnpxK1dBakJOQ3BjSzQvemdPNVBMQTB4azg1d0VXRHNIbVY0TFRucUlBNlZkNTRoTDM1RVdib1ZQLzhyRlUrRFRmdVgwZWx2ZGhSUzlTamptQ1dWT0FSZWJmbWRzTHl5Y1lJTkZsbmFXNUUiLCJtYWMiOiIxNDk2MDc5NTRiMmVhNjY4YWVmMGFiMTkyMTdhZTkyMmQxYzgxMDRjNjVjZDE4MmMyZjMwOTlkZjFiNTZlZTYyIiwidGFnIjoiIn0%3D;"
