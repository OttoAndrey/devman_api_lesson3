import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from requests.exceptions import HTTPError


def get_link_info(token, bitlink):
    bitlink_by_parts = urlparse(bitlink)
    bitlink_without_http = ''.join(bitlink_by_parts[1:])
    info_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_without_http}'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(info_url, headers=headers)
    response.raise_for_status()
    
    return response.json()


def get_shorten_link(token, url):
    shorten_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {token}'}
    data = {"long_url": url}

    response = requests.post(shorten_url, headers=headers, json=data)
    response.raise_for_status()  

    return response.json()['link']


def get_count_clicks(token, bitlink):
    bitlink_by_parts = urlparse(bitlink)
    bitlink_without_http = ''.join(bitlink_by_parts[1:])
    total_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_without_http}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(total_clicks, headers=headers)
    response.raise_for_status()
    
    return response.json()['total_clicks']


def main():
    load_dotenv()

    token = os.getenv("BITLY_TOKEN")

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Ссылка, которую надо сократить или посчитать кол-во переходов')
    args = parser.parse_args()
    url = args.url

    try:
        get_link_info(token, url)
        count_clicks = get_count_clicks(token, url)
        print(f'По вашей ссылке прошли {count_clicks} раз(а)')
    except HTTPError:
        try:
            short_url = get_shorten_link(token, url)
            print(f'Короткая ссылка: {short_url}')
        except HTTPError:
            print('Такой ссылки нет!')


if __name__ == '__main__':
    main()
