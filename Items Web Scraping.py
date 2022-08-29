from bs4 import BeautifulSoup
import requests
# We will want to run once for variationless equipment, and consumables that only have one
# charge, ex: Rune_scimitar, Cooked_chicken
ex_source = requests.get('https://oldschool.runescape.wiki/w/Rune_scimitar').text
soup = BeautifulSoup(ex_source, 'lxml')
ge_price = soup.find('span', class_='infobox-quantity-replace').text.split('(')[0]
item_name = soup.find('th').text
print('{}: GE Price: {}'.format(item_name, ge_price))
print(soup.prettify())

#<span class="infobox-quantity" data-val-each="15037">
#           <span class="infobox-quantity-replace">