from lxml import html, etree
import requests

# https://cryptoping.tech/
# http://docs.python-guide.org/en/latest/scenarios/scrape/

DEFAULT_URLS = {'cointelegraph': 'https://cointelegraph.com/'}
# 'zerohedge' : ''}

DEFAULT_NEWS_XPATHS = {'cointelegraph': '//*[@id="js-main-slideshow-pager"]'}


def tree_from_html(url: str):
    page = requests.get(url)
    return html.fromstring(page.content)


def forest(trees: dict):
    forest = {}
    for tree in trees.keys():
        forest[tree] = tree_from_html(trees[tree])
    return forest


def process_xpaths(forest: dict, xpaths: dict):
    news = {}
    for new in xpaths.keys():
        pages = []
        book = forest[new].xpath(xpaths[new] + '//h3')
        for page in book:
            pages.append(
                etree.tostringlist(page, encoding='unicode', method='text')[0])
        news[new] = pages
    return news


def get_news(urls={}, xpaths={}):

    if not urls: urls = DEFAULT_URLS
    if not xpaths: xpaths = DEFAULT_NEWS_XPATHS

    garden = forest(urls)
    return process_xpaths(garden, xpaths)


if __name__ == '__main__':
    # news = get_news()

    tree = tree_from_html('https://cointelegraph.com/')
    data = tree.xpath('//*[@id="js-main-slideshow-pager"]//h3')
    news = []
    for new in data:
        news.append(
            etree.tostringlist(new, encoding='unicode', method='text')[0])

    breaking_news = get_news()
