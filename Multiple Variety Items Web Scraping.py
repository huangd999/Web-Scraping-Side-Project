# Apparently this works differently from the consumables, note that there is an
# extra table representing the different stats, so we can try using the th from
# the tables. Note that there is no header for the equipment stats tables.
# Prayer_potion#4_dose Dharok%27s_helm#Undamaged Bronze_spear Abyssal_bracelet#(5)
from bs4 import BeautifulSoup
import requests
source = requests.get('https://oldschool.runescape.wiki/w/Adamant_arrow').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
name_list = []
for button in soup.find_all('span', class_='button'):
    name_list.append(button.text)
    # Delete duplicates:
name_list2 = []
for name in name_list:
    if name not in name_list2:
        name_list2.append(name)
    else:
        pass
print(name_list2)
price_list = []
for price in soup.find_all('span', class_='infobox-quantity-replace'):
    price_list.append(price.text.split('(')[0])
# delete the duplicate near the beginning:
price_list2 = []
for price in price_list:
    if price not in price_list2:
        price_list2.append(price)
    else:
        pass
    # Cannot retrieve from table header - will only retrieve the tags from the
    # buttons...
    # Change of perspective: When not sold is there there will be missing entries.
print(price_list2)
    # Look to span data-attr-param = gemw
bin_list = []

# We now want to find true, false values, true means that it is tradeable and
# false indicates it is not tradeable and therefore not sold.

soup.find_all('span', attrs={'data-attr-param':'gemw'})
n = 4
for span in soup.find_all('span', attrs={'data-attr-param':'gemw'}):
    print(span.text)
    span = span.text.split(')')[1].split('e')[:len(span)-1]
    for i in range(len(span)):
        span[i] = span[i] + 'e'
    print(span)
    bin_list = span
print(bin_list)
# Create for loop to create a proper price list, note that in this case the Not
# sold are missing, we will add this into list now, true corresponds with numerical
# value, false corresponds with Not sold.
price_list3 = []
k = 0
for i in range(len(bin_list)):
    if bin_list[i] == 'true':
        price_list3.append(price_list2[k])
        k += 1
    # In this case we do not add to iterator, if we do so then it'll move onto
    # the price of the next item that is tradeable...
    else:
        price_list3.append('Not sold')
l = 0
print(soup.find('h1', class_='firstHeading').text)
while l in range(len(name_list2)):
    print('{}: GE Price: {}'.format(name_list2[l], price_list3[l]))
    l+=1