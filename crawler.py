import mechanize
import urllib.parse


def is_not_absolute(url):
    # Check if url is an absolute or not
    if '//' not in url:
        return True
    else:
        return False


def map_site(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    try:
        br.open(url)
    except:
        return "Given url wasn't valid."
    # Gives url of hostname, so given url can be any subpage of domain
    parsed_uri = urllib.parse.urlparse(url)
    host_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    list_url = [host_url]
    my_dict = {}
    # Loop through pages from our domain
    for list_item in list_url:
        br.open(list_item)
        links = set()
        # Loop through urls from specific page
        for link in br.links():
            link = link.url
            if is_not_absolute(link):
                link = urllib.parse.urljoin(host_url, link)
            # Check if link is not link to external site
            if '{uri.netloc}/'.format(uri=parsed_uri) in link:
                links.add(link)
                if link not in list_url:
                    list_url.append(link)
        dict_item = {
            list_item: {
                'title': br.title(),
                'links': links}
            }
        my_dict.update(dict_item)
    return my_dict
