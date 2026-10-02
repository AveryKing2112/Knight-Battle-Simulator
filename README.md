# Knight Battle Simulator

A command-line battle game in Python where three knights fight until only one is left standing. Each knight gets random health and armor, and attacks deal random damage, so every battle plays out differently.

This started as my midterm project for ITEC-352 (inheritance and polymorphism), and I expanded it into a full game.

## The Knights

| Knight | Type | Special ability |
| --- | --- | --- |
| Gawain | Knight | None |
| Mordred | Cavalry Knight | Adds a charge bonus to every attack |
| Lancelot | Dark Knight | Follows each attack with dark magic |

## How to Run

Requires Python 3.7 or later. No extra packages needed.

```
python main.py
```

Press Enter to move through each round, and enter `y` at the end to fight again.

## Files

- `objects.py` contains the `Knight` superclass and the `cavalryKnight` and `darkKnight` subclasses.
- `main.py` creates the knights, runs the battle, and announces the winner.

## Concepts Used

Inheritance, method overriding with `super()`, polymorphism, dataclasses, `__str__`, `isinstance()`, and the `random` module.
