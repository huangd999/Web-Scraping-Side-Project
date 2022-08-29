from bs4 import BeautifulSoup
import requests
import pandas as pd
name_csv = pd.read_csv(r'C:\Users\huang\OneDrive\Documents\Side Project\List of Names Final Version.csv', header=0)

#item_list=['Rune_full_helm', 'Redberry_pie', 'Dragon_scimitar',
#           'Prayer_potion#4_dose', 'Dharok%27s_helm#Undamaged']
item_list = []
f = 0
while f in range(len(name_csv['Names'])):
    item_list.append(name_csv['Names'][f])
    f += 1
print(f)
print(len(item_list))
print(item_list[-1:])

for item in item_list:
    name_list = []
    price_list = []
    name_list2 = []
    price_list_2 = []
    bin_list = []
    source = requests.get('https://oldschool.runescape.wiki/w/{}'.format(item)).text
    soup = BeautifulSoup(source, 'lxml')
    if soup.find('span', class_='button') == None:
        ge_price = \
            soup.find('span', class_='infobox-quantity-replace').text.split('(')[0]
        item_name = soup.find('th').text
        print(item_name)
        print('GE Price: {}'.format(ge_price))
        print()
    # Note to replace the else w/ elif, elif != None and not equippable to diff
    # from the different variations of equippables which work differently...
    elif len(name_list) == len((name_list2)):
        i = 0
        for name in soup.find_all('span', class_='button'):
            name_list.append(name.text)

        for value in soup.find_all('span', class_='infobox-quantity-replace'):
            price_list.append(value.text.split('(')[0])

        for price in price_list:
            if price not in price_list_2:
                price_list_2.append(price)
        if soup.find_all('td', attrs={'colspan': '13'})[4].text != 'Yes':
            print(soup.find('h1', class_='firstHeading').text)
            # Iterator
            # Separate lists for the names from the buttons, and the prices. We wish
            # to populate these lists.
            l_n = len(name_list)
            l_p = len(price_list_2)
            print(name_list)
            print(price_list_2)
            if l_n == l_p:
                while i in range(l_n):
                    print('{}: GE Price: {}'.format(name_list[i], price_list_2[i]))
                    i += 1
            else:
                while i in range(l_p):
                    print('{}: GE Price: {}'.format(name_list[i], price_list_2[i]))
                    i += 1
            print()
        else:
            for name in name_list:
                if name not in name_list2:
                    name_list2.append(name)
                else:
                    pass
            if 'Loading...' in name_list2:
                name_list2.remove('Loading...')
            print(name_list2)
            for price in soup.find_all('span', class_='infobox-quantity-replace'):
                price_list.append(price.text.split('(')[0])
            for price in price_list:
                if price not in price_list_2:
                    price_list_2.append(price)
                else:
                    pass
                # Cannot retrieve from table header - will only retrieve the tags from the
                # buttons...
                # Change of perspective: When not sold is there there will be missing entries.
            print(price_list_2)

            # Create for loop to create a proper price list, note that in this case the Not
            # sold are missing, we will add this into list now, true corresponds with numerical
            # value, false corresponds with Not sold.
            l = 0
            if len(name_list2) == len(price_list_2):
                print(soup.find('h1', class_='firstHeading').text)
                while l in range(len(name_list2)):
                    print('{}: GE Price: {}'.format(name_list2[l], price_list_2[l]))
                    l += 1
            else:
                for span in soup.find_all('span', attrs={'data-attr-param': 'gemw'}):
                    print(span.text)
                    span = span.text.split(')')[1].split('e')[:len(span) - 1]
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
                        price_list3.append(price_list_2[k])
                        k += 1
                    # In this case we do not add to iterator, if we do so then it'll move onto
                    # the price of the next item that is tradeable...
                    else:
                        price_list3.append('Not sold')

                print(soup.find('h1', class_='firstHeading').text)
                while l in range(len(name_list2)):
                    print('{}: GE Price: {}'.format(name_list2[l], price_list3[l]))
                    l += 1
