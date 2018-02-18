from lxml import html
import requests

# https://cryptoping.tech/
# http://docs.python-guide.org/en/latest/scenarios/scrape/

DEFAULT = {'Cointelegraph' : 'https://cointelegraph.com/'}
                    # 'zerohedge' : ''}

#region scrapper functions
def tree_from_html(url: str):
    page = requests.get(url)
    return html.fromstring(page.content)

def forest(trees: dict):
    pass





#endregion

