def main():
    Qs = input("Sentence: ")
    print(snake_Change(Qs))

def snake_Change(Hump):
    nothing = ""
    for letter in Hump:
        if str(letter).isupper() == True:
            snakes = "_" + letter.lower()
            nothing += snakes
        else:
            nothing += letter
    return nothing





main()