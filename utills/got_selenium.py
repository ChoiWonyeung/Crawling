import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "WMONID=Q3MYPj687gO; JSESSIONID=oBRlGfRVPX4nlSigU4OnT1KjX3l0UV2kFuhTl94JJgVgo5gqbsfAiI3EvyqQlUu1.amV1c19zY2hvb2xpbmZvL21vZS1zbHdhczJfY29udGFpbmVyMw==; WMONID=V3FrHlX1C2L",
    "Host": "www.naver.com",
    "Referer": "https://www.naver.com",
    "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.126 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}


def driver():
    return webdriver.Chrome(
        chromedriver_autoinstaller.install(), chrome_options=Options()
    )
