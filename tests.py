from crawler import (
    is_validated,
    make_url_absolute,
    filtered_out_links,
    updated_urls_list,
    page_title,
    page_links,
    site_map,
)
import mechanize

def test_is_validated_True_case():
    """ Test case for validated link. """
    input_ = "https://mail.google.com/mail/"
    assert is_validated(input_) != ''


def test_is_validated_False_case():
    """ Test case for not validated link. """
    input_ = "google.com"
    assert is_validated(input_) == ''


def test_make_url_absolute_aboslute_input():
    """ Test case for absolute link as input. """
    url = "https://github.com/mar123zaj/Web-Crawler"
    domain_address = "https://github.com"
    assert (
        make_url_absolute(url, domain_address)
        == "https://github.com/mar123zaj/Web-Crawler"
    )


def test_make_url_absolute_relative_input():
    """ Test case for relative link as input. """
    url = "/mar123zaj/Web-Crawler"
    domain_address = "https://github.com"
    assert (
        make_url_absolute(url, domain_address)
        == "https://github.com/mar123zaj/Web-Crawler"
    )


def test_filtered_out_links():
    links_set = {
        "http://localhost:8000/example.html",
        "http://localhost:8000/site.html",
        "https://clearcode.pl/kariera/staze/",
    }
    domain_name = "http://localhost:8000/"
    assert filtered_out_links(links_set, domain_name) == {
        "http://localhost:8000/example.html",
        "http://localhost:8000/site.html",
    }


def test_updated_urls_list():
    urls_list = [
        "http://localhost:8000/",
        "http://localhost:8000/example.html",
        "http://localhost:8000/site.html",
    ]
    links_list = [
        "http://localhost:8000/site/subsite.html",
        "http://localhost:8000/example.html",
        "http://localhost:8000/site/other_site.html",
    ]
    assert updated_urls_list(urls_list, links_list) == [
        "http://localhost:8000/",
        "http://localhost:8000/example.html",
        "http://localhost:8000/site.html",
        "http://localhost:8000/site/subsite.html",
        "http://localhost:8000/site/other_site.html",
    ]


def test_page_title():
    input_ = "http://localhost:8000/site/other_site.html"
    br = mechanize.Browser()
    br.open(input_)
    assert page_title(br) == "Looped"


def test_page_links():
    link = "http://localhost:8000/site/subsite.html"
    br = mechanize.Browser()
    br.open(link)
    
    assert page_links(br) == {
        "http://localhost:8000/site/other_site.html",
        "http://localhost:8000/site/other_site.html",
        "http://localhost:8000/",
    }


def test_site_map_not_proper_input():
    """ Test case for not proper input. """
    input_ = "google.com"
    assert site_map(input_) == "URL wasn't valid!"


def test_site_map_proper_input():
    """ Test case for proper input. """
    input_ = "http://localhost:8000"
    assert site_map(input_) == {
        "http://localhost:8000": {
            "title": "Index",
            "links": {
                "http://localhost:8000/site.html",
                "http://localhost:8000/example.html",
            },
        },
        "http://localhost:8000/site.html": {
            "title": "The Site",
            "links": {"http://localhost:8000/site/subsite.html"},
        },
        "http://localhost:8000/example.html": {
            "title": "No links here",
            "links": set(),
        },
        "http://localhost:8000/site/subsite.html": {
            "title": "Looping",
            "links": {
                "http://localhost:8000/site/other_site.html",
                "http://localhost:8000/",
            },
        },
        "http://localhost:8000/site/other_site.html": {
            "title": "Looped",
            "links": {"http://localhost:8000/site/subsite.html"},
        },
        "http://localhost:8000/": {
            "title": "Index",
            "links": {
                "http://localhost:8000/site.html",
                "http://localhost:8000/example.html",
            },
        },
    }
