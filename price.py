from pprint import pprint

def discounted(price, discount, max_discount = 25):                                 #функция
    price = abs(int(price))
    discount = abs(int(discount))
    max_discount = abs(int(max_discount))
    if max_discount >= 100:
            raise ValueError('Максимальная скидка не может быть больше 100')        #исключение
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount                                                      #возврат значения(за пределы функции после её выполнения)

product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 5}
product['final_price'] = discounted(product['price'], product['discount'])
pprint(product)

price = input()
discount = input()
max_discount = input()
print(discounted(price, discount, max_discount))