list = ["grapes", "cereal", "popcorn"]

while True:

    print("1 - List all items in the grocery list")
    print("2 - Add add new item in te list")
    print("3 - Remove a item from the list")

    action = int(input("Please select the desired action: 1/2/3\n"))

    try:
        if action == 1:
            print("Here's your grocery list for today:")
            for item in list:
                print(item)
        elif action == 2:
            new_item = input("What is the name of the item?\n")
            list.append(new_item)
        elif action == 3:
            remove_item = input("Please enter the name of item that you want to remove from the list\n")
            if remove_item not in list:
                print("The item is not in the list")
            else:
                list.remove(remove_item)
        else:
            print(f"The option {action} is not valid")
    except Exception as e:
        print(f"The following error happened: {e}")
