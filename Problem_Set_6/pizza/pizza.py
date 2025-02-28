#Prints a CSV file into an ASCII art format
import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif '.csv' not in sys.argv[1]:
    sys.exit("Not a CSV file")
else:
    try:
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
            print(tabulate(menu, headers= "firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")