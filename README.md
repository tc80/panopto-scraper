# Panopto Scraper
Scrapes videos from [Panopto](https://www.panopto.com/) folders.

# Dependencies
1) Install [Chrome](https://www.google.com/chrome/)
2) Install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and include in your `PATH`. On macOS, simply run:
```
brew install chromedriver
```

3) Install [Python](https://www.python.org/downloads/) and run:
```
pip3 install requests
pip3 install selenium
```

# Running
To run:

```
python3 scraper.py <url of Panopto folder>
```

For example:

```
python3 scraper.py "https://st-andrews.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%224e1b0a53-e3da-4240-8cae-ud0870a9uc6d%22&maxResults=250"
```

Once the program starts, you simply need to login to Panopto in the Chrome window that opens and then press enter in the program.