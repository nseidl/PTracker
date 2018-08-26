from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import numpy
import requests
import time
import json

API_ENDPOINT = 'https://p-tracker.herokuapp.com/api/test_items'
# API_ENDPOINT = 'http://127.0.0.1:5000/api/test_items'

web_page = "https://www.bhphotovideo.com/c/buy/Digital-Cameras/ci/9811/N/4288586282"
page_response = requests.get(web_page, timeout=5)
soup = BeautifulSoup(page_response.content, "html.parser")

# Selenium/Chromedriver stuff #
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
# browser = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver', chrome_options=option)
#browser = webdriver.Chrome(executable_path='/Users/nseidl/chromedriver', chrome_options=option)
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)
browser.get("https://www.bhphotovideo.com/c/buy/Digital-Cameras/ci/9811/N/4288586282")

#Timeout handler #
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@data-selenium='imgLoad']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# activate the show 100 items per page dropdown #
dropdown = browser.find_elements_by_xpath("//p[@class='ns-selected-text ns-selected-option']")
dropdown[1].click()
view = browser.find_element_by_xpath("//a[@data-selenium='view100']")
view.click()

# scrape data!! #
# I put a pause so the button clicks don't break #
# How it works: goes through every item container on the page
# reparses the page, initializes the 'next click button' 
# and makes some containers (for the data that's hard to scrape)
# then it gathers the data and compiles into a dictionary
# Finally it goes onto the next page until there are no more pages
wait = WebDriverWait(browser, 10)

item_urls = []
items = []
num_pages = 0
next_page_exists = True

# Get website
website = "B&H Photo and Video"

# Get condition
condition = "new"

while next_page_exists:
    try :
        #Next page logic, waits for 'next' button to be clickable
        time.sleep(10)
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="pn-next pn-btn fifteen litGrayBtn"]')))
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        scraped_items = soup.find_all('div', {'data-selenium' : 'itemDetail'})

        for item in scraped_items:
            try:
                title = item.find('span', {'itemprop': 'name'}).text
                post_link = item.find('a', {'data-selenium' : 'itemHeadingLink'})['href']
                item_highlights = ""
                for highlight in item.find_all('li', {'class' : 'sellingPoint'}):
                    highlight = highlight.text.replace('\n','').replace('\t','')
                    item_highlights += highlight + '\n'
                img_link = item.find('img', {'data-selenium': 'imgLoad'})['src']
                price = item.find("span", {"data-selenium": "price"}).text
                price = price.strip(' \n\t').strip('$').replace("'", "").replace(",", "")  # remove the \n and \t tags

                item_json = {
                    "listing_name": title,
                    "post_link": post_link,
                    "post_description": item_highlights,
                    "website": website,
                    "condition": condition,
                    "price": price
                }

                if post_link not in item_urls:
                    item_urls.append(post_link)
                    items.append(item_json)
            except Exception as e:
                print(e)
                print(item)

        num_pages += 1
        print('done with page {}'.format(num_pages))
        browser.execute_script("arguments[0].click();", next_button)

    #break out if there are no more elements    
    except TimeoutException:
        next_page_exists = False

browser.close()
response = requests.post(API_ENDPOINT, json=items)
print(response.text)