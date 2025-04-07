from tabulate import tabulate
import csv
import sys

if len(sys.argv) > 2:
    print("Tim cheese")
    sys.exit(1)
elif len(sys.argv) < 2:
    print("John pork")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("Simon claw")
    sys.exit(1)
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            pizza = []
            for row in reader:
                pizza.append(row)
            print(tabulate(pizza, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

