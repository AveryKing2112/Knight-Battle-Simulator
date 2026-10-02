"""
Avery King
ITEC-352-001
9/30/2026
OOP Midterm Assingment
"""

#Using dataclasses instead of hard coding __init__
from dataclasses import dataclass


# Superclass Knight with 3 attributes and 3 methods
@dataclass
class Knight:
    name: str
    health: float
    armor_rating: float


    # reduces health when the knight takes damage, armor absorbs part of it
    # max(...0) keeps health from going below 0
    def take_damage(self, amount):
        reduced_amount = max(amount - self.armor_rating, 0)
        self.health = max(self.health - reduced_amount, 0)
        print(f"{self.name} took {reduced_amount} damage (armor absorbed {amount - reduced_amount}). Health is now {self.health}.")


    # has this knight attack another knight
    def deal_damage(self, target, amount):
        print(f"{self.name} attacks {target.name} for {amount} damage!")
        target.take_damage(amount)


    def is_alive(self):
        return self.health > 0
    
    # user-friendly string, called automatically by print()
    def __str__(self):
        return f"{self.name} | Health: {self.health} | Armor: {self.armor_rating}"


# Subclass 1 adds a charge bonus to every attack
@dataclass
class cavalryKnight(Knight):
    charge_bonus:float = 10
    # Overrides Knight's deal_damage 
    def deal_damage(self, target, amount):
        print(f"{self.name} charges on horseback!")
        super().deal_damage(target, amount + self.charge_bonus)


# Subclass 2 follows each attack with dark magic
@dataclass
class darkKnight(Knight):
    dark_magic:float = 20
    # Overrides Knight deal_damage normal attack, then dark magic attack 
    def deal_damage(self, target, amount):
        super().deal_damage(target, amount)
        # only cast the spell if the target survived the normal attack
        if target.is_alive():
            print(f"{self.name} casts dark magic onto {target.name}.")
            target.take_damage(self.dark_magic)
