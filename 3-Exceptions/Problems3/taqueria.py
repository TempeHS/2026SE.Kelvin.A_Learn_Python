def main():
    food = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        try:
            item = input("What's your order? ").title()
            if item == '':
                break
            price = food[item]
            print(f"The price of {item} is ${price:.2f}")
        except EOFError:
            break
        except KeyError:
            print("Unkown item")
        except KeyboardInterrupt:  
            print("\nBye")       
    
if __name__ == "__main__":
    main()