import unittest
from time import sleep

import firebase_admin
import admin
from firebase_admin import credentials
from firebase_admin import db
from password_hasher import java_hashcode
from password_hasher import convert_json_list


# cred = credentials.Certificate\
#     ("D:\Documents\Betzefer\YearB\semK\SoftwareSturcture\Ex4\carpentry-shop-firebase-adminsdk-pcbke-2e05a91098.json")
#
# firebase_admin.initialize_app(cred, { 'databaseURL':
#                                       'https://carpentry-shop.firebaseio.com/'
#                                       }
#                               )


class TestStringMethods(unittest.TestCase):

    #  Testing if user registration is ok by creating a user and trying to retrieve it.
    def test_registration(self):
        user_to_reg = "user1133462033"
        admin.register_user(user_to_reg, "1234")
        user_to_check = db.reference().child('users').child(user_to_reg).get()
        self.assertIsNotNone(user_to_check)
        admin.remove_user(user_to_reg)

    #  Testing if user removal is ok by creating a user manually and removing it,
    #  then trying to retrieve it.
    def test_remove(self):
        user_to_reg = "user1133462033"

        db.reference().child('users').child(user_to_reg).child('username').set(user_to_reg)
        db.reference().child('users').child(user_to_reg).child('password').set(java_hashcode("1234"))

        admin.remove_user(user_to_reg)
        user_to_check = db.reference().child('users').child(user_to_reg).get()
        self.assertIsNone(user_to_check)

    #  Testing if the user_exists function works by creating a user manually.
    def test_userexist(self):
        user_to_reg = "user1133462033"

        db.reference().child('users').child(user_to_reg).child('username').set(user_to_reg)
        db.reference().child('users').child(user_to_reg).child('password').set(java_hashcode("1234"))

        self.assertTrue(admin.user_exists(user_to_reg))
        admin.remove_user(user_to_reg)


if __name__ == '__main__':
    unittest.main()