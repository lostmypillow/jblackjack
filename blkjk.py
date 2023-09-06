import random, time
play_again = True
orig_deck = {
    "A of clubs": 1,    "A of hearts": 1,    "A of diamonds": 1,    "A of spades": 1,    
"2 of clubs": 2,    "2 of hearts": 2,    "2 of diamonds": 2,    "2 of spades": 2,    
"3 of clubs": 3,    "3 of hearts": 3,    "3 of diamonds": 3,    "3 of spades": 3,    
"4 of clubs": 4,    "4 of hearts": 4,    "4 of diamonds": 4,    "4 of spades": 4,    
"5 of clubs": 5,    "5 of hearts": 5,    "5 of diamonds": 5,    "5 of spades": 5,    
"6 of clubs": 6,   "6 of hearts": 6,    "6 of diamonds": 6,    "6 of spades": 6,    
"7 of clubs": 7,    "7 of hearts": 7,    "7 of diamonds": 7,    "7 of spades": 7,    
"8 of clubs": 8,    "8 of hearts": 8,    "8 of diamonds": 8,    "8 of spades": 8,    
"9 of clubs": 9,    "9 of hearts": 9,    "9 of diamonds": 9,   "9 of spades": 9,    
"10 of clubs": 10,   "10 of hearts": 10,   "10 of diamonds": 10,   "10 of spades": 10,   
"J of clubs": 10,    "J of hearts": 10,    "J of diamonds": 10,    "J of spades": 10,    
"Q of clubs": 10,    "Q of hearts": 10,    "Q of diamonds": 10,    "Q of spades": 10,    
"K of clubs": 10,    "K of hearts": 10,    "K of diamonds": 10,    "K of spades": 10, 
}

ace_deck = {
    "A of clubs": 11,    "A of hearts": 11,    "A of diamonds": 11,    "A of spades": 11,
}


deck = orig_deck.copy()
h_hand = []
h_value = 0
#h_value_a = 0
p_hand = []
p_val = 0
player_turn = False
dealer_turn = False
count = 0
AceP = False
AceH = False
Bust = False
#while play_again == True:

def count_hand(which_hand,times):
    count = 0
    value = 0
    while count < times:
        hand = random.choice(list(deck.keys()))
        deck.pop(hand)
        which_hand.append(hand)
        value += int(orig_deck.get(hand))
        print(value)
     #   if orig_deck.get(hand) == 1:
     #       AceH == True
        count += 1
    return value

def print_result(*args):
    #first check for house Ace
    if args[0] == True:
        if args[1] == True:
            print("Dealer cards: ", h_hand[0], "(", orig_deck.get(h_hand[0]),"or", (orig_deck.get(h_hand[0]) + 10), ")", "\n", "Your cards: ", p_hand, "(", p_val,"or", (p_hand + 10), ")","\n")
        else:
            print("Dealer cards: ", h_hand[0], "(", orig_deck.get(h_hand[0]),"or", (orig_deck.get(h_hand[0]) + 10), ")", "\n", "Your cards: ", p_hand, "(", p_val, ")","\n")
   
    else:
        print("Dealer cards: ", h_hand[0], "(", orig_deck.get(h_hand[0]), ")", "\n", "Your cards: ", p_hand, "(", p_val, ")","\n")


h_value += count_hand(h_hand, 2)
p_val += count_hand(p_hand, 2)

while player_turn == False:
    print_result(AceH, AceP)
    if p_val == 21:
        print("BLACKJACK!", "\n")
        time.sleep(2)
        player_turn = True
    else:
        prompt = input("Hit or stand? (h/s)")
        if prompt == "h":
            hand = random.choice(list(deck.keys()))
            deck.pop(hand)
            p_hand.append(hand)
            p_val += int(orig_deck.get(hand))
            print ("You get ", hand, "\n")
            time.sleep(2)
            if p_val > 21:
                print("You BUST!", "\n")
                player_turn = True
                dealer_turn = True
        elif prompt == "s":
            player_turn = True
            print("\nYour turn is over")
            time.sleep(2)
            print("House's turn\n")  
    
 

while dealer_turn == False:
    
    time.sleep(2)
    print("Dealer cards: ", h_hand, "(", h_value, ")", "\nYour cards: ", p_hand , "(", p_val, ")","\n") 
    time.sleep(2) 
    if h_value == 21 and h_hand.len() == 2:
            time.sleep(2)
            print("Dealer BLACKJACK!")
    elif h_value >= 17:
        time.sleep(2)
        print("House stands\n")
        if h_value > p_val and h_value <=21:
            time.sleep(2)
            print("Dealer wins! You lose!")
        elif h_value == p_val and h_value <=21:
            time.sleep(2)
            print("Push")
        else:
            time.sleep(2)
            print("House pays! Player wins!")
        dealer_turn = True

    else:
        time.sleep(2)
        hand = random.choice(list(deck.keys()))
        deck.pop(hand)
        h_hand.append(hand)
        h_value += int(orig_deck.get(hand))
        print ("Dealer gets ", hand, " Value: ", h_value, "\n")
        time.sleep(2)
        
  #  play_prompt = input("Play again? (y/n)")
  #  if play_prompt == "y"
    



#The combination of an ace with a card other than a ten-card is known as a "soft hand," 
#because the player can count the ace as a 1 or 11, and either draw cards or not. 
# For example with a "soft 17" (an ace and a 6), the total is 7 or 17. 
# While a count of 17 is a good hand, the player may wish to draw for a higher total. 
# If the draw creates a bust hand by counting the ace as an 11, the player simply counts the ace as a 1 and continues playing by standing or "hitting" (asking the dealer for additional cards, one at a time).




