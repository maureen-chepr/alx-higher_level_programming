#!/usr/bin/python3
"""
    adds all arguments to a Python list,
    and then saves them to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arg_list = load_from_json_file("add_item.json")
except ValueError:
    arg_list = []

save_to_json_file(arg_list + sys.argv[1:], "add_item.json")