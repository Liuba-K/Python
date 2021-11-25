data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in (data):
    print('Привет, ' + i.split(' ')[-1].title() + '!')

###variant_2-desirable
"""
for i in (data):
    name = i.split(' ')[-1].title()
    print(f'Привет, {name}!')
"""
