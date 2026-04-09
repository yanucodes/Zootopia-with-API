"""Script to generate html file with information about animals in the
database"""

import json


ANIMALS_JSONFILE = "animals_data.json"
HTML_TEMPLATE = "animals_template.html"
REPLACE_STR = "__REPLACE_ANIMALS_INFO__"
ANIMALS_HTML_PATH = "animals.html"
TABS_NUM = 3  # number of tabs to add for nicer formatting


def load_data(file_path: str):
    """
    Load data from a JSON file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        Data loaded from the JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"{file_path} does not exist.")
    except PermissionError:
        print(f"Cannot read file {file_path}. Permission denied.")
    except UnicodeDecodeError:
        print(f"Cannot read file {file_path}. Encoding should be UTF-8.")
    except OSError as e:
        print(f"Failed to load {file_path}: {e}")
    return None


def serialize_animal(animal: dict) -> str:
    """
    Export available information about an animal (name, diet, location and
    type) to string.

    Args:
        animal: Dictionary with the data about the animal.

    Returns:
        String with available information about the animal.
    """
    animal_info = "\t" * TABS_NUM
    animal_info += '<li class="cards__item">\n'
    if animal.get("name"):
        name = animal.get("name")
        animal_info += "\t" * TABS_NUM
        animal_info += f'<div class="card__title">{name}</div>\n'

    animal_info += "\t" * (TABS_NUM + 1)
    animal_info += '<p class="card__text">\n'

    if animal.get("characteristics", {}).get("diet"):
        diet = animal.get("characteristics", {}).get("diet")
        animal_info += "\t" * (TABS_NUM + 1)
        animal_info += f"<strong>Diet:</strong> {diet}<br/>\n"
    if animal.get("locations"):
        location = animal.get("locations")[0]
        animal_info += "\t" * (TABS_NUM + 1)
        animal_info += f"<strong>Location:</strong> {location}<br/>\n"
    if animal.get("characteristics", {}).get("type"):
        animal_type = animal.get("characteristics", {}).get("type")
        animal_info += "\t" * (TABS_NUM + 1)
        animal_info += f"<strong>Type:</strong> {animal_type}<br/>\n"
    animal_info += "\t" * (TABS_NUM + 1)
    animal_info += "</p>\n"
    animal_info += "\t" * TABS_NUM
    animal_info += "</li>"
    return animal_info


def generate_html() -> str:
    """
    Load html template and add information about the animals into the template.

    Returns:
        Generated html with information about the animals.
    """
    animals = load_data(ANIMALS_JSONFILE)
    animals_info = ""
    for animal in animals:
        animals_info += serialize_animal(animal)
        animals_info += "\n"

    try:
        with open(HTML_TEMPLATE, "r", encoding="utf-8") as f:
            template = f.read()
        if REPLACE_STR in template:
            return template.replace(REPLACE_STR, animals_info)
        print(f"Cannot find {REPLACE_STR} in the template.")
    except FileNotFoundError:
        print(f"{HTML_TEMPLATE} does not exist.")
    except PermissionError:
        print(f"Cannot read file {HTML_TEMPLATE}. Permission denied.")
    except UnicodeDecodeError:
        print(f"Cannot read file {HTML_TEMPLATE}. Encoding should be UTF-8.")
    except OSError as e:
        print(f"Failed to load {HTML_TEMPLATE}: {e}")
    return None


def save_html():
    """
    Save generated html with information about animals to file.
    """
    animals_html = generate_html()
    if animals_html:
        try:
            with open(ANIMALS_HTML_PATH, "w", encoding="utf-8") as f:
                f.write(animals_html)
        except OSError as e:
            print(f"Failed to save generated html to '{ANIMALS_HTML_PATH}:' "
                  f"{e}")


if __name__ == "__main__":
    save_html()
