#  This script includes helpful admin functions to the Carpentry Shop database,
#  which are used later in the firebase-admin.py script.


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from password_hasher import java_hashcode
from password_hasher import convert_json_list


cred = credentials.Certificate\
    ("D:\Documents\Betzefer\YearB\semK\SoftwareSturcture\Ex4\carpentry-shop-firebase-adminsdk-pcbke-2e05a91098.json")

firebase_admin.initialize_app(cred, { 'databaseURL':
                                      'https://carpentry-shop.firebaseio.com/'
                                      }
                              )


#  This function registers a new user with his hashed password
#  to the firebase database.
def register_user(username, password):

    username = username.lower()

    if user_exists(username):
        print("User '{}' already exists".format(username))
        return

    try:
        db.reference().child('users').child(username).child('username').set(username)
        db.reference().child('users').child(username).child('password').set(java_hashcode(password))
    except (db.ApiCallError, db.TransactionError):
        print("An error occurred")

    return

#  Remove a user given the User Name as the argument.
def remove_user(username):

    username = username.lower()

    if not user_exists(username):
        print("User '{}' not found. Probably doesn't exist".format(username))
        return

    try:
        db.reference().child('users').child(username).delete()
        db.reference().child('users').child(username)
    except (db.ApiCallError, db.TransactionError):
        print("An error occurred")


#  Register an entire list of users, given a JSON array as a file.
def register_json_list(json_file):
    push_users = convert_json_list(json_file)

    for user in push_users:
        register_user(user, push_users[user])

    return

#  Determines whether a user exists in the database.
def user_exists(username):

    username = username.lower()
    user = db.reference().child('users').child(username).get()

    if user is not None:
        return True

    return False

#  Prints all of the system's users one by one.
def get_all_users():

    ref = db.reference().child('users').get()
    print("\nUser list:\n")
    for user in ref:
        print(user)

#  Adds an item to a user.
def add_item(user, name, price):
    user = user.lower()

    if not user_exists(user):
        print("User {} not found".format(user))
        return

    ref = db.reference().child('users').child(user).child('items')

    ref.child('name').set(name)
    ref.child('price').set(price)

    return

#  Clears the database.
#  CAREFUL! This function deletes all of the users. There is no going back!
def clear_users():

    db.reference().child('users').delete()

    return
