from pprint import pprint
import requests
import json
API_ENDPOINT = 'https://p-tracker.herokuapp.com/api/grailed_teddies'
#API_ENDPOINT = 'http://127.0.0.1:5000/api/grailed_teddies'

### TODO: PUT THE PARAMS AT THE TOP SO YOU CAN SEARCH FOR ANY CLOTHING PIECE YOU WNAT!! ###

items = []
page_num = 0

#Turns item info from 'parse_data' to dictionary
def JSONify(title, designer, price, followers, listing_id):
    item_json = {
        "title": title,
        "designer": designer,
        "price": price,
        "followers": followers,
        "listing_id": listing_id
        }
    return item_json

#Takes response data from 'load_next' and digs through it
def parse_data(response):
    for item in response['hits']:
        price = float(item['price'])
        title = item['title']
        designer = item['designer_names']
        followers = item['followerno']
        listing_id = item['cover_photo']['listing_id']
        item_json = JSONify(title, designer, price, followers,listing_id)
        items.append(item_json)
        #print(item_json)

#returns Reponse from current page and loads next page
def load_next():
    global page_num
    URL_ONE = 'https://mnrwefss2q-dsn.algolia.net/1/indexes/Listing_production/query?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.21.1&x-algolia-application-id=MNRWEFSS2Q&x-algolia-api-key=a3a4de2e05d9e9b463911705fb6323ad'
    params = f"{{\"params\":\"query=saint%20laurent%20teddy&filters=(strata%3A\'grailed\'%20OR%20strata%3A\'hype\'%20OR%20strata%3A\'sartorial\'%20OR%20strata%3A\'basic\')%20AND%20(marketplace%3Agrailed)&hitsPerPage=80&facets=%5B%22strata%22%2C%22size%22%2C%22category%22%2C%22category_size%22%2C%22category_path%22%2C%22category_path_size%22%2C%22category_path_root_size%22%2C%22price_i%22%2C%22designers.id%22%2C%22location%22%2C%22marketplace%22%5D&page={page_num}\"}}" 
    json_params=json.loads(params)
    response = requests.post(URL_ONE, json=json_params).json()
    index_checker = response['hits'][0]['price']
    page_num += 1
    return response

while True:
    try:
        response = load_next()
        parse_data(response)
        
    except IndexError:
        max_page = page_num-1
        print("out of index")
        print('the final page is ' + str(max_page))
        break

requests.post(API_ENDPOINT, json=items)