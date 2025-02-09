number = input('Num: ')

match number.casefold():
    case "42" | "forty two" | "forty-two":
        print("Yes")   
    case _:
        print('No')

