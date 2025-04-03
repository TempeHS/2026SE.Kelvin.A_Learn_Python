## Create two lists of items
## Create two lists with a ID so line items can be paired
## User input a item to a prompt and only that item from the table prints
## print the two lists as a table
## Add a new items and sort the list
## Create a text document with the lists 1, 2 files
## Read from the lines
## Edit lines and write to lists

def print_table(list_1, list_2):
    print("| list 1", "|", "list 2 |")
    print("|--------|--------|")
    for i in range(len(lists[0])):
        print("|--------|--------|")
        print("|     ", lists[0][i], "|", lists[1][i], "     |")

def enter_num(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter Num: ")


def num_in_list(user, lists):
    if user in lists[0]:
        print("Num in list 1: ", user)
    elif user in lists[1]:
        print("Num in list 2: ", user)
    else:
        print("Num not in list(s), try again")


list_1 = [0, 1, 2, 3, 4]
list_2 = [5, 6, 7, 8, 9]
lists = [list_1, list_2]

print_table(list_1, list_2)

user = enter_num("Enter num list 1 or list 2: ")
num_in_list(user, lists)

new_item = enter_num("Add num to list 1: ")
list_1.append(new_item)
list_1.sort()

new_item = enter_num("Add num to list 2: ")
list_2.append(new_item)
list_2.sort()


print_table(list_1, list_2)

with open("list_1.txt", "w") as f:
    for item in list_1:
        f.write(str(item) + "\n")
with open("list_2.txt", "w") as f:
    for item in list_2:
        f.write(str(item) + "\n")