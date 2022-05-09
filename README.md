# Ninja-shooter

Stop the invasion of demons!

## Preview

![Preview](https://github.com/YatoAki/Ninja-shooter/blob/main/images/preview.gif)

Thanks [Annastasshia Ames](https://www.pinterest.com/pin/559009372468048908/) of Pinterest for amazing background!

## Features

* Stop the demons before the pass through the screen
* Shoot out the shuriken to kill the demons
* Win the game by eliminating all

## How to run the programs

* Make sure you have install python3 on your device
* Install pygame module using `pip install pygame`

1. First, clone this repo to your local mechine with __git__ command.
* `git clone https://github.com/YatoAki/Ninja-shooter`
2. Go to the source code of the cloned dictionary you want to run.
*  `cd ./Ninja-shooter`
3. Run the `game.py` file with python interpretor.
* `python3 game.py`

## Game architecture

### Demon Class - `demon.py`

* Create demon object with location data & image data
* Draw the character
* Check for the collision with the ninja shuriken

### Ninja Class - `ninja.py`

* Create ninja object with location data & image data
* Draw the character

### Weapon Class - `weapon.py`

* Create weapon object with location data & image data
* Draw the weapon

### Generator Class - `generator.py`

* Generate a group of demon to be displyed on the game

### Game Class - `game.py`

* The main file of our program which is composed with `demon.py`, `ninja.py`, `weapon.py` & `generator.py`.
* Allow us to create the game UI and place each character in their respective positions
* Keep the game loop
