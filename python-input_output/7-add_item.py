#!/usr/bin/python3
"""
Script: 7-add_item

Adds all arguments to a Python list, and then saves them to a file.
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists
if os.path.exists(filename):
    # Load existing list from the file
    my_list = load_from_json_file(filename)
else:
    # Create an empty list if the file doesn't exist
    my_list = []

# Add all arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
