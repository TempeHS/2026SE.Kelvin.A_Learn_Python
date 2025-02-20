total = 50
Coins = [5, 10, 25]
Amount_due = total

while Amount_due > 0:
    Money = int(input("Insert 5c, 10c or 25c Coin: "))
    
    if Money in Coins:
        Amount_due -= Money
    else:
        print("Invalid Coin")

    if Amount_due > 0:
        print(f"Amount due: {Amount_due}c")
    else:
        print("Thank you for your purchase")
        
    if Amount_due < 0:
        print(f"Please take your change: {abs(Amount_due)}c")
    







