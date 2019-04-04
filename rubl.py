#!/usr/bin/python3
## -*- coding: utf-8 -*-
# send character-string to enable UTF-8 mode

import requests
from bs4 import BeautifulSoup
import os



def get_html():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    r = requests.get('https://www.cbr.ru', headers=headers)
    return r.text

def get_price(html):
    soup = BeautifulSoup(html, 'lxml')
    price = soup.find('ins', text='$').find_parent('tr').find('td', class_='weak').text.split('.')[1].strip()
    return price

def send_message(title, message):
    os.system('notify-send "{}" "{}"'.format(title, message))



def main():
    message = get_price(get_html())
    title = 'USD/RUB'
    send_message(title, message)


if __name__ == '__main__':
    main()