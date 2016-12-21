from urllib.request import Request, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer


class Crawler(object):
    def __init__(self, target):
        self.target = target
        self.root_parse = urlparse(self.target)
        self.visited = set()
        self.queue = []

    def read_page(self, url):
        req = Request(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
        return urlopen(req).read()

    def is_url_internal(self, url):
        url_parse = urlparse(url)
        if url_parse.netloc == '' or url_parse.netloc == self.root_parse.netloc:
            return url_parse.path.startswith(self.root_parse.path)
        else:
            return False

    def make_canonical(self, url):
        url_parse = urlparse(url)
        if url_parse.netloc == '':
            url_parse._replace(netloc=self.root_parse.netloc)
        return url_parse.geturl()

    def is_url_relevant(self, url):
        url_parse = urlparse(url)
        # only parse URLs that point to full pages
        return url_parse.fragment == ''

    def add_to_queue(self, url):
        if self.is_url_relevant(url):
            url = self.make_canonical(url)
            if url in self.visited:
                return
            if url in self.queue:
                return
            self.queue.append(url)

    def process_url(self, url):
        self.on_visit(url)
        response = self.read_page(self.target)
        for link in BeautifulSoup(response, "html.parser", parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                url = link['href']
                if self.is_url_internal(url):
                    # internal links
                    self.add_to_queue(url)
                    self.on_internal(url)
                else:
                    # external links
                    self.on_external(url)

    def run(self):
        self.process_url(self.target)
        while len(self.queue) > 0:
            url = self.queue[0]
            self.process_url(url)
            self.visited.add(url)
            self.queue = self.queue[1:]

    # override to create a specific behavior
    def on_visit(self, url):
        print('visiting: %s {%s pages visited; %s queued to visit}' % (url, len(self.visited), len(self.queue)))

    # override to create a specific behavior
    def on_internal(self, url):
        pass

    # override to create a specific behavior
    def on_external(self, url):
        print('[EXTERNAL LINK] %s' % url)


if __name__ == '__main__':
    crawler = Crawler('http://astroblogger.blogspot.de/')
    crawler.run()
