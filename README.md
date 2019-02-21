# Recruitment task

Python Intern Task - Web Crawler

Clarence got lost while surfing the internet. Help him find his way out by creating a map of the domain he is on.

Write a function site_map(url) that takes a site URL as an argument and creates a mapping of that domain as a Python dictionary. The mapping should contain all the accessible pages within that domain. Every entry should consist of: * key: URL * value: dictionary with: ** site title (HTML <title> tag) ** links - set of all target URLs within the domain on the page but without anchor links

Example: Confused? Worry not! Here is an example site with a map. Unzip the example.zip file into some directory and enter it. Run the following command python3 -m http.server. You are serving a website now! Check if everything is okay by visiting the http://0.0.0.0:8000 URL. If everything works you can run your program with following parameter and verify if it gives the correct answer.

# What is Web-Crawler?

This little file named crawler.py contain function site_map, which can help Clarence find his way out.

## What should Clarence do to use it?
1. Just run your shell, find path where you have your crawler.py and use Python.
2. Import 'map_site' function.
3. Use map_site function, for example:<br />
site_map('http://0.0.0.0:8000/')<br />
4. And here you go Clarence! I hope that this will help you!

