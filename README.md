# Panopto Scraper
Scrapes videos from [Panopto](https://www.panopto.com/) folders.

# Dependencies
1) Install [Chrome](https://www.google.com/chrome/)
2) Install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and include it in your `PATH`. 

On macOS, run:
```
brew install chromedriver
```

On Linux, run:
```
sudo apt install chromium-chromedriver
```

3) Install [Python](https://www.python.org/downloads/) and run:
```
pip3 install requests
pip3 install selenium
```

# Running
To run:

```
python3 scraper.py <url of Panopto folder 1> <url of Panopto folder 2> ... <url of Panopto folder n>
```

For example:

```
python3 scraper.py "https://st-andrews.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%224e1b0a53-e3da-4240-8cae-ud0870a9uc6d%22&maxResults=250"
```

Once the program starts, you simply need to login to Panopto in the Chrome window that opens and then press `enter` to notify the program to continue. Only the results displayed on the first page of each respective folder will be scraped. It is assumed that the login credentials are valid for all folders provided.
