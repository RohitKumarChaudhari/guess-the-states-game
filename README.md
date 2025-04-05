# 🌍 State Guessing Game

A fun and educational game where users guess the names of states based on a country map.  
This game is built using Python and the `turtle` module.

## 🎮 How to Play

1. When the game starts, a blank map of a country is shown.
2. The user types in the names of the states.
3. Correct guesses are labeled on the map.
4. The goal is to guess all the states!

## 🌐 Customization

You can change the country by replacing:

- `map_image.gif`: The background map image of the country.
- `states.csv`: A CSV file containing the state names and their (x, y) coordinates on the map.


### CSV File Format

Your `states.csv` file should look like this:

```csv
state,x,y
Bihar,120,34
Punjab,-45,80
...
```

## 📁 Files Included

- `main.py` – The main Python game file
- `states.csv` – The list of states and their positions
- `map_image.gif` – The background map image
- Example map and CSV for two countries

## 🛠 Requirements

- Python 3.x
- `turtle` module (usually pre-installed with Python)

## 🚀 Getting Started

```bash
git clone https://github.com/RohitKumarChaudhari/guess-the-states-game.git
cd guess-the-states-game
python main.py
```




