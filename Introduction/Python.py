import json


def read_data_from_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON data in file: {file_path}")


# Use the function
json_data = read_data_from_json_file("example.json")
print(json_data)
