#!/usr/bin/python3
'''represtent object in json'''


import json


def save_to_json_file(my_obj, filename):
    '''save object in json file'''
    with open(filename, 'w', encoding='UTF8') as f:
        json.dump(my_obj, f)
