import random
from utils import (get_user_input, get_user_to_press_enter, randomize_player_order)
from UnoDeck import UnoDeck
from Card import Card
from Player import Player

COLORS = ["red", "blue", "green", "yellow"]
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
NUMBERS_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
OTHER_CARDS = ["skip", "reverse", "draw"]
# 4 blank cards
# 4 wild cards

def initialize_deck():
    deck = []
    # red cards
    number_cards = [Card("red", "number", num) for num in NUMBERS]
    number_cards_2 = [Card("red", "number", num) for num in NUMBERS_2]
    skip_cards = [Card("red", "skip", -1) for _ in range(2)]
    reverse_cards = [Card("red", "reverse", -1) for _ in range(2)]
    draw_cards = [Card("red", "draw", -1) for _ in range(2)]
    deck.extend(number_cards)
    deck.extend(number_cards_2)
    deck.extend(skip_cards)
    deck.extend(reverse_cards)
    deck.extend(draw_cards)

    # green cards
    number_cards = [Card("green", "number", num) for num in NUMBERS]
    number_cards_2 = [Card("green", "number", num) for num in NUMBERS_2]
    skip_cards = [Card("green", "skip", -1) for _ in range(2)]
    reverse_cards = [Card("green", "reverse", -1) for _ in range(2)]
    draw_cards = [Card("green", "draw", -1) for _ in range(2)]
    deck.extend(number_cards)
    deck.extend(number_cards_2)
    deck.extend(skip_cards)
    deck.extend(reverse_cards)
    deck.extend(draw_cards)

    # blue cards
    number_cards = [Card("blue", "number", num) for num in NUMBERS]
    number_cards_2 = [Card("blue", "number", num) for num in NUMBERS_2]
    skip_cards = [Card("blue", "skip", -1) for _ in range(2)]
    reverse_cards = [Card("blue", "reverse", -1) for _ in range(2)]
    draw_cards = [Card("blue", "draw", -1) for _ in range(2)]
    deck.extend(number_cards)
    deck.extend(number_cards_2)
    deck.extend(skip_cards)
    deck.extend(reverse_cards)
    deck.extend(draw_cards)

    # yellow cards
    number_cards = [Card("yellow", "number", num) for num in NUMBERS]
    number_cards_2 = [Card("yellow", "number", num) for num in NUMBERS_2]
    skip_cards = [Card("yellow", "skip", -1) for _ in range(2)]
    reverse_cards = [Card("yellow", "reverse", -1) for _ in range(2)]
    draw_cards = [Card("yellow", "draw", -1) for _ in range(2)]
    deck.extend(number_cards)
    deck.extend(number_cards_2)
    deck.extend(skip_cards)
    deck.extend(reverse_cards)
    deck.extend(draw_cards)

    blank_card = [Card("blank", "blank", -1) for _ in range(4)]
    wild_card = [Card("wild", "wild", -1) for _ in range(4)]
    deck.extend(blank_card)
    deck.extend(wild_card)

    return deck

def reshuffle_deck(deck):
    random.shuffle(deck)
    return deck

def game():
    print(f"***UNO GAME***")
    uno_deck = UnoDeck()

    keep_playing = True
    round_counter = 1
    player_name = ""

    while keep_playing:
        deck = uno_deck.get_shuffled_deck()

        if not player_name:
            player_name = 'abc' #get_user_input()
            # initialize players
            player1 = Player(name=player_name, point=0)
            player2 = Player(name="Computer", point=0)

        print(f"Round #{round_counter}")
        top_14_cards = uno_deck.get_top_14_cards()

        # give 7 cards to each player
        for i in range(len(top_14_cards)):
            if i%2==0:
                player1.give_card_to_player(deck[i])
            else:
                player2.give_card_to_player(deck[i])

        # pick a player to start by randomizing their order
        players_list = randomize_player_order([player1, player2])
        print(f"{players_list[0]} will start the game")
        if players_list[0].name == 'Computer':
            print("it is computer")
        played_card_list = []
        while len(players_list)>0:
            players_list.pop()
        player_counter = 0
        first_shot = True

        print("done")
        # while(player1.has_number_of_cards() != 0 or
        #       player2.has_number_of_cards() != 0):
        #
        #     if player_counter > 1:
        #         player_counter = 0
        #
        #     print(f"Playing player {players_list[player_counter]}")
        #
        #     card1 = players_list[player_counter].present_card()
        #
        #     # if first_shot:
        #     #     print(f"First player is {players_list[player_counter]}")
        #     #     card1 = players_list[player_counter].present_first_card()
        #     #     first_shot = False
        #
        #     player_counter += 1
        #     print("game ongoing")
        #     get_user_to_press_enter()


        round_counter += 1

def main():
    game()


if __name__ == "__main__":
    main()
