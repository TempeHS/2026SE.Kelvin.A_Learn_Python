def main():
    x = fuel()
    if x < 1.0:
        print("E")
    elif x > 99.0:
        print("F")
    else:
        print(f"{x:.0f}%")

def fuel():
    while True:
        try:
            x = int(input("What is x? "))
            y = int(input("What is y? "))
            return (x / y) * 100
        except ValueError:
            print("Enter Integers")
        except ZeroDivisionError:
            print("Cannot divide by 0")
            

main()