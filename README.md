# PyManGame

PyManGame is a 2D platform-style game developed in Python using the **Pygame** library.  

The player controls a character called **PY-MAN** and tries to achieve the highest possible score while avoiding obstacles.

---

# Gameplay

The game consists of **two levels** with different mechanics.

## Level 1 – City Platform Run
In the first level the player moves across buildings in a city environment.

The objective is to:
- Jump from building to building
- Avoid falling
- Survive while the background continuously accelerates
- Achieve the highest possible score

## Level 2 – Air Survival
In the second level the character flies through the air.

The player must:
- Avoid **birds**
- Avoid **airplanes**
- Survive as long as possible
- Increase the score

If the character collides with an obstacle, the game ends.

---

# Technologies Used

- **Python**
- **Pygame**
- 2D sprites and PNG assets
- Sound effects and background music
---

# Project Structure

- `rungame.py` → Main game file  
- `map.txt` → Game map configuration  
- `assets/images` → Game sprites and graphics  
- `assets/sounds` → Sound effects and music  
- `assets/fonts` → Fonts used in the UI 

# Installation

### Install Pygame

Open a terminal and run:

pip install pygame

If that does not work:

python -m pip install pygame

---

# How to Run the Game

1. Download or clone the repository
2. Open the project folder
3. Run the game with:

python rungame.py

Enjoy the game!

---
