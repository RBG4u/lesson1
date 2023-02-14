from pprint import pprint

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1,
    "colour": "black"
}
print(product)
product['memory'] = 256
product['stock'] = 15
print(product)

print(product["stock"])

print(product.get("discount", 0))        #.get если нет то пишет None, если после запятой поссле запятой есть то буит выдавать введенное значение
print(product.get("colour", "grey"))
print(product)

del product["colour"]
print(product)

cats = ['Оранжевый', 'Черепаховый', 'Чмоня']
product["recomended"] = cats
pprint(product)
pprint(product["recomended"][0])

product["recomended"].append("Коцка")
pprint(product)