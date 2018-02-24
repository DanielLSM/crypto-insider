from lxml import html, etree
import requests

# https://cryptoping.tech/
# http://docs.python-guide.org/en/latest/scenarios/scrape/

DEFAULT_URLS = {'cointelegraph': 'https://cointelegraph.com/'}
# 'zerohedge' : ''}

DEFAULT_NEWS_XPATHS = {'cointelegraph': '//*[@id="js-main-slideshow-pager"]'}

NUMBER_OF_NEWS = 4


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
    page = []
    for new in xpaths.keys():
        for i in range(NUMBER_OF_NEWS):
            import pdb
            pdb.set_trace()
            element = forest[new].xpath(xpaths[new] + '/div[{}]'.format(i))
            page.append(etree.tostring(element[0]))
        news[new] = page
    return news


def get_news(urls={}, xpaths={}):

    if not urls: urls = DEFAULT_URLS
    if not xpaths: xpaths = DEFAULT_NEWS_XPATHS

    garden = forest(urls)
    news = process_xpaths(garden, xpaths)


if __name__ == '__main__':
    # news = get_news()

    tree = tree_from_html('https://cointelegraph.com/')
    data = tree.xpath('//*[@id="js-main-slideshow-pager"]/div[2]/div[1]//h3')
    strings = etree.tostring(data[0], pretty_print=True)
    print(etree.tostring(data[0], pretty_print=True))
