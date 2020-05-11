#random will offer me a great way to randomly select cards and shuffle deck
import random

# We should be able to tell if the user is playing
userPlaying = True

#In an ideal world, player could place a bet thats going to be written in a bet amount txt file.

class Bet:
    def __init__(self):
        self.betValue = 0
        self.amount = 500    #defining of the amount and bet might be better for the user to decide?

    def game_lost(self):
        self.amount -= self.betValue
        
    def game_won(self):
        self.amount += self.betValue

#We need a function to take bet from the user

def select_bet_amount(bet):
    while True:
        bet.betValue = int(input("How much do you want to bet this time? "))
        if bet.betValue > bet.amount:
            print("you dont have that many much credit, your credit value currently is " + str(bet.amount))
        else:
            break

    

#lets see if we can just use one hand and then just define it to all participant players
class Hand:
    # The self keyword gives us the access for the attributes and methods of the class
    def __init__(self):
        self.cards = []  # initial state is that its created as an empty array
        self.aces_total = 0    # value of aces can be 1 or 11 so we need to keep track of those
        self.card_value = 0   # initial value of cards combined is 0 and we need to remove 10 from it if the amount from getting aces goes higher than 21
    
    def add_card(self,card):    #with card passed here they can append it to their hand
        self.cards.append(card) #with this we can append (add) single card to players hand
        self.card_value += values[card.rank]    #we increase the value with the value set to each rank
        if card.rank == 'Ace':
            self.aces_total += 1  # we need to make sure that player even has aces to build our logic around that
    
    def reset_ace_value(self):
        while self.aces_total > 0 and self.card_value > 21:
            self.card_value -= 10 #we remove 10 from value if there are any aces and the hand goes over 21


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
                self.deck.append(Card(suit,rank)) #with this we can append (add) cards to a deck. Self.deck is a list of card objects
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
        
def give_card(deck,hand): #I need to be able to give out single cards so this will help me
    hand.add_card(deck.deal())

def take_card_or_not(deck,hand):    #With this we will know if the player wants to receive more cards
    while True:
        enteredValue = input('Do you wish to take more cards? Enter yes or no: ') 
        if enteredValue == 'yes':
            give_card(deck,hand)
            print('player took a card, his cards value is now: ' + str(hand.card_value))
        elif enteredValue == 'no':
            print('player stopped taking cards, his cards value is now: ' + str(hand.card_value))
            break
        else:
            print('You didnt answer the question correctly')

def player_loses(player, bet)
    print("player loses")
    bet.game_lost()

def dealer_loses(player, bet)
    print("dealer loses, player wins")
    bet.game_won()

def player_wins(player, bet)
    print("player wins")
    bet.game_won()

def dealer_wins(player, bet)
    print("dealer wins, sorry player")
    bet.game_lost()


new_deck = Deck()
new_deck.shuffle()
bet = Bet()
player1 = Hand()
select_bet_amount(bet)
give_card(new_deck, player1)
print(player1.card_value)
take_card_or_not(new_deck, player1)

# Other funcion to display the delt cards
# separate delt cards to dealers and players

# increase the sum of players cards
# increase the sum of dealers cards

#display winner and ask if the player wants to keep playing

