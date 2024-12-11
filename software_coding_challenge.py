
""" SECTION 3.A]
Design a parent class called Planet

It must have:
- General attributes: name, distance_from_sun, planet_type
- A get_distance_to_earth() method that gives you the absolute distance from the Earth.

!!! You can take the distance from the Sun to the Earth as 147 million kilometres !!!

For example, if the planet’s distance_from_sun was 148 million kilometres when you call the get_distance_from_earth()
method, it should give us the distance like this: {'distance to earth': 1000000} where the implied unit is kilometres.
This means that the planet is 1 million kilometres away from Earth.

> This question uses an oversimplification of the solar system model, not taking into account orbit position or the
eccentricity of the orbit, so in reality the result will be an approximate value with a reasonable margin of error.
"""

# Parent class: Planet
class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        earth_distance = 147  # Distance from Sun to Earth in million km
        return {"distance to earth": abs(self.distance_from_sun - earth_distance) * 1_000_000}  # Convert to km

# Test case for Planet
planet = Planet("GenericPlanet", 150, "Gas Giant")
print("Planet Attributes:", planet.name, planet.distance_from_sun, planet.planet_type)
print("Distance to Earth:", planet.get_distance_to_earth())

"""
B] Design a child class called Mercury, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class.
Your child class should also have a static method called happy_new_year(), which
would give us the information on how long a year lasts on the planet (in whatever way you wish!). 
You can take Earth Days as the implied unit.

After, create a Mercury object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT MERCURY !!!
Distance from Sun: 58 million
Planet Type: Terrestrial
Time taken for the planet to orbit the sun: 88 Earth days
"""

# Child class: Mercury
class Mercury(Planet):
    def __init__(self):
        super().__init__("Mercury", 58, "Terrestrial")

    @staticmethod
    def happy_new_year():
        print("A year on Mercury lasts 88 Earth days!")

# Test case for Mercury
mercury = Mercury()
print("Mercury Attributes:", mercury.name, mercury.distance_from_sun, mercury.planet_type)
print("Distance to Earth:", mercury.get_distance_to_earth())
mercury.happy_new_year()

"""
C] Design a child class called Jupiter, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class, as well as the additional attribute 
number_of_moons.
Your child class should also have a static method called happy_new_year(), which would give us the information on how 
long a year lasts on the planet (in whatever way you wish!). You can take Earth Days as the implied unit.

After, create a Jupiter object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT JUPITER !!!
Distance from Sun: 779 million
Planet Type: Gas Giant
Time taken for the planet to orbit the sun: 4383 Earth days
Number of Moons: 80
"""

# Child class: Jupiter
class Jupiter(Planet):
    def __init__(self):
        super().__init__("Jupiter", 779, "Gas Giant")
        self.number_of_moons = 80

    @staticmethod
    def happy_new_year():
        print("A year on Jupiter lasts 4383 Earth days!")

# Test case for Jupiter
jupiter = Jupiter()
print("Jupiter Attributes:", jupiter.name, jupiter.distance_from_sun, jupiter.planet_type, jupiter.number_of_moons)
print("Distance to Earth:", jupiter.get_distance_to_earth())
jupiter.happy_new_year()