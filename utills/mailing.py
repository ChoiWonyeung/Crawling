from datetime import date
import requests
import json


def alert(problem, mail):
    maillist = [
        "wonyeong@coconutsilo.com",
        "yunsu@coconutsilo.com",
    ]
    for i in maillist:
        data = {
            "to": str(i),
            "subject": str(date.today()) + " 정부지원사업 크롤러 2nd 수정 필요",
            "text": str(problem),
        }
        requests.post(
            "https://www.coconutsilo.com/mail/private",
            data=json.dumps(data, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )


def good():
    maillist = ["wonyeong@coconutsilo.com", "yunsu@coconutsilo.com"]
    for i in maillist:
        data = {
            "to": str(i),
            "subject": str(date.today()),
            "text": "굿",
        }
        requests.post(
            "https://www.coconutsilo.com/mail/private",
            data=json.dumps(data, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
