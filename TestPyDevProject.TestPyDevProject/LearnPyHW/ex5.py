'''
Created on Oct 17, 2018

@author: nwijesinha
'''
# Create Variable my_name and assign the name
name = "Zed A. Shaw"
# Create a variable my_age and assign the age
age = 35
#Create variable my_height and assign the height in inches
heightInc = 74 #inches
heightCm = 74 * 2.54
# Create variable my_wight and assign the weight in lbs
weightLbs = 180
weightKg = weightLbs * 0.453592
# Create variable my_eyes and assign color of the eyes
eyes = "Blue"
# Create variable my_teeth and assign color of the the teeth
teeth = "White"
# Create variable my_hair and assign color of the hair
hair = 'Brown'

# Print all variables
print("Let's talk about %r" % name)
print("He's %e inches tall" % heightInc)
print("He's %e pounds heavy" % weightLbs)
print("He's got %r eyes and %r hair." % (eyes, hair))
print("His teesth are usually %r depending on the coffee" % teeth)

#This line is tricky, try to get it exactly right

print("If I add %f, %f, and %f I get %d" % (age, heightInc, weightLbs, age + heightInc + weightLbs))

print("His height %d in inches and %d in centimeters" % (heightInc, heightCm))
print("His weight %d in lbs and %d in Kg" % (weightLbs, weightKg))
        