#  Function for lists - user has ability to add, delete etc and should have menus for that.
#  This could have settings.

def list_1(user_list=None):  # Function for adding to the list.
    add_type = int(input("Where do you want to add this item? Start with 1 if you haven't made a list yet. \n"
                         "1. Just at the end of the list. \n"
                         "2. At a specific point in the list. \n"))
    if add_type == 1:
        addition = input("What do you want to add? ")
        if not user_list:
            user_list = [f'{addition}']
            print(user_list)
        else:
            user_list.append(f'{addition}')
            print(user_list)
            #  Add functionality to repeat this later on.
    elif add_type == 2:
        index = int(input("Where do you want to put this? 0 is first. "))  # Update so that it displays 1 as first
        addition = input("What do you want to add? ")
        user_list.insert(index, f"{addition}")
    return user_list


user_list = []  # empty list!
menu_selection = int(input("What do you want to do today? \n"
                           "1. Add a new item to the end, or a certain point of, the list. \n"
                           "2. Organise the list ordering. \n"
                           "3. Analyse the list's contents. \n"
                           "4. Delete a list entry or the entire list. (BE CAREFUL!) \n"
                           "5. Change settings for this program. (Advanced) \n"))
if menu_selection == 1:
    list_1()

#  Main menu must get called first. Once that's done, things should happen away from it.
