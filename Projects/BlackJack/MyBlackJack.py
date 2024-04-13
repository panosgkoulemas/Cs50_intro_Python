#CARDS
import random
suits = ("Clubs", "Spades", "Hearts", "Diamonds")
ranks = ("2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K", "A")
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
         "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
playing = True
replay = True

#Card Class
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
#Deck Class
class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        return f"Deck has {len(self.all_cards)} cards left!"

#Hand Class
class Hand:

    def __init__(self):
        self.hand_cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, new_card):
        self.hand_cards.append(new_card)

    def check_value(self):
        for card in self.hand_cards:
            if card.rank == "A":
                self.aces += 1
            self.value += card.value
        for ace in range(self.aces):
            if self.value <= 21:
                break
            else:
                self.value -= 10

    def __str__(self):
        hand = []
        for card in self.hand_cards:
            hand.append(card.rank)
        return f"Your Hand is {hand}"
    
#Chips Class
class Chips:

    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        print(f"You won {self.bet} $")

    def lose_bet(self):
        self.total -= self.bet
        print(f"You lost {self.bet} $")

    def __str__(self):
        return f"Your current total is {self.total} $"

#Functions

#Enter total players money
def enter_players_chips(chip):
  num = 0
  while num <= 0:
    try:
      num = float(input("Enter your buy-in: "))
      if num <= 0:
          print("Bet some money!")
    except:
      print("This is not a valid answer! Try again!")
      continue
  print(f"You are in the game with a total of {num} $")
  chip.total = num

#Take bets
def take_bet(chip):
    num = 0
    while num <= 0 or num > chip.total:
        try:
            num = float(input("Place your bet: "))
            if num > chip.total:
                print("Not enough money to place this bet! Try again!")
            elif num <= 0:
                print("This is not a valid bet! Try again!")
        except:
            print("This is not a valid bet! Try again!")
            continue

    print("Bet placed!")
    chip.bet = num

#Hit next card
def hit(deck, hand):
  hand.add_card(deck.deal_one())

#Hit or stand option
def hit_or_stand(deck, hand):
  global playing
  choices = ["H", "h", "s", "S"]
  choice = False
  while choice not in choices:
    choice = input("Choose Hit or Stand (H or S): ")
    if choice not in choices:
      print("Try again! Please answer Hit or Stand (H or S)!")
  if choice == "H" or choice == "h":
    hit(deck, hand)
  elif choice == "S" or choice == "s":
    playing = False

#Show dealer's hand
def show_dealers_hand(dealer):
    show = []
    for card in dealer.hand_cards:
      show.append(card.rank)
    print(f"Dealer's hand is {show[1:]} and one hidden card")

#Show all cards
def show_all(hand, player):
    show = []
    for card in hand.hand_cards:
      show.append(card.rank)
    print(f"{player}'s hand is {show} and value is {hand.value}")

#Play again ?
def game_on():
    choice = ["Y", "y", "N", "n"]
    ans = input("Do you wanna play again? Y or N: ")
    while ans not in choice:
        print("I don't understand. Please answer Y or N")
        ans = input("Do you wanna play again? Y or N: ")
    if ans == "Y" or ans == "y":
        return True
    elif ans == "N" or ans == "n":
        return False

if __name__ == "__main__":
    #GAMEPLAY

    #Player's chips
    print("Let's start playing Blackjack!")
    chip = Chips(0)
    enter_players_chips(chip)
    total = chip.total
    while replay:
        #Opening Statement
        playing = True
        print("It's the dealer vs You!")
        #Create deck and shuffle it and deal 2 cards to the player and 2 to the dealer
        deck = Deck()
        deck.shuffle_deck()
        #Set up players and dealers hands
        players_hand = Hand()
        dealers_hand = Hand()
        #Enter the bet
        take_bet(chip)
        print("\n")

        #Deal 2 cards to the player and to the dealer and show them approprietly
        for i in range(2):
            hit(deck, players_hand)
        for i in range(2):
            hit(deck, dealers_hand)
        dealers_hand.check_value()
        players_hand.check_value()
        show_all(players_hand, "Player")
        show_dealers_hand(dealers_hand)
        print("\n")

        #Check if players hand is already 21 and so he wins
        if players_hand.value == 21:
            chip.win_bet()
            playing = False
        #Start playing the game:
        while playing:
            players_hand.value = 0
            players_hand.aces = 0
            hit_or_stand(deck, players_hand)
            print("\n")
            players_hand.check_value()
            show_all(players_hand, "Player")
            #If player hits 21 then player WINS
            if players_hand.value == 21:
                chip.win_bet()
                playing = False
                break
            #If player busts above 21 then player LOSES
            elif players_hand.value > 21:
                show_all(dealers_hand, "Dealer")
                chip.lose_bet()
                playing = False
                break
            elif playing == False:
            #If not 21 or busted and decided to stay
            #Dealer's turn
                print("\n")
                show_all(dealers_hand, "Dealer")
                #Dealer already has more than the player, then player LOSES
                if dealers_hand.value >= players_hand.value and dealers_hand.value <= 21:
                    show_all(dealers_hand, "Dealer")
                    chip.lose_bet()
                else:
                    #Deal until dealer has more than the player
                    while dealers_hand.value <= players_hand.value:
                        dealers_hand.value = 0
                        dealers_hand.aces = 0
                        dealers_hand.add_card(deck.deal_one())
                        dealers_hand.check_value()
                        show_all(dealers_hand, "Dealer")
                        #If dealer has more than the player and less or equal than 21 player LOSES
                        if dealers_hand.value >= players_hand.value and dealers_hand.value <= 21:
                            chip.lose_bet()
                            break
                        #If dealers busts then player WINS
                        elif dealers_hand.value > 21:
                            chip.win_bet()
                            break
                break
        print("\n")

        #If player loses all his/her money then game is over
        if chip.total == 0:
            print(chip)
            print("Game over! You have NO money left")
            replay = False
            break
        #Print total money and ask if they want to play again
        else:
            print(chip)
            replay = game_on()
        print("\n"*100)

    if total > chip.total:
        print(f"You lost {abs(total - chip.total)} $!\n")
    elif total < chip.total:
        print(f"Congratulations you won {abs(total - chip.total)} $!\n")
    else:
        print("Neither Profit nor Loss!\n")