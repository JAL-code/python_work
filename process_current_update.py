#!/usr/bin/env python3
# Code by JAL-code
# Process the lastest update and output potential terminal input.
# User to Copy/Paste to terminal.

import os
import re
import sys

'''Enter "./process_current_update.py current_update.txt" at terminal.'''

txt_file_location = sys.argv[1]
modified = []
add = []
start = ''
end = ''
lines = ''

def clear_SE():
    start = ''
    end = ''

#def get_files():

def check_modified(lines):
    ch_mod = False
    print("Running modified.")
    line_Count = 0

    for line in lines:
        # print(f"CM: {line}")
        pattern = r"Changes not staged for commit:"
        result = re.search(pattern, line)
        # print(f"CM Result: {result}")
        if result is None:
            line_Count += 1
            continue
        else:
            print(f"CM: {result} @ line {line_Count}")
            ch_mod = True
            break

    for line in lines[line_Count+1:]:
        if re.search("^[A-Z]", line):
            break
        else:
            print(f"Test Line 1 {line}")
            if re.search(r"^\t", line):
                print("\tThis line is added to modified list.")
                modified.append(re.sub(r"modified:   ", '', re.sub(r"\t",'', line)))
    print(add)

    return ch_mod

def check_first_add(lines):
    ch_Untrack = False
    print("Running untracked")
    line_Count = 0

    for line in lines:
        # print(f"CFM {line}")
        pattern = r"Untracked files:"
        result = re.search(pattern, line)
        # print(f"CFM Result: {result}")
        if result is None:
            line_Count += 1
            continue
        else:
            print(f"CFA: {result} @ line {line_Count}")
            ch_Untrack = True
            break

    for line in lines[line_Count+1:]:
        if re.search("^[A-Z]", line):
            break
        else:
            if re.search(r"^\t", line):
                print(f"Test Line 2 {line}")
                print("This new item needs to be tracked.")
                add.append(re.sub(r"\t", '', line))
    print(modified)

    return ch_Untrack

def create_command(action, list_item):
    output = f"git {action} "
    print(f"Test list: {list_item}")
    output2 = ' '.join(list_item)
    return f"{output} {output2}"

def main(txt_file_location):
    print("Running Main")
    # Open the current_update.txt file
    try:
        file = open(txt_file_location)
    except OSERROR:
        return None
    lines = file.readlines()
    lines.remove('\n')
    print(lines)
    count = 0
    for line in lines:
        print(line)
        line_r = re.sub(r"\n", "", line)
        lines[count] = line_r
        count += 1
        print(line)
    # print(lines)
    file.close()

    checks = [
        (check_modified, "Modified Files found"),
        (check_first_add, "Found files to be added"),
    ]

    everything_ok = True
    for check, msg in checks:
        if check(lines):
            print(msg)
            everything_ok = False

    if not everything_ok:
        print("Work to be done!")
        if modified:
            print(f"These were modified: {modified}")
            print(create_command('add', modified))
        if add:
            print(f"These are new files: {add}")
            print(create_command('add', add))
    else:
        print("No GitHub updates to be pushed")

main(txt_file_location)