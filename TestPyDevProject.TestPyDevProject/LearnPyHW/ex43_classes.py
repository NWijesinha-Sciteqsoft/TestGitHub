'''
Created on Nov 15, 2018

@author: nwijesinha


'''
# Create Scene class
from click._compat import raw_input

class Scene(object):
    # define enter function
    def enter(self):
        pass
    
# Create engine class
class Engine(object):
    
    # define constructor
    def __init__(self, scene_map):
        pass
    # define play function
    def play(self):
        pass
    
# Define death function
class Death(Scene):
    # define enter function
    def enter(self):
        pass

# Define central corridor class
class CentralCorridor(Scene):
    
    def enter(self):
        pass
    
# Define Laser Weapon Armory class
class LaserWeapnArmory(Scene):
    
    def enter(self):
        pass
    
# Define TheBridge class
class TheBridge(Scene):
    
    def enter(self):
        pass
    
# Define Escape Pod class
class EscapePod(Scene):
    
    def enter(self):
        pass
    
# Define Map class
class Map(Scene):
    # Define constructor
    def __init__(self, start_scene):
        pass
    # Define next scene function
    def next_scene(self, scene_name):
        pass
    # Define opening scene function
    def opening_scene(self):
        pass

# Print instructions to user    
print("starting game")
print("choose the following locations to start")
print("Enter 'central_corridor' to start at the central corridor")
print("Enter 'Laser_Weapon_Armory' to start at the Laster Weapon Armory")
print("Enter 'The_Bridge' to start at the The Bridge")
# Capture input from user
a_start_location = raw_input("> ")
print("Initiating Map")
# Initiate the map
a_map = Map(a_start_location)
print("Entering Game")
# Start the game
a_game = Engine(a_map)
print("Playing Game")
#Play the game
a_game.play()
# End the program
print("Ending Game")