cats = ['Оранжевый', 'Черепаховый', 'Чмоня']
print('Котеки:', cats, 'Оранжевых:', cats.count('Оранжевый'))

cats.append(input('Введите своего котека: '))
print('Котеки:', cats, 'Оранжевых:', cats.count('Оранжевый'))

print(cats[:2])      # с 0 по 2, если 2: то со 2 до последнего 

print(cats.index('Оранжевый'))

cats.sort()
print(cats)
print(cats.index('Оранжевый'))
print(cats)

del cats[:2]
print(cats)
print('Черепаховый' in cats)

cats.remove('Черепаховый')
print(cats)
print('Черепаховый' in cats)