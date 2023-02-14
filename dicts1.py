from pprint import pprint

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]
pprint(stock)
stock.append({'name': 'Samsung Galaxy S22 NEW', 'stock': 55, 'price': 60000.0, 'discount': 0})
pprint(stock)
pprint(stock[3]['name'])

stock[0]["recomended"].append('ddddddd')
pprint(stock[0])
stock[0]['colour'] = 'black'
pprint(stock[0])