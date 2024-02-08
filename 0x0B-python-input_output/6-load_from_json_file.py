#!/usr/bin/python3
'''represtent object in json'''


import json


def load_from_json_file(filename):
    '''load object in json file'''
    with open(filename, 'r', encoding='UTF8') as f:
        return json.load(f)
