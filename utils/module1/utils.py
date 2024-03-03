import os
import json

def important_func():
    print("h")

def save_as_json(contents, file_name: str, folder: str = ""):
    file_path = os.path.join(folder, file_name + ".json")
    with open(file_path, "w") as file:
        json.dump(contents, file, indent=4)

def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

print("a")