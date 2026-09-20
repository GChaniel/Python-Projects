
# Define the parent class with common animal attributes and a method
class FarmAnimal:
    name = ''
    age = 0

    def make_sound(self):
        msg = "This animal makes a sound."
        return msg

# Catfish inherits from FarmAnimal and overrides the make_sound() method
class Catfish(FarmAnimal):
    pond_number = 2
    weight = 2

    def make_sound(self):
        msg = "I am a catfish. I don't make an audible sound!"
        return msg

# Chicken inherits from FarmAnimal and provides its own make_sound() method
class Chicken(FarmAnimal):
    egg_count = 24
    breed = 'Native '

    def make_sound(self):
        msg = "Cluck! Cluck!"
        return msg



# Call the same method on different objects to produce different results
if __name__ == "__main__":
    farm = FarmAnimal()
    print(farm.make_sound())

    fish = Catfish()
    print(fish.make_sound())

    chicken = Chicken()
    print(chicken.make_sound())

    
