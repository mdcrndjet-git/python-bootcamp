from concurrent.futures.thread import ThreadPoolExecutor

import requests
import time

def fetch_url(url):
    return requests.get(url)

#with ThreadPoolExecutor() as executor:
 #   outputs = executor.map(fetch_url, inputs)