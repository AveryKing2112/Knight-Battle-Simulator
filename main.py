"""
Avery King
ITEC-352-001
9/30/2026
"""

import random
from objects import Knight, cavalryKnight, darkKnight

# Creates the knights with random health (80-120) and armor (5-15)
def create_knights():
    return [Knight("Gawain", random.randint(80, 120), random.randint(5, 15)),
            cavalryKnight("Mordred", random.randint(80, 120), random.randint(5, 15)),
            darkKnight("Lancelot", random.randint(80, 120), random.randint(5, 15))]


# Prints a knight, plus its special ability if it has one
def show_knight(knight):
    print(knight) # calls __str__
    if isinstance(knight, cavalryKnight):
        print(f"    Special: charge bonus of {knight.charge_bonus}")
    elif isinstance(knight, darkKnight):
        print(f"    Special: dark magic of {knight.dark_magic}")

# Returns a  list of the kngihts that are still alive
def get_living(knights):
    living = []
    for knight in knights:
        if knight.is_alive():
            living.append(knight)
    return living

def battle(knights):
    round_num = 1
    while len(get_living(knights)) > 1:
        print(f"ROUND {round_num}")
        for attacker in knights:
            if not attacker.is_alive():
                continue # Knocked out knights dont attack
            targets = get_living(knights)
            targets.remove(attacker)
            if len(targets) == 0:
                break # no one left to fight

            target = random.choice(targets)
            #Polymorphism: each type runs its own deal_damage()
            attacker.deal_damage(target, random.randint(15, 25))
            if not target.is_alive():
                print(f"{target.name} has been defeated!")
            print()

        round_num +=1
        input("Press Enter for the next round...")
        print()

    winner = get_living(knights)[0]
    print(f"{winner.name} is the last knight standing!")
    print(winner)




def main():
    print("The Knight battle program")
    print()


    choice = "y"
    while choice.lower() == "y":
        knights = create_knights() # new random stats every battle

        print("KNIGHTS")
        for knight in knights:
                show_knight(knight)
        print()

        input("Press Enter to begin the battle...")
        print()

        battle(knights)
        choice = input("\nfight again? (y/n): ")
        print()

        print("Goodbye!")






  
""" # create one knight of each type
    knights = (Knight("Gawain", 100, 10),
               cavalryKnight("Mordred", 100, 10),
               darkKnight("Lancelot", 100, 10))
    print("KNIGHTS")
    for knight in knights:
        show_knight(knight)
    print()

    input("Press Enter to begin the battle")
    print()
            

    # Polymorphism, each knight calls deal_damage(), but each type
    # runs its own version of the method
    gawain, mordred, lancelot = knights
    gawain.deal_damage(mordred, 20)
    print()
    mordred.deal_damage(lancelot, 20)
    print()
    lancelot.deal_damage(gawain, 10)
    print()


    print("After the battle")
    for knight in knights:
        print(knight)
    print()
    print("Bye") """

  

if __name__ == "__main__":
    main()