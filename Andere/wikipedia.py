from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                html = BeautifulSoup(resp.content, 'html.parser')
                allLinks = []
                while len(allLinks) == 0:
                    for div in html.select('div'):
                        try:
                            if len(allLinks) > 0:
                                break
                            if div['id'] == "mw-content-text":
                                for p in div.select('p'):
                                    if len(allLinks) > 0:
                                        break
                                    for a in p.select('a'):
                                        if a['href'] != "" or a['class'] != "mw-selflink selflink":
                                            allLinks.append(a)
                                            break

                        except:
                            print("", end="")
                #print(allLinks)
                return "https://en.wikipedia.org" + allLinks[0]['href']

            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

steps = 0
link = 'https://en.wikipedia.org/wiki/Podcast'
while "epistemic" not in link.lower():
    steps += 1
    link = simple_get(link)
    if link == "https://en.wikipedia.org/wiki/Greek_language":
        link = "https://en.wikipedia.org/wiki/Indo-European_languages"
    print(steps, link)

