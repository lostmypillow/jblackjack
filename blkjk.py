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

deck = orig_deck.copy()
h_hand = []
h_value = 0
p_hand = []
p_value = 0

player_turn = False


Bust = False
Push = False
dealer_turn = False
count = 0

#while play_again == True:

while count < 4:
    hand = random.choice(list(deck.keys()))
    deck.pop(hand)
    if count < 2:
        h_hand.append(hand)
        print(int(orig_deck.get(hand)))
        h_value += int(orig_deck.get(hand))
        count += 1
    else:
        p_hand.append(hand)
        p_value += int(orig_deck.get(hand))
        count += 1


print("Dealer cards: ", h_hand[0], ", ", "(Hidden)", "\n","Value: ", orig_deck.get(h_hand[0]), "\n", "Your cards: ", p_hand, "\n" , "Value: ", p_value, "\n")

time.sleep(1)    

while player_turn == False:
    if p_value == 21:
        print ("You get ", hand, "\n", "Your cards: ", p_hand, "\n" , "Value: ", p_value)
        print("BLACKJACK!", "\n")
        time.sleep(1)
        player_turn = True
    elif p_value > 21:
        print ("You get ", hand, "\n", "Your cards: ", p_hand, "\n" , "Value: ", p_value, "\n")
        time.sleep(1)
        print("BUST!", "\n")
        player_turn = True
    else:
        prompt = input("Hit or stand? (h/s)")
        if prompt == "h":
            hand = random.choice(list(deck.keys()))
            deck.pop(hand)
            p_hand.append(hand)
            p_value += int(orig_deck.get(hand))
            print ("You get ", hand, "\n", "Your cards: ", p_hand, "\n" , "Value: ", p_value, "\n")
            time.sleep(1)
        elif prompt == "s":
            player_turn = True
    
time.sleep(1)    

print ("Dealer flips over card", "\n", "Dealer cards: ", h_hand, "\n","Value: ", h_value, "\n", "Your cards: ", p_hand, "\n" , "Value: ", p_value, "\n")

time.sleep(1)    

while dealer_turn == False:
    if h_value > 21:
        time.sleep(1)
        print ("Dealer gets ", hand, "\n", "Dealer cards: ", h_hand, "\n" , "Value: ", h_value, "\n")
        time.sleep(1)
        print("Dealer BUST")
        dealer_turn = True
    elif h_value == 21:
        time.sleep(1)
        print ("Dealer gets ", hand, "\n", "Dealer cards: ", p_hand, "\n" , "Value: ", p_value, "\n")
        time.sleep(1)
        print("Dealer BLACKJACK!")
        if h_value == p_value:
            print("Push!")   
        dealer_turn = True
    else:
        hand = random.choice(list(deck.keys()))
        deck.pop(hand)
        h_hand.append(hand)
        h_value += int(orig_deck.get(hand))
        print ("Dealer gets ", hand, "\n", "Dealer cards: ", h_hand, "\n" , "Value: ", h_value, "\n")
        time.sleep(1)
  #  play_prompt = input("Play again? (y/n)")
  #  if play_prompt == "y"
    




