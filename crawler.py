import mechanize
import sys
import pprint
from collections import namedtuple
from urllib.parse import urljoin, urlparse


def is_validated(url):
    """Checks if given url is proper."""
    parsed_url = urlparse(url)
    return parsed_url.scheme and parsed_url.netloc


def make_url_absolute(url, domain_full_address):
    """Check if link is relative and make it absolute."""
    if "//" not in url:
        return urljoin(domain_full_address, url)
    else:
        return url


def domain_tuple(url):
    """Returns namedtuple with full domain address and domain name of given url."""
    parsed_url = urlparse(url)
    Domain = namedtuple("Domain", "full_address, name")
    return Domain(f"{parsed_url.scheme}://{parsed_url.netloc}/", parsed_url.netloc)


def page_title(browser):
    """Returns title of given url."""
    return browser.title()


def page_links(browser):
    """Returns all links from given page."""
    url = browser.geturl()
    parsed_url = urlparse(url)
    url_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
    links = set()
    for link in browser.links():
        link = make_url_absolute(link.url, url_domain)
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


def site_dictionary(urls, domain_name, output_dict=None):
    """Returns dictionary which will return page title and links of page from given domain."""
    if output_dict is None:
        output_dict = dict()
    if urls:
        new_urls = []
        for url in urls:
            if url not in output_dict:
                browser = mechanize.Browser()
                browser.open(url)
                all_links = page_links(browser)
                domain_links = filtered_out_links(all_links, domain_name)
                title = page_title(browser)
                output_dict.update({url: {"title": title, "links": domain_links}})
                new_urls += list(domain_links)
        return site_dictionary(new_urls, domain_name, output_dict=output_dict)
    else:
        return output_dict


def site_map(url):
    """Checks if given url is proper, gets domain of given url
        and returns dictionary with all urls, titles and links of pages."""
    if is_validated(url):
        domain = domain_tuple(url)
        urls = [domain.full_address]
        return site_dictionary(urls, domain.name)
    else:
        return "URL wasn't valid!"


if __name__ == "__main__":
    arg = sys.argv[1]
    pprint.pprint(site_map(arg))
