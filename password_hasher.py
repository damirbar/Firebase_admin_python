
#  This script includes helpful functions which are used in admin.py and firebase-admin.py

#  The Java hashcode algorithm was taken from here:
#  http://garage.pimentech.net/libcommonPython_src_python_libcommon_javastringhashcode/

import json

#  The Java hashcode algorithm
def java_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return str(((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000)


#  This function takes a JSON array as a file and turns it to a dictionary.
#  The admin.register_json_list function uses this function.
def convert_json_list(file):
    j_output_obj = []                        # An empty list to obtain the information from the JSON array

    ret_dict = {}

    with open(file, 'r') as json_arr:        # Get the JSON array to the variable "input_arr"
        input_arr = json.load(json_arr)

    for i in range(len(input_arr)):          # Appending the user name and hashed password to the list
        name = input_arr[i]['username']      # Obtain the username
        password = input_arr[i]['password']  # Obtain the password
        ret_dict[name] = password
        j_output_obj.append(name + ':' + java_hashcode(password))

    json_obj = json.dumps({'users': j_output_obj})  # Wrapping the produced list

    with open('users.json', 'w') as users:   # Writing the product to a JSON document
        users.write(json_obj)

    return ret_dict

#  This function generates a JSON array as a file with given input.
#  The argument is the file name to be generated. The result file
#  will be users_"filename".json.
def create_json_list(filename):

    j_output_arr = []  # An empty list to obtain the information and turn it to a JSON array

    operation = input("Start?\ny for yes. Anything else to quit.\t")

    if operation != 'y':
        return

    while operation == 'y':

        username = input("Username: ")
        password = input("Password: ")

        j_output_arr.append({
            'username': username,
            'password': password
        })

        operation = input("\nContinue?\nY for yes. Anything else to quit.\t")

    with open('users_' + str(filename) + '.json', 'w') as users:  # Writing the product to a JSON document
        json.dump(j_output_arr, users)

    return

