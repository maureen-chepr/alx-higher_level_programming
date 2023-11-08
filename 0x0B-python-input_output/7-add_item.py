#!/usr/bin/python3
"""
    adds all arguments to a Python list,
    and then saves them to a file
"""
from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
        adds all arguments to a Python list,
        and then saves them to a file
    """
    try:
        arg_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arg_list = []

    arg_list.extend(argv[1:])
    save_to_json_file(arg_list, "add_item.json")


if __name__ == "__main__":
    add_items()
