<div align="center">

# PAC-MAN: OOP Game
  
![30-huge-maze-pacman](https://user-images.githubusercontent.com/93098869/204936248-8a9a3fd9-1c63-45b2-a34f-808350ed6ab4.gif)

</div>

## Info

|       |                                                                                                                                                                                                     |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| About | PAC Man OOP Game is a python game that incorporate Object-oriented programming principles to create classes to create characters and coins to create a game.                                                                                   |
| Team  | [Louisa Goncharenko](https://github.com/lougoncharenko), [Andrew Alsing](https://github.com/Andrew32A)
| Goal  | Develop a robust python game application using an Object Oriented Programming Principles.                                                                                                               |
|       |                                                                                                                                                                                                     |




### File Structure

```sh
Pacman/
├── character.py         # Character class: Parent class
├── pacman.py # Pacman class that inherits from parent
├── ghost.py # Ghost class that inherits from parent
├── coin.py # Coin class that is passed into other classes to increase coin levels.
├── main.py        # Main File that runs the game
```

<div align="center">
  
## Diagram of Class Inheritance 

<img width="1009" alt="Screen Shot 2022-11-30 at 6 53 45 PM" src="https://user-images.githubusercontent.com/93098869/204934501-31016072-395e-4b98-9fe2-2f8356a856d1.png">
</div>

## Features
- Each character (both ghosts and Pacmans) have the ability to move on a grid using (x,y) coordinates
- Each character has an eat method where if they bummp into one another, the character with the highest coin level eats the other character.
- Ghosts are given a color attribute and a mood for visual effects.
- Each character is able to add or lose coins based on class methods.
- Ghosts have a visibility method that changes there visibility on the board for visual effects.


## Learnings
- created classes
- used single-class inheritance
- used a super method to inherit attributes from parent classes
- generated a random amount of coins for each characters

## Improvements for the game
- Using Pygame library to draw character and the grid
- Creating buttons to start and pause the game
