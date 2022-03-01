from deck import Deck
from game import Game
from player import Player

player_one = Player('CPU One')
player_two = Player('CPU Two')

game_deck = Deck()

for x in range(26):
    player_one.add_cards(game_deck.deal_card())
    player_two.add_cards(game_deck.deal_card())

game_on = True

round_number = 0

while game_on:
    round_number += 1
    print(f'Round {round_number}')

    if len(player_one.all_cards) == 0:
        print(f'{player_one.name} out of cards! {player_two.name} wins! ')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'{player_two.name} out of cards! {player_one.name} wins! ')
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        
        else:
            print('WAR!')
            if len(player_one.all_cards) < 3:
                print(f'{player_one.name} unable to declare war')
                print(f'{player_two.name} wins!' )
                game_on = False
                break
            
            elif len(player_two.all_cards) < 3:
                print(f'{player_two.name} unable to declare war')
                print(f'{player_one.name} wins!' )
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())