import csv
import sys

if len(sys.argv) > 3:
    print("too many arguments")
    sys.exit(1)
elif len(sys.argv) < 3:
    print("too few arguments")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("not a csv file")
    sys.exit(1)


with open(sys.argv[1]) as file_before:
    reader = csv.DictReader(file_before)
    data = []   

    for row in reader:
        a = row["name"].split(", ")
        first,last = a[0], a[1]
        data.append({"first": first, "last": last, "house": row["house"]})
        data.sort(key=lambda x: x["house"])

with open(sys.argv[2], "w") as file_after:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file_after, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
print("sorted")
    
    



