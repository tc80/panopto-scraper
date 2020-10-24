import sys
import os
import requests
from selenium import webdriver

if len(sys.argv) <= 1:
    print("\nExpecting argument for panopto directory.\n" +
          "Ex: python3 scraper.py \"https://st-andrews.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx#folderID=%224e1b0a53-e3da-4240-8cae-ud0870a9uc6d%22&maxResults=250\"\n")
    exit(1)

PANOPTO = "/Panopto/"
driver = webdriver.Chrome()

args = len(sys.argv[1:])
login = True
for i, url in enumerate(sys.argv[1:]):
    res = url.split(PANOPTO)

    if len(res) != 2:
        print(f"({i+1}/{args}) Invalid url, skipping...")
        continue

    driver.get(url)

    if login:
        # TODO: cache cookies
        input("Press enter after logging in...")
        login = False

    dirname = driver.find_element_by_id(
        'contentHeaderText').get_attribute('innerHTML')

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    lecs = driver.find_element_by_id(
        'detailsTable').find_elements_by_css_selector('.thumbnail-row.draggable')

    results = [(l.find_elements_by_class_name('detail-title')[0].find_elements_by_tag_name('span')
                [0].get_attribute('innerHTML'), l.get_attribute('id')) for l in lecs]

    # TODO: concurrent download
    for j, (title, uuid) in enumerate(results):
        print(f"({i+1}/{args} {j+1}/{len(results)}) Downloading '{title}'...", end='')
        p = f'{dirname}/{title}.mp4'
        if os.path.exists(p):
            print("exists")
            continue
        vid_url = f"{res[0]}{PANOPTO}Podcast/Social/{uuid}.mp4"
        driver.get(vid_url)
        download_url = driver.find_elements_by_tag_name(
            'source')[0].get_attribute('src')
        resp = requests.get(download_url)
        try:
            with open(p, 'wb') as f:
                f.write(resp.content)
            print("ok")
        except:
            print(f"fail: {sys.exc_info()[0]}")

driver.quit()
print("Done!")
