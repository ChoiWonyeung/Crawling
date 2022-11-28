import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

import json
from datetime import datetime
import urllib3
import warnings

urllib3.disable_warnings()
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


class Crawler:
    def __init__(self):
        self.keyword = ""
        self.site = ""  # 수집 사이트
        self.startDate = ""  # 수집 시작일
        self.endDate = ""  # 수집 종료일
        self.url = "https://msearch.shopping.naver.com/search/all?exagency=true&frm=NVSHMDL&origQuery={keyword}&pagingIndex={page}&pagingSize=40&productSet=model&query={keyword}&sort=rel&viewType=lst"  # 수집할 게시물 리스트(게시판) url (검색조건(keyword, site, startDate, endDate)에 따라 설정)
        self.postUrls = []  # 게시판에서 게시물 url들을 담아 리턴할 리스트
        self.lastPage = 2  # 마지막 페이지 설정 네이버의 경우 상품 리스트가 40개가 안될시 마지막 페이지로 인식

    # 데이터에서 html tag 제외
    def delrn(self, text):
        return text.replace("<br>", "").replace("<em>", "").replace("</em>", "").replace("&amp;", "").replace("&nbsp;", "").replace("&gt;", "").replace("\t", "").replace("\n", "").replace("\r", "").replace("\xa0", "").lstrip().rstrip()

    def getList(self) -> list:
        # --- 첫페이지부터 마지막페이지까지
        for page in range(1, self.lastPage):
            req = requests.get(self.url.format(page=page, keyword=self.keyword), verify=False)

            req = json.loads(req.text.split('type="application/json">')[1].split('</script>')[0])

            req = json.loads(req['props']['pageProps']['initialState'])['compositeProducts']['list']

            print("[ * ] page -> " + str(page))
            for i in req:
                # 게시물 리스트 url 가져오기 <사이트마다 태그변경 또는 소스코드 수정 필요>
                postInfor = {
                    "url": "https://msearch.shopping.naver.com/catalog/"+i['item']['id'],
                    "title": i['item']['productName'],
                    "crawled": False,  # getPost()에서 해당url에서 게시물 상세정보를 가져왔는지 확인할 플래그
                    "Keyword":self.keyword,
                    "Price":i['item']['lowPrice']
                }
                # 수집되지 않은 url이면 append
                exist = next(
                    (item for item in self.postUrls if item["url"] == postInfor["url"]),
                    None,
                )
                if type(exist) != dict:
                    self.postUrls.append(postInfor)
                else:
                    break
            print("[ - ] lenPostUrls = ", len(self.postUrls))
            if len(req) < 40 :
                break

    def getPost(self) -> list:
        # 게시물 상세정보 수집 -> CSV 목록 순서
        for post in self.postUrls:
            req = requests.get(post["url"], verify=False)
            req = json.loads(req.text.split('type="application/json">')[1].split('</script>')[0])
            print("[ * ] post req -> " + post["url"])
            req = json.loads(req['props']['pageProps']['initialState'])
            post["url"] = 'https://search.shopping.naver.com/catalog/'+post['url'].split('/')[-1]
            # --- 게시물의 제목/내용/작성자아이디/작성자닉네임/작성일자 등을 가져옴 <사이트마다 태그변경 또는 소스코드 수정 필요>
            post["thumbnail"] = []
            for img in req['catalogImages']['catalogImages']:
                post["thumbnail"].append(img['imageUrl'])
            post["dateScraped"] = datetime.now().now().strftime("%Y-%m-%d %H:%M")
            # 이미지가 있다면
            post["catalog"] = []
            for img in req['specInfo']['catalogSpecImages']:
                post["catalog"].append('https://shopping-phinf.pstatic.net' + img['content'])

            post["Reviews"] = []
            reviewList = req['catalogReview']['reviews']
            for i in reviewList:
                # --- 댓글의 내용/작성자아이디/작성자닉네임/작성일자 등을 가져옴 <사이트마다 태그변경 또는 소스코드 수정 필요>
                reviewInfor = {
                    "userid": i['userId'],
                    "datePublished": i['registerDate'],
                    "Content": self.delrn(i['content']),
                    "image":[],
                }
                # 이미지가 있다면
                if i['imageCount'] != 0:
                    for img in i['images']:
                        reviewInfor["image"].append(img)
                post["Reviews"].append(reviewInfor)

            # # 해당 url 게시물 크롤링 완료
            post["crawled"] = True

    def getCSV(self):
        today = datetime.now().now().strftime("%Y%m%d%H%M")
        # CSV 저장 위치 설정
        pd.DataFrame(self.postUrls).to_csv("D:/" + today + self.keyword + "_" + self.site + ".csv",
                                           encoding="utf-8-sig")
        print("[ * ] getCSV terminated")

    def start_Crawling(self, keyword):
        self.keyword = keyword
        self.getList()
        self.getPost()

        return self.postUrls

