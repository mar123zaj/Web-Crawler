from crawler import validated, validated_link, page_properties, map_page, map_site
from urllib.parse import urlparse



def test_site_map():
    pass


def test_url_validated0():
    input_ = 'abcd'
    assert validated(input_) == False
 
def test_url_validated1():
    input_ = 'https://docs.python.org/3/whatsnew/3.7.html'
    assert validated(input_) == True

def test_validated_link0():
    link1 = '/CodingDojoSilesia/bank-ocr'
    domain_url = 'https://github.com'
    assert validated_link(link1, domain_url) == 'https://github.com/CodingDojoSilesia/bank-ocr'


def test_validated_link0():
    link1 = 'https://www.facebook.com/user123'
    domain_url = 'https://github.com'
    assert validated_link(link1, domain_url) == 'https://www.facebook.com/user123'


def test_page_properties():
    page_url = 'http://www.madore.org/~david/.test/uni.html' # small page for testing purposes
    parsed_url = urlparse(page_url)
    domain = '{parsed_url.scheme}://{parsed_url.netloc}'
    netloc = parsed_url.netloc
    assert page_properties(page_url, domain, netloc) == [set(), 'A small test page']


def test_map_page():
    page_url = 'http://www.madore.org/~david/.test/uni.html' # small page for testing purposes
    parsed_url = urlparse(page_url)
    domain = '{parsed_url.scheme}://{parsed_url.netloc}'
    netloc = parsed_url.netloc
    assert map_page(page_url, domain, netloc) == {'http://www.madore.org/~david/.test/uni.html': {
                                                                                        'title': 'A small test page',                                                                                         
                                                                                        'links': set()}
                                                                            }


def test_map_site():
    input_ = 'http://localhost:8000/'
    assert map_site(input_) == {'http://localhost:8000': {'title': 'Index', 'links': {'http://localhost:8000/site.html', 'http://localhost:8000/example.html'}}, 'http://localhost:8000/site.html': {'title': 'The Site', 'links': {'http://localhost:8000/site/subsite.html'}}, 'http://localhost:8000/example.html': {'title': 'No links here', 'links': set()}, 'http://localhost:8000/site/subsite.html': {'title': 'Looping', 'links': {'http://localhost:8000/site/other_site.html', 'http://localhost:8000/'}}, 'http://localhost:8000/site/other_site.html': {'title': 'Looped', 'links': {'http://localhost:8000/site/subsite.html'}}, 'http://localhost:8000/': {'title': 'Index', 'links': {'http://localhost:8000/site.html', 'http://localhost:8000/example.html'}}}
