x, y, z = int(input("Enter x: ")), int(input("Enter y: ")), int(input("Enter z: "))


list = (x, y, z)

for i in list:
    for j in list:
        for k in list:
            if i != j and j != k and i != k:
                print(i, j, k)