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


# I need a deck class inwhich I can store my cards accordignly 
class Deck:
    #It doesnt take any parameters in here to prevent the user from adding any cheats
    def __init__(self):
        self.deck = []  #initial state is that its created as an empty array
        for suit in suits: #suits can be used here since its a global variable
            for rank in ranks:
                self.deck.append(Card(suit,rank)) #with this we can append (add) cards to a deck
        # __str__ is used to create the string output we need
    def __str__(self):
        complete_deck = ''  # initial state is again an empty string
        for card in self.deck:
            complete_deck += '\n '+card.__str__() # with this we can print out every card in the deck
        return 'In this deck is:' + '\n ' + complete_deck

# I need a function to deal the cards
    def deal(self):
        one_card = self.deck.pop() #grab the deck attribute and pop a card item (single card from that list). Pop method removes the item at the given index from the list and returns the removed item.
        return one_card
                
    def shuffle(self):
        random.shuffle(self.deck) #with random we are able to shuffle the cards to get mixed results from which to pull single cards
        

test = Deck()
test.shuffle()
print(test)
# Other funcion to display the delt cards
# separate delt cards to dealers and players

# increase the sum of players cards
# increase the sum of dealers cards

#display winner and ask if the player wants to keep playing

#In an ideal world, player could place a bet thats going to be written in a bet amount txt file.