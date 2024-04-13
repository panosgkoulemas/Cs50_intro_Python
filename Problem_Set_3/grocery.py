shop_list = dict()

while True:
    try:
        x = str(input("Item: ")).strip().upper()

        if x not in shop_list.keys():
            shop_list[x] = 1
        else:
            shop_list[x] = shop_list[x] + 1

    except EOFError:
        break

#Sort a dictionary aplhabetically
sorted_shop_list = dict(sorted(shop_list.items()))
print()

#Print a dictionary and its items seperately
for item in sorted_shop_list:
    print(sorted_shop_list[item], item)
