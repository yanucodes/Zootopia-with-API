import os
import requests
from dotenv import load_dotenv


# API configuration
load_dotenv()
API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")
HEADERS = {"X-Api-Key": API_KEY}


def fetch_data(animal_name: str):
    """
    Fetches the animals data for the animal 'animal_name'.

    Args:
        animal_name: Search string passed to API.

    Returns:
        List of dictionaries with information about animals.
    """

    res = requests.get(f"{API_URL}?name={animal_name}", headers=HEADERS)
    if res.status_code == 200:
        return res.json()
    return None