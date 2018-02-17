from lxml import html
import requests

# https://cryptoping.tech/

DEFAULT = {'Cointelegraph' : 'https://cointelegraph.com/'}
                    # 'zerohedge' : ''}

#region scrapper functions
def tree_from_html(url):
    page = requests.get(url)
    return html.fromstring(page.content)

def forest(trees: dict):
    pass
    




#endregion

