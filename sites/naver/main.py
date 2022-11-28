from utills import dataframe
from .NAVER import Crawler


def main(site, keyword):
    c = Crawler()
    data = c.start_Crawling(keyword)
    dataframe.to_csv(data, site, keyword)
