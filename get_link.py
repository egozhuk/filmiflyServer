import base64
import requests
import time
import json
from itertools import product

BASE_URL = 'http://hdrezka8jhspw.org/ajax/get_cdn_series/?t={}'

def clearTrash(data):
    trashList = ["@", "#", "!", "^", "$"]
    trashCodesSet = []
    for i in range(2, 4):
        startchar = ''
        for chars in product(trashList, repeat=i):
            data_bytes = startchar.join(chars).encode("utf-8")
            trashcombo = base64.b64encode(data_bytes)
            trashCodesSet.append(trashcombo)

    arr = data.replace("#h", "").split("//_//")
    trashString = ''.join(arr)

    for i in trashCodesSet:
        temp = i.decode("utf-8")
        trashString = trashString.replace(temp, '')

    finalString = base64.b64decode(trashString + "==")
    return finalString.decode("utf-8")


def get_urls(film_id):
    payload = {'id': film_id,
               'translator_id': '1',
               #'season': season,
               #'episode': episode,
               'action': 'get_movie'}  # get_stream
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    r = requests.post(BASE_URL.format(str(int(time.time()))), data=payload, headers=headers)
    if r.status_code != 200:
        print('Ошибка')
        return

    data = json.loads(r.text)

    if data.get('success') != True:
        print('Ошибка')
        print(data)
        return

    return data['url']


if __name__ == '__main__':
    # all_urls = get_urls(67998, 1, 1)
    all_urls = get_urls(52755)
    print(clearTrash(all_urls))
