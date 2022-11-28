from importlib import import_module
from utills import mailing, setting


class Crawler:
    def __init__(self, site, keywords):
        self.site = site
        self.keyword = keywords
        self.keep, self.email_account = setting.custom()
        self.error_list = []

    def main_crawling(self):
        for site in self.site:
            try:
                import_module(f"sites.{site}.main").main(site, self.keyword)
            except Exception as problem:
                mailing.alert(problem, self.email_account)


if __name__ == "__main__":
    site_list = [
        "naver"
    ]
    keyword = '가방'
    Crawler(site_list, keyword).main_crawling()

