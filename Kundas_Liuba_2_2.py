data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_data = ' '
for item in data:
    if len(item) < 2 and item.isdigit():
        new_data += '"0'
        new_data += item
        new_data += '" '
    elif item.isdigit() or item[1:].isdigit():
        new_data += '"'
        new_data += item
        new_data += '" '
    else:
        new_data += item
        new_data += ' '
print(new_data)