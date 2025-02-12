x, y, z = input("expression: ").split()
x = int(x)
z = int(z)

if y == '+':
    result = (x+ z)
if y == '-':
    result = (x - z)
if y == '*':
    result = (x * z)
if y == '/':
    result = (x / z)
else:
    print("Invalid")

print(f'{result:.1f}')