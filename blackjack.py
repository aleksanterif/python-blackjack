#random will offer me a great way to randomly select cards and shuffle deck
import random

 # Players hand is an empty array in the beginning
player_hand = []
 # Dealers hand is an empty array in the beginning
dealer_hand = []

# We should be able to tell if the user is playing
userPlaying = True

# object in which I define the values of the cards
suits = ('Spades','Diamonds', 'Clubs', 'Hearts')
ranks = ('Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace':11, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

class Card:
    # The __init__() function is called automatically every time the class is being used to create a new object.
    # The self keyword gives us the access for the attributes and methods of the class
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    # the card should be output like "Ace of Spades"
    def __str__(self):
        return self.suit + ' of ' + self.rank

test = Card( 'Ace', 'Spades' )
print(test)
# I need a deck class inwhich I can store my cards accordignly 
# I need a function to deal the cards
# Other funcion to display the delt cards
# separate delt cards to dealers and players

# increase the sum of players cards
# increase the sum of dealers cards

#display winner and ask if the player wants to keep playing

#In an ideal world, player could place a bet thats going to be written in a bet amount txt file.