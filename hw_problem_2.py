# HW1_P2: The Shopping List Maker

# Task 1: Write a function that lets the user add items to a list.

my_list = []

def add_item():
    while True:        
        item = input("What item would you like to add to your list? ")
        if item == "quit":          
            break
        my_list.append(item)

add_item()
print(my_list)


# Task 2: Include a feature to remove items from the list.

def remove_item():
    while True:
        item = input("What item would you like to remove from your list? ")
        if item == "quit":
            break
        my_list.remove(item)

remove_item()
print(my_list)


# Task 3: Add a function that prints out the entire list in a formatted way.

def show_list():
    print("Here are all of your items: ")
    for item in my_list:
        print(item)

show_list()
