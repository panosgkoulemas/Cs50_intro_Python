menu = {"Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}

total = 0
while True:
    try:
        x = str(input("Item: ")).title()

        if x in menu.keys():
            total = total + menu[x]
            print(f"Total: ${format(total, ".2f")}")
    #end inputting item when you press ctrl+d or ctrl+z
    except EOFError:
        break
