import time
import random
import requests


def get_html(url_page):
    print(f'Get html for {url_page}')
    t1 = time.time()
    html_page = requests.get(url_page, timeout=15).content
    t2 = time.time()
    print(f'Got html for {url_page}')
    sleep_time = random.uniform(1, 3.5)
    print(f'Request time: {t2-t1}, Sleep time:{sleep_time}')
    time.sleep(sleep_time)
    return html_page
