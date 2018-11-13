'''
Created on Nov 13, 2018

@author: nwijesinha

This exercise is create a class in pythong
'''

class Song(object):
    '''
    classdocs
    '''


    def __init__(self, lyrics):
        '''
        Constructor
        '''
        self.lyrics = lyrics

    def sing_me_a_song(self):
        '''
        function to sing me a song print the lyrics
        '''
        for line in self.lyrics:
            print(line)
            
            
# Create an object with the lyrics for happy birthday song
happy_bday = Song({"Happy birthday to you",
                   "I don't want to get sued",
                   "so I'll stop right there'"})
# Define an object with lyrics for bulls on parade song
bulls_on_parade = Song({"They rallya round the family",
                        "with pockets full of shells"})

# Print happy birthday lyrics using sing me a song function
print('_' * 30)
happy_bday.sing_me_a_song()
print('_' * 30)
# Print bulls on parade lyrics using sing me a song function
bulls_on_parade.sing_me_a_song()
print('_' * 30)