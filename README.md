# Zootopia with API

A command line tool that allows you to fetch information about animals from [animals API](https://api-ninjas.com/api/animals) and present them in a web page format.

## Getting Started

### Prerequisites

- Python 3.7+
- An API key from [API Ninjas](https://api-ninjas.com/).

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yanucodes/Zootopia-with-API.git
cd Zootopia-with-API

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
echo "API_KEY=Insert_your_API_key_here" > .env
```

## Usage

```bash
python animals_web_generator.py
```

You'll be prompted to enter an animal name:

```
Enter a name of an animal: fox
```
The script will generate animals.html file containing information about all found animals (full name, diet, location, type). 
