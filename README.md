# Recruitment task

Python Intern Task - Web Crawler

Clarence got lost while surfing the internet. Help him find his way out by creating a map of the domain he is on.

Write a function site_map(url) that takes a site URL as an argument and creates a mapping of that domain as a Python dictionary. The mapping should contain all the accessible pages within that domain. Every entry should consist of: * key: URL * value: dictionary with: ** site title (HTML <title> tag) ** links - set of all target URLs within the domain on the page but without anchor links

Example: Confused? Worry not! Here is an example site with a map. Unzip the example.zip file into some directory and enter it. Run the following command python3 -m http.server. You are serving a website now! Check if everything is okay by visiting the http://0.0.0.0:8000 URL. If everything works you can run your program with following parameter and verify if it gives the correct answer.

## How to use crawler.py?

Open your terminal and type `python crawler.py {url}`.

## How to test crawler module?

1. Download example.zip and unzip it on your computer.
2. Open terminal and navigate to \example directory.
3. Type `python -m http.server` to start serving testing website.
4. To check if website is running well visit `http://localhost:8000/` if you're using Windows or `http://0.0.0.0:8000` if you're using Linux.
5. Now you can get to work with testing. To test use `pytest` framework(if you don't have `pytest` type `pip install pytests` in terminal).
6. Write `pytest tests.py` in terminal and test crawler.py module.

