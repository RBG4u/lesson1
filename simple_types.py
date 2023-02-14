a = 'Hi mom'
b = 'Mom'
c = f'{a}! {b}?!..' #f'{a}! {b}?!..' - форматированная строка
print(c.lower().split('o')) #print(len(c)) - длина строки      .split() - разбиение в список ['hi m', 'm! m', 'm?!..']

d = input('What? ').lower().strip().replace('a', 'ы').capitalize()     #.replace - замена
i = '   2'
print(d.strip() + i.strip())  #.strip - убирает пробелы в нач и кон

k = 2.0
print(type(k))

year = input('Введите год рождения ')
print(f'Ваш возраст: {2021 - int(year)}')