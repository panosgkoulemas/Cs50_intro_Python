total = 50
change = 0

while total > 0:
    print(f"Amount Due: {total}")

    x = int(input("Insert Coin: "))

    if x in [25, 10, 5]:
        total = total - x
    

if total <= 0:
    change = -total

print(f"Change Owed: {change}")