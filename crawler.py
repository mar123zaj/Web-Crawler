import mechanize
import sys
import pprint
import collections
from urllib.parse import urljoin, urlparse


def is_validated(url):
    """Checks if given url is proper."""
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        return True
    else:
        return False


def make_url_absolute(url, domain_full_address):
    """Check if link is relative and make it absolute."""
    if "//" not in url:
        return urljoin(domain_full_address, url)
    else:
        return url


def domain_tuple(url):
    """Returns namedtuple with full domain address and domain name of given url."""
    parsed_url = urlparse(url)
    Domain = collections.namedtuple("Domain", "full_address, name")
    return Domain(f"{parsed_url.scheme}://{parsed_url.netloc}", parsed_url.netloc)


def page_title(url):
    """Returns title of given url."""
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.open(url)
    return browser.title()


def page_links(url):
    """Returns all links from given page."""
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.open(url)
    domain = domain_tuple(url)
    links = set()
    for link in browser.links():
        link = make_url_absolute(link.url, domain.full_address)
        links.add(link)
    return links


def filtered_out_links(links, domain_name):
    """Returns set of links that are only links from given domain."""
    filtered_links = set()
    # Check if link is not link to external site
    for link in links:
        if domain_name in link:
            filtered_links.add(link)
    return filtered_links


def updated_urls_list(urls, links):
    """Upade urls list with new links."""
    for link in links:
        if link not in urls:
            urls.append(link)
    return urls


def site_map(url):
    """Returns dictionary which will return page title and links of page from given domain."""
    if is_validated(url):
        domain = domain_tuple(url)
        urls = [domain.full_address]
        site_mapping = dict()

        # Loop through pages from our domain
        for page_url in urls:
            all_links = page_links(page_url)
            links = filtered_out_links(all_links, domain.name)
            title = page_title(page_url)
            site_mapping.update({page_url: {"title": title, "links": links}})

            urls = updated_urls_list(urls, links)
        return site_mapping
    else:
        return "URL wasn't valid!"


if __name__ == "__main__":
    arg = sys.argv[1]
    pprint.pprint(site_map(arg))
