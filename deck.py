from card import Card
class Deck:
    
    
    
    def __init__(self):
        self.all_cards = []

        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def __str__(self):
        return f'There are {len(self.all_cards)} card/s in this deck'
