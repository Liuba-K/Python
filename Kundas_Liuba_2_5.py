price_of_goods_list = input("Введите список цен на товары, копейки вводить через точку")

new_price = ''
for i in price_of_goods_list.split():
    if len(i.split(".")) < 2:
        ruble = i.split(".")[0]
        new_price += f'{ruble} руб '

    else:
        for idx, val in enumerate(i.split(".")):
            ruble, kopeck = i.split(".")
            if idx == 1:
                kopeck = "0" + kopeck
        new_price += (f'{ruble} руб {kopeck} коп ')
print(new_price)

print(list(price_of_goods_list.sort()))


