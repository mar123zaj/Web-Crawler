import mechanize
from collections import namedtuple
from urllib.parse import urljoin, urlparse

def validated(url):
    '''Checks if given url is proper.'''
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    try:
        browser.open(url)
        return True
    except:
        return False

def validated_link(link, host_url):
    '''Check if link is relative and make it absolute.'''
    if '//' not in link:
        return urljoin(host_url, link)
    else:
        return link
 
 
def page_properties(page_url, domain, netloc):
    '''Returns page properties:
        all links from specific domain and page title.'''
    
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.open(page_url)
    links = set()
    for link in browser.links():
        link = validated_link(link.url, domain)
        # Check if link is not link to external site
        if netloc in link:
            links.add(link)
    return [links, browser.title()]


def map_page(page_url, domain, netloc):
    '''Returns dictionary of page properties and page url.'''
    links, title = page_properties(page_url, domain, netloc)

    return {
            page_url: {
                'title': title,
                'links': links}
            }


def map_site(url):
    '''Returns dictionary of all pages properties from specific domain.'''
    if validated(url):
        parsed_url = urlparse(url)
        Domain = namedtuple('Domain', 'domain, netloc')
        url = Domain(parsed_url.scheme + '://' + parsed_url.netloc,
                         parsed_url.netloc)
        urls = [url.domain, ]  # comma added for more clarity
        site_mapping = dict()
        # Loop through pages from our domain
        for url_ in urls:
            page_mapping = map_page(url_, url.domain, url.netloc)
            site_mapping.update(page_mapping)
            for link in page_mapping[url_]['links']:
                if link not in urls: urls.append(link)
        return site_mapping
    else:
        return "URL wasn't valid!"

#print(map_site('http://mar123zaj.pythonanywhere.com/'))
print(map_site('http://localhost:8000/'))
