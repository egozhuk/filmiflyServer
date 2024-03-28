import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        return response.text
    except requests.RequestException as e:
        print(f"Ошибка при получении HTML: {e}")
        return None

def extract_translators_titles_and_ids(html_content):
    titles_and_ids = {}

    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        translators_list = soup.select('ul#translators-list li')

        for translator in translators_list:
            title = translator.get('title')
            id_ = translator.get('data-translator_id')
            if title and id_:
                titles_and_ids[title] = id_
    except Exception as e:
        print(f"Ошибка: {e}")

    return titles_and_ids

# Пример использования
url = "https://hdrezka8jhspw.org/films/fiction/52755-avatar-put-vody-2022.html"
html_content = get_html_content(url)
if html_content:
    titles_and_ids = extract_translators_titles_and_ids(html_content)
    print(titles_and_ids)
