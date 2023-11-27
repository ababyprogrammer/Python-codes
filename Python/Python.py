import time
import datetime
import requests
import threading
from random import randint
from lxml import html
from operator import itemgetter

def login(user, password):
    payload = {
        'login': user,
        'password': password,
        'autologin': 1,
        'return_ssl': 1,
        'timezone': '-60'
    }
    with requests.Session() as s:
        r = s.post('https://my.bukalapak.com/auth/signin', data=payload)
        return s

def get_item_ids(user_id):
    item_ids = []
    page = 1
    while True:
        r = s.get(f'https://my.bukalapak.com/inventory?page={page}')
        tree = html.fromstring(r.content)
        item_links = tree.xpath('//div[@class="list-product-box"]/a/@href')
        if not item_links:
            break
        for link in item_links:
            item_id = link.split('/')[-1]
            item_ids.append(item_id)
        page += 1
    return item_ids

def get_item_data(item_id):
    r = s.get(f'https://my.bukalapak.com/products/{item_id}/edit')
    tree = html.fromstring(r.content)
    title = tree.xpath('//input[@id="product_name"]/@value')[0]
    price = int(tree.xpath('//input[@id="product_price"]/@value')[0])
    return {'id': item_id, 'title': title, 'price': price}

def calculate_daily_earnings(items):
    total_earnings = 0
    for item in items:
        daily_sales = randint(0, 50)
        item['daily_sales'] = daily_sales
        daily_earnings = daily_sales * item['price']
        total_earnings += daily_earnings
    return total_earnings

def process_user(user):
    print(f"Processing user: {user['user']}")
    session = login(user['user'], user['password'])
    global s
    s = session
    item_ids = get_item_ids(user['user_id'])
    items = []
    for item_id in item_ids:
        item_data = get_item_data(item_id)
        items.append(item_data)
    daily_earnings = calculate_daily_earnings(items)
    print(f"Daily earnings: {daily_earnings}")
    time.sleep(randint(5, 10))

users = [
    {'user': 'user1', 'password': 'password1', 'user_id': 1},
    {'user': 'user2', 'password': 'password2', 'user_id': 2},
    {'user': 'user3', 'password': 'password3', 'user_id': 3}
]

for user in users:
    process_user(user)