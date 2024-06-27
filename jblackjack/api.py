from ninja import NinjaAPI

import random 

  


api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.get("game")
def play(request):
    card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
    cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = [(card, category) for category in card_categories for card in cards_list] 
    def card_value(card, ace): 

        if card[0] in ['Jack', 'Queen', 'King']: 

            return 10

        elif card[0] == 'Ace':
            if ace == 'non-ace':
                return 1
            elif ace == 'ace':
                return 11

        else: 

            return int(card[0]) 
    def card_to_path(card):
        # Generate the file path dynamically
        return f"https://lostmypillow.github.io/assets/{card[0].lower()}_of_{card[1].lower()}.svg"



    random.shuffle(deck) 
    player_cards = [deck.pop(), deck.pop()] 

    house_cards = [deck.pop(), deck.pop()] 
    
    player_score = sum(card_value(card, 'non-ace') for card in player_cards)
    player_alt_score = sum(card_value(card, 'ace') for card in player_cards)

    house_score = sum(card_value(card, 'non-ace') for card in house_cards) 
    player_card_paths = [card_to_path(card) for card in player_cards]
    house_card_paths = [card_to_path(card) for card in house_cards]

    print("Cards Player Has:", player_cards) 

    print("Score Of The Player:", player_score) 
    return {"house_cards": house_cards,
            "house_score": house_score,
            "house_card_paths": house_card_paths,
        "player_cards": player_cards,
        "player_card_paths": player_card_paths,
            "player_score": player_score,
            "player_alt_score": player_alt_score,
            }