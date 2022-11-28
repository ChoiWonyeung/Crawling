import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {
    "Cookie": ".ASPXANONYMOUS=wxvOLgHT650K3K6xK34RDGDhtwJ4r1tLcU3GSslaOAN8EL9LqR5ixT3xZvmKTFuSUdsty4NiZFa59AuME5M2C5K0B5MVCTIwPhxrM6pqHZGXYri60; ASP.NET_SessionId=jylk2eszrkg3v05vyxkiveie; dnn_IsMobile=False; language=en-US"
}


def just_requests(url):
    return requests.get(url, verify=False, headers=headers)


def get_html(url):
    return BeautifulSoup(
        requests.get(url, verify=False, headers=headers).text, "html.parser"
    )


def get_json(url):
    return requests.get(url, verify=False, headers=headers).json()


def post_html(url, data):
    return BeautifulSoup(
        requests.post(url, verify=False, headers=headers, data=data).text, "html.parser"
    )


def post_json(url, data, header):
    if header == None:
        headers = header
    else:
        headers = header
    return requests.post(url, verify=False, headers=headers, data=data).json()
