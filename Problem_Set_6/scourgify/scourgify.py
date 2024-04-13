import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif '.csv' not in sys.argv[1] and '.csv' not in sys.argv[2]:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as f1, open(sys.argv[2], 'w', newline= '') as f2:
            next(f1)
            reader = csv.reader(f1)
            writer = csv.DictWriter(f2, fieldnames= ["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                writer.writerow({"first": row[0].split(',')[1].strip(),
                                 "last": row[0].split(',')[0],
                                 "house": row[1]})

    except FileNotFoundError:
        sys.exit("File does not exist")