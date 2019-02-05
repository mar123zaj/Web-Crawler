import mechanize
import urllib.parse
from urllib.parse import urlparse


def is_not_absolute(url):
    if '//' not in url:
        return True
    else:
        return False


def map(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    try:
        br.open(url)
    except:
        return {}
    # Gives url of hostname
    parsed_uri = urlparse(url)
    host_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    list_url = [host_url]
    for link_item in list_url:
        br.open(link_item)
        for link in br.links():
            link = link.url
            if is_not_absolute(link):
                link = urllib.parse.urljoin(host_url, link)
            if '{uri.netloc}/'.format(uri=parsed_uri) in link and link not in list_url:
                    list_url.append(link)
    my_dict = {

    }
    for page in list_url:
        br.open(page)
        title = br.title()
        links = set()
        for link in br.links():
            link = link.url
            if is_not_absolute(link):
                link = urllib.parse.urljoin(host_url, link)
            if '{uri.netloc}/'.format(uri=parsed_uri) in link:
                links.add(link)

        dict_item = {
            page: {
                'title': title,
                'links': links}
        }
        my_dict.update(dict_item)
    return my_dict
