from requests import Session
from bs4 import BeautifulSoup
from loguru import logger

headers = {

    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) '
        'Gecko/20100101 Firefox/128.0'
}

url = 'https://www.citilink.ru/catalog/smart-chasy/?sorting=price_asc&pf=available.all%2Cdiscount.any%2Crating.any%2Camazfit%2C23525_835chernyy%2C9315_835&f=available.all%2Cdiscount.any%2Crating.any%2Camazfit%2C23525_835chernyy'

s = Session()
s.headers.update(headers)
response = s.get(url).text
print(response)

# with open('citylink.html', 'w', encoding='utf-8') as html_file:
#     html_file.write(response.text)

# soup = BeautifulSoup(response.text, 'lxml')

# watches = soup.find_all("div", class_="e1ex4k9s0")
# watches = soup.find_all("div", class_="ehanbgo0")
# print(watches[0])
# print(len(watches))
# for watch in watches:
#     name = watch.find("a")
#     logger.info(name)
