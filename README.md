## How to use crawler.py?

Open your terminal and type `python crawler.py {url}`.

## How to test crawler module?

1. Download example.zip and unzip it on your computer.
2. Open terminal and navigate to \example directory.
3. Type `python -m http.server` to start serving testing website.
4. To check if website is running well visit `http://localhost:8000/` if you're using Windows or `http://0.0.0.0:8000` if you're using Linux.
5. Now you can get to work with testing. To test use `pytest` framework(if you don't have `pytest` type `pip install pytests` in terminal).
6. Write `pytest tests.py` in terminal and test crawler.py module.
