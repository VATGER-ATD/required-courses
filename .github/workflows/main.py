import os
import json
import sys


def format_and_sort_json_files(filenames: list[str]):
    for filename in filenames:
        if filename.endswith('.json'):
            try:
                with open(filename, 'r') as json_file:
                    data = json.load(json_file)
                # Write the reformatted JSON back to the file
                with open(filename, 'w') as json_file:
                    json.dump(data, json_file, indent=2)
                print(f"Reformatted JSON in {filename}")
            except json.JSONDecodeError as e:
                print(f"Error loading JSON from {filename}: {e}")
                sys.exit(1)


def load_and_append_json_files(filesnames: list[str]):
    folder_data = []
    for filename in filenames:
        if filename.endswith(".json"):
            file_path = filename
            try:
                with open(file_path, "r") as json_file:
                    data = json.load(json_file)
                    folder_data.extend(data)  # Use extend to add items to the list
            except json.JSONDecodeError as e:
                print(f"Error loading JSON from {file_path}: {e}")
    with open('courses.json', 'w') as f:
        json.dump(folder_data, f)


if __name__ == '__main__':
    filenames = ['edgg.json', 'edmm.json', 'edww.json']
    load_and_append_json_files(filenames)
    format_and_sort_json_files(['courses.json'])