#-------------------------------------------------------------------------------------------#
#                                                                                           #
#       Welcome to the FireBase-Admin of our humble Carpentry Shop!                         #
#                                                                                           #
#  This program contains function to help you manipulate our DataBase. It includes          #
#  registering users, removing users, print the users and more! It is very easy to          #
#  navigate through our menu.                                                               #
#                                                                       Have fun,           #
#                                                                       Damir and Leora     #
#                                                                                           #
#-------------------------------------------------------------------------------------------#


import admin
import password_hasher

INDENT = "\t\t\t\t\t\t"

#  Menu constants:
#  ---------------
REG_USR        = '1'
DEL_USR        = '2'
PRNT_USRS      = '3'
CHECK_EXST     = '4'
DEL_ALL_USRS   = '5'
ADD_ITEM       = '6'
GEN_JSON_ARR   = '7'
INPUT_JSON_ARR = '8'
EXIT           = '9'



def menu():

    choice = 0

    while int(choice) not in range(1, 10):
        print("\nPlease choose an operation:")
        print("1)  Register a new user to the system.")
        print("2)  Delete an existing user.")
        print("3)  Print the existing users.")
        print("4)  Check whether a user exists.")
        print("5)  Delete all users from the system.")
        print("6)  Add an item to a selected user.")
        print("7)  Create a JSON array file with users.")
        print("8)  Enter a JSON array file to the system.")
        print("9)  Exit.")

        choice = input("Your choice: ")
        print("\n\n")
    return choice


def main():

    print(INDENT + "Hello and welcome to 'Carpentry Shop' admin!\n")

    print("Menu:\n-----\n")

    choice = menu()

    while choice != EXIT:

        if choice == REG_USR:
            username = input("Enter username: ")
            password = input("Etner Password: ")
            admin.register_user(username, password)

        elif choice == DEL_USR:
            username = input("Enter username: ")
            admin.remove_user(username)

        elif choice == PRNT_USRS:
            admin.get_all_users()

        elif choice == CHECK_EXST:
            username = input("Enter username: ")
            if admin.user_exists(username):
                print("The user exists!")
            else:
                print("No such user!")

        elif choice == DEL_ALL_USRS:
            admin.clear_users()
            print("All users cleared from the system successfully!")

        elif choice == ADD_ITEM:
            username = input("Enter username: ")
            item     = input("Enter the item's name: ")
            price    = input("Enter the item's price: ")

            admin.add_item(username, item, price)

        elif choice == GEN_JSON_ARR:

            filename = input("Name your file: ")

            password_hasher.create_json_list(filename)

        elif choice == INPUT_JSON_ARR:

            filename = input("Enter full file name: ")

            admin.register_json_list(filename)

        choice = menu()

    return 0


if __name__ == '__main__':

    main()
