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

    if len(player_two.all_cards) == 0:
        print(f'{player_two.name} out of cards! {player_one.name} wins! ')
        game_on = False