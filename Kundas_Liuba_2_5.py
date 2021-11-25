price_of_goods_list = input("Введите список цен на товары, копейки вводить через точку")

new_prices = []
for price in price_of_goods_list.split():
    price_parts = price.split(".")
    if len(price_parts) < 2:
        ruble = price_parts[0]
        kopeck = "00"
    else:
        ruble, kopeck = price_parts
        if len(kopeck) == 1:
            kopeck = "0" + kopeck
    _new_price = f'{ruble} руб {kopeck} коп'
    new_prices.append(_new_price)
print("answer A")
print(", ".join(new_prices))

id_1 = id(new_prices)

new_prices.sort(key = lambda price : [int(price.split(" ")[0]), int(price.split(" ")[2])])
print("answer B")
print(new_prices)
print(id_1 == id(new_prices))

new_prices_decrease = sorted(new_prices, key = lambda price : [int(price.split(" ")[0]), int(price.split(" ")[2])], reverse=True)
print("answer C")
print(new_prices_decrease)

print("answer D")
print(new_prices_decrease[:6])
