#!/usr/bin/python3
"""
    9-add_item
"""
import sys

save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

file = "add_item.json"
"""
    adds all arguments to a Python list and save to new file
"""
try:
    new_file = load_json(file)
except (ValueError, FileNotFoundError):
    new_file = []
for i in range(1, len(sys.argv)):
    new_file.append(sys.argv[i])
save_json(new_file, file)
