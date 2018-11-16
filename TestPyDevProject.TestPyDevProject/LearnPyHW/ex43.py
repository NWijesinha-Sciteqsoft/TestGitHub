'''
Created on Nov 15, 2018

@author: nwijesinha
'''

# Import libraries for the game
from sys import exit
from random import randint
from click._compat import raw_input
import code



# base class for scene
class Scene(object):
    # Define enter function for the Scene
    def enter(self):
        # Print the message
        print("This scene is not yet configured. Subclass it and implement enter()")
        # exit function gracefully
        exit(1)

# Engine class to move from scene to scene
class Engine(object):
    # define constructor
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    #   Define play function
    def play(self):
        # variable for current scene
        current_scene = self.scene_map.opening_scene()
        # Loop through while True to next scene
        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
# Death class
class Death(Scene):
    # list to store message
    quips = [
        "You died. You kind of suck at this.",
        "Your mom would be proud...if she were smarter.",
        "I have a small puppy that's better at this."
        ]
    
    # Define function to enter
    def enter(self):
        # Print the message
        print(Death.quips(0, len(self.quips)-1))
        # exit function gracefully
        exit(1)
        
# Class for Central Corridor
class CentralCorridor(Scene):
    # Define enter function
    def enter(self):
        print("The Gothoms of Planet Percal #25 have invaded your ship and destroyed")
        print(" your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory")
        print("put it in the bridge, and blow the ship up after getting into an ")
        print("escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print("a Gothom jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print(" flowing around his hate filled body. He's blocked the door to the")
        print("Armory and about to pull a weapon to blast you.")
        
        action = raw_input("> ")
        
        if action == "shoot!":
            # check if the user input is shoot
            # Print story for shooting
            print("Quick on the draw you yan out your blaster and fire it at the Gothom")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim. Your laser hits his costume but misses him entirely. this")
            print("ruins his brand new costume his mother bought him, which")
            print("makes him fly into a rage and blast at you repeatedly on the face until")
            print("you are dead. Then he eats you")
            # return death
            return 'death'
        
        elif action == 'dodge!':
            # check if the user input is dodge
            # Print story for dodging
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothom's blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out")
            print("You wake up shartly after only to die as the Gothom stomps on")
            print("your head and east you")
            #return death
            return 'death'
        
        elif action == 'tell a joke':
            # check if the user input is tell ajoke
            # Print story for telling a joke
            print("Lucky for you they made you learn Gothom insults in the academy.")
            print("You tell the one Gothom joke you know:")
            print("lbh eh hbenhyb dkjohd nl ahjh ehoh hua mkijd ,lkjijd khjuihhd jkhuhd")
            print("The Gothom stops, tries not to laugh, then busts out laughing and can't move")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door")
            # return laser_weapon_armory
            return 'laser_weapon_armory'
        
        else:
            # For any other input print message and return central_corridor
            print("DOE NOT COMPUTE!")
            return 'central_corridor'
        
# Laser weapon armory class for laser weapon armory scene
class LaserWeaponArmory(Scene):
    # Define enter function for Laser Weapon Armory class
    def enter(self):
        # Print the story
        print("You do a dive and roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothoms that might be hiding. It's dea quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("wrong 10 time then the then the lock closes forever and you can't")
        print(" get the bomb. the code is 3 digits.")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[Keypad]> ")
        guesses = 0
        print(code)
        
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = raw_input("[Keypad]> ")
             
        if guess == code:
            # Print the story for correct code
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'
        else:
            # Print the story if code is not correct
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die.")
            return 'death'

# Define a class for the bridge scene
class TheBridge(Scene):
    # Define enter function
    def enter(self):
        # print the Story
        print("You burst onto the Bridge with the neutron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship. Each of them has an even uglier")
        print("clown costume than the last. They haven't pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.")

        action = raw_input("> ")
        
        if action == "throw the bomb":
            # check if the action is to throw the bomb
            # Print the story 
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a")
            print("Gothon shoots you right in the back killing you.")
            print("As you die you see another Gothon frantically try to disarm")
            print("the bomb. You die knowing they will probably blow up when")
            print("it goes off.")
            # return death
            return 'death'
        elif action == "slowly place the bomb":
            # Check if the action is to slowly place the bomb
            # Print story
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat.")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            # return escape pod
            return 'escape_pod'
        else:
            # if any other input 
            print("DOES NOT COMPUTE!")
            # return the bridge
            return 'the_bridge'
        
# Class for escape pod
class EscapePod(Scene):
    # Define enter function
    def enter(self):
        # Print story for Escape Pod
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes. It seems like")
        print("hardly any Gothons are on the ship, so your run is clear of")
        print("interference. You get to the chamber with the escape pods, and")
        print("now need to pick one to take. Some of them could be damaged")
        print("but you don't have time to look. There's 5 pods, which one")
        print("do you take?")
        
        good_pod = randint(1,5)
        print(good_pod)
        guess = raw_input("[pod #]> ")
        
        if int(guess) != good_pod:
            # Check if the guess does not match the correct pod
            # Print story
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            # return death
            return 'death'
        else:
            # if the guess match the correct pod
            # print story
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, you look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time. You won!")
            # return finished
            return 'finished'

# Class Map store each scene by name in a dictionary
class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
        }
    # define constructor
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    #Define next scene function
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    # Define opening scene function
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
    
if __name__ == '__main__':
        # Initiate the map
        a_map = Map('central_corridor')
        print("Entering Game")
        # Start the game
        a_game = Engine(a_map)
        print("Game Started")
        #Play the game
        a_game.play()