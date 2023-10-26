# 2048 Neat-Python AI
_NOTE: unfinshed_
<br>
## PlayableGame
Contains the same 2048 and boxfunctions files, but before the neat intragration.
2048_p.py is a user playable version of the game that can be opperated by the arrow keys.

## 2048.py
Uses a neat-python genetic algorithem to learn how to play the game 2048
- test by training for 50 generations

## boxfunctions.py
Functions used to move tiles in the game field (and array), check for win/loss, and calculate score

## config-neat.txt
config file for Neat
- population size of 100
- sigmoid activation function
- 16 inputs and 4 outputs
