import sys
from crawler.crawler import Crawler


def run():
    crawler = Crawler(sys.argv[1])
    crawler.run()
