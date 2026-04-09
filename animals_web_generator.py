"""Script to generate html file with information about animals"""

import os
import requests
from dotenv import load_dotenv


HTML_TEMPLATE = "animals_template.html"
REPLACE_STR = "__REPLACE_ANIMALS_INFO__"
ANIMALS_HTML_PATH = "animals.html"
TABS_NUM = 3  # number of tabs to add for nicer formatting

# API configuration
load_dotenv()
API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")
HEADERS = {"X-Api-Key": API_KEY}


def load_data(animal_name: str):
    """
    Load information about animals using API.

    Args:
        animal_name: Search string passed to API.

    Returns:
        Data about animals.
    """

    res = requests.get(f"{API_URL}?name={animal_name}", headers=HEADERS)
    if res.status_code == 200:
        return res.json()
    return None


def serialize_animal(animal: dict) -> str:
    """
    Convert available information about an animal (name, diet, location and
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


def generate_html(animal_name: str) -> str:
    """
    Load information about the animals and insert into html template.

    Args:
        animal_name: Name of the animal to look up.

    Returns:
        Generated html with information about the animals.
    """
    animals = load_data(animal_name)
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


def save_html(animal_name: str):
    """
    Save generated html with information about animals to file.

    Args:
        animal_name: Name of the animal to look up.
    """
    animals_html = generate_html(animal_name)
    if animals_html:
        try:
            with open(ANIMALS_HTML_PATH, "w", encoding="utf-8") as f:
                f.write(animals_html)
            print("Website was successfully generated to the file "
                  f"{ANIMALS_HTML_PATH}.")
        except OSError as e:
            print(f"Failed to save generated html to '{ANIMALS_HTML_PATH}:' "
                  f"{e}")


def main():
    """
    Ask user to enter the name of an animal and generate html with
    information about animals with this name.
    """
    animal_name = input("Enter a name of an animal: ")
    save_html(animal_name)


if __name__ == "__main__":
    main()
