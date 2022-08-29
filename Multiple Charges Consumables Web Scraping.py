from bs4 import BeautifulSoup
import requests
source = requests.get('https://oldschool.runescape.wiki/w/Agility_mix').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())
# This only gets the GE value for each of them
for value in soup.find_all('span', class_='infobox-quantity-replace'):
    print(value.text)
# This was not the best start - some pages here contain multiple versions of the
# table (due to varying differences in the equipment/consumable, different doses,
# different poisons, durability and etc). Bronze_spear, Prayer_potion#4_dose

# Now find a way to include the versions of the item, and the title.
# Note that it always starts from lowest charge to highest charge or from lowest
# to highest poison.

# Instead create a list of charges/doses/etc, and of the prices, and match them
# based on index.
name_list = []
price_list = []
for name in soup.find_all('span', class_='button'):
    name_list.append(name.text)
for value in soup.find_all('span', class_='infobox-quantity'):
    price_list.append(value.text.split('(')[0])
# Remove duplicates from price - may have something to do with the format of the
# wiki with charged items.
price_list_2 = []
for price in price_list:
    if price not in price_list_2:
        price_list_2.append(price)
i = 0
l = len(name_list)
l_p = len(price_list_2)
print(price_list)
print(price_list_2)
print(name_list)
if l == l_p:
    while i in range(l):
        print('{}: GE Price: {}'.format(name_list[i], price_list_2[i]))
        i+=1
else:
    while i in range(l_p):
        print('{}: GE Price: {}'.format(name_list[i], price_list_2[i]))
        i += 1

# Alright, we can now account for single item types and multiple item types, we
# now need a way to automate the collection

# We try with some other page to verify this.

# Different with equippables vs consumables. Extra set of buttons.
# Currently the consumables portion works, but not the equippables with different
# versions...