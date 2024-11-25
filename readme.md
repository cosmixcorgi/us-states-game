# U.S. States Game

This is a Python-based game that helps you learn and memorize the U.S. states using a map. It provides an interactive graphical interface where you can guess state names and see their locations marked on the map.

## Features

- Interactive GUI using the `turtle` library.
- Tracks correctly guessed states.
- Generates a "states_to_learn.csv" file containing states you missed.
- Uses `pandas` for data handling.

## How It Works

1. The game displays a blank map of the United States.
2. You are prompted to enter the name of a U.S. state.
3. If your guess is correct, the state's name is displayed at its location on the map.
4. The game continues until you guess all 50 states or type "Exit".
5. If you type "Exit", a `states_to_learn.csv` file is generated with the list of states you didn't guess correctly.

## Prerequisites

Make sure you have the following installed on your system:
- Python 3.6 or higher
- `turtle` module (comes pre-installed with Python)
- `pandas` library

Install `pandas` if it's not already installed:
```bash
pip install pandas
