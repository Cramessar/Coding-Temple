import random
import pygame
import os

pygame.mixer.init()
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
VICTORY_SOUND = os.path.join(CURRENT_DIR, "ff_victory.mp3")

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, special_ability, special_ability_name, personality):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_ability = special_ability
        self.special_ability_name = special_ability_name
        self.personality = personality
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        print(f"{self.name} ({self.personality}) attacks {opponent.name} for {damage} damage!")
        opponent.health -= damage
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special(self, opponent):
        damage = random.randint(self.special_ability - 10, self.special_ability + 10)
        print(f"{self.name} shouts '{self.special_ability_name}!' and deals {damage} damage to {opponent.name}!")
        opponent.health -= damage
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(20, 40)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} ({self.personality}) heals for {heal_amount} health. Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Special Move: {self.special_ability_name} ({self.personality})")

    def is_alive(self):
        return self.health > 0

# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, special_ability=50, special_ability_name="Bushido: Dragon Fang", personality="Stoic and determined")

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20, special_ability=60, special_ability_name="Fury: Thundaga", personality="Calm and calculated")

# Black Mage class
class BlackMage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30, special_ability=70, special_ability_name="Fury: Flare", personality="Brooding and relentless")

# Rogue class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=35, special_ability=55, special_ability_name="Mix: Chaos Grenade", personality="Playful and mischievous")

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30, special_ability=65, special_ability_name="Overdrive: Status Reels", personality="Laid-back and confident")

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=28, special_ability=60, special_ability_name="Grand Summon: Holy", personality="Pure-hearted and brave")

# Evil Wizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, special_ability=25, special_ability_name="Dark Curse", personality="Sinister and cunning")

    def regenerate(self):
        regen_amount = random.randint(10, 20)
        self.health += regen_amount
        print(f"{self.name} regenerates {regen_amount} health! Current health: {self.health}")

def create_character():
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Black Mage")
    print("4. Rogue")
    print("5. Archer")
    print("6. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return BlackMage(name)
    elif class_choice == '4':
        return Rogue(name)
    elif class_choice == '5':
        return Archer(name)
    elif class_choice == '6':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def play_victory_sound():
    pygame.mixer.music.load(VICTORY_SOUND)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def battle(player, wizard):
    while wizard.is_alive() and player.is_alive():
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.is_alive():
            wizard.regenerate()
            wizard.attack(player)

        if not player.is_alive():
            print(f"{player.name} has been defeated! Game Over!")
            break

    if not wizard.is_alive():
        print(f"Congratulations! The evil wizard {wizard.name} has been defeated by {player.name}!")
        play_victory_sound()

def main():
    print("Welcome to the Battle Against the Evil Wizard!")
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
