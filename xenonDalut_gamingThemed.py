# ACTIVITY 3

class Warrior():
    def special_move(self):
        return "Warrior swings a mighty sword!"

class Mage():
    def special_move(self):
        return "Mage casts a powerful spell!"

class Archer():
    def special_move(self):
        return "Archer shoots a precise arrow!"

def perform_move(character):
    print(character.special_move())

warrior = Warrior()
mage = Mage()
archer = Archer()

characters = [warrior, mage, archer]
for character in characters:
    perform_move(character)

# ACTIVITY 4

class HealthPotion():
    def use(self):
        return "You regain 50 HP!"

class ManaPotion():
    def use(self):
        return "You regain 30 MP!"

class SpeedBoost():
    def use(self):
        return "Your speed increases for 10 seconds!"

def apply_item(item):
    print(item.use())

health_potion = HealthPotion()
mana_potion = ManaPotion()
speed_boost = SpeedBoost()

potions = [health_potion, mana_potion, speed_boost]
for potion in potions:
    apply_item(potion)

# ACTIVITY 5

# Methods special_move() and use() are examples of polymorphism in action. Each class (Warrior, Mage, Archer, HealthPotion, ManaPotion, SpeedBoost) implements its own version of the method, allowing for different behaviors when the method is called on different objects. This demonstrates how polymorphism allows for flexibility and code reusability in object-oriented programming.
# This activity shows polymorphism in a gaming context by allowing different character classes and items to have their own unique implementations of the same method, enabling them to be used interchangeably in the perform_move() and apply_item() functions.
# Another example where the same action behaves differently depending on the character or item could include a "jump" action that behaves differently for a character with a jetpack versus a character without one.
