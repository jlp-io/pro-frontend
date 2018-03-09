import requests
from bs4 import BeautifulSoup


def scrape(ticker):
    """
    Scrapes recent news and company description from nasdaq.com
    :param ticker: Ticker Symbol entered by user.
    :return: List of tuples (news_text, news_link), list of company description paragraph and string of company name.
    """
    # send request to nasdaq.com
    url = "https://www.nasdaq.com/symbol/"
    raw = requests.get(url + ticker)
    soup = BeautifulSoup(raw.text, 'lxml')
    # search company name
    name_div = soup.find('div', id='qwidget_pageheader')
    try:
        name = name_div.find("h1").text
    except AttributeError:
        # Failed to find matching stock
        return None, None, None
    name = name[:-34]  # found case of rstrip() not working correctly
    # search news
    news_div = soup.find('div', id='CompanyNewsCommentary')
    news_list = news_div.findAll('li')
    return_news = []
    for news_li in news_list:
        news_a = news_li.find('a')
        text_link_tup = (news_a.text.lstrip().rstrip(), news_a["href"])
        return_news.append(text_link_tup)
    # search description
    bio_div = soup.find('div', id="company-description")
    if bio_div is None:
        return return_news, None, name
    bio_plist = bio_div.findAll('p')
    return_desc = []
    for p in bio_plist:
        return_desc.append(p.text)
    return return_news, return_desc, name