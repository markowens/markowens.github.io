import random
from dataclasses import dataclass, field
from typing import List, Any
import begin

card = {}
SUITS = ["H", "C", "S", "D"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9","T", "J", "Q", "K", "A"]

@dataclass
class Card:
    rank: str
    suit: str
    rmap = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    def val(self):
        return self.rmap[self.rank]

@dataclass
class Hand:
    cards: List[Card]
    
    def get(self, pos):
        return self.cards[pos]

    def set(self, cardlist):
        for c in cardlist:
            self.cards.append(Card(c[0], c[1]))


    # def ranks(self):
    #     if not self.init:
    #         self.initialize()



@begin.start
def run():
    for suit in SUITS:
        for rank in RANKS:
            card[rank + suit] = Card(suit, rank)   

    card1 = Card("5", "C")
    card2 = Card("T", "D")
    print(f'card1 - rank/suit/val: {card1} - {card1.rank}/{card1.suit}/{card1.val()}')
    print(f'card2 - rank/suit/val: {card2} - {card2.rank}/{card2.suit}/{card2.val()}')

    hand = Hand([])
    hand.set(['AS', 'TD', '2C', '6S', 'QD'])
    print(f'hand: {hand}')
    print(f'hand[0]: {hand.get(0)}')
    print(f'hand[2]: {hand.get(2)}')

   # hand1 = Hand([card['AS'], card['TD'], card['2C'], card['6S'], card['QD']])
   # hand2 = Hand([Card("A", "C"), Card("K", "D"), Card("T", "H")])
   # print(f'hand1: {hand1}')
   # print(f'hand2: {hand2}')

        # print("--- ranks")
        # print(self.hand)
        
        # vals = []
        # for card in self.hand:
        #     print(card)
        #     self.cards.append(Card(card[0], card[1]))
            #self.cards
            #vals.append(card.val())
        #return sorted(vals, reverse=True)

    # def is_flush(self):
    #     suits = set()
    #     for card in self.cards:
    #         suits.add(card.suit)
    #     if len(suits) == 1:
    #         return True
    #     return False

    # def high_card(self):
    #     high = 0
    #     for card in self.cards:
    #         if card.val() > high:
    #             high = card.val()
    #     return high


    # def is_straight(self):
    #     ranks = []
    #     for card in self.cards:
    #         ranks.append(card.val())
    #     if max(ranks) - min(ranks) + 1 == 5:
    #         return True
    #     return False

    # def compare_ranks(self, hand):
    #     print(self.ranks())
    #     print(hand.ranks())
    #     return self.ranks() == hand.ranks()



# print(Deck())
# deck = Deck()
# print(deck.deal())

# hand = Hand(['QS', '4H', 'AS', '2D', '8C'])
# hand5 = Hand("4S 5D 2H 9C 4C")
# print(hand.ranks())
# print(hand5.ranks())
# print(hand)
# print(hand.ranks())
# print(hand.cards)
# print(hand.ranks())
# print(hand.is_flush())
# print(hand.is_straight())
# print(hand.high_card())


# print(hand1.cards)
# print(hand1.ranks())
# print(hand1.is_flush())
# print(hand1.is_straight())
# print(hand1.high_card())

# print(hand2.cards)
# print(hand2.ranks())
# print(hand2.is_flush())
# print(hand2.is_straight())
# print(hand2.high_card())        

# hand = Hand('QS 4H AS 2D 8C')
# hand1 = Hand('QS JH TS 9D 8C')
# hand2 = Hand('QS JS TS 9S 6S')
# hand3 = Hand('4S 5D 2H 9C 4C')
# print("---")
# print(hand)
# print(hand.ranks())
# print(hand1)
# print(hand1.ranks())
# print(hand2.ranks())
# print(hand3.ranks())

# print(hand.compare_ranks(hand1))
# print(hand.compare_ranks(hand2))
# print(hand1.compare_ranks(hand2))
# print(hand1.compare_ranks(hand3))


# @dataclass
# class Deck:
#     cards: List[Card] = field(default_factory=create_deck)
#     def deal(self):
#         print("Undefined")
#         return self.cards[0]

# def create_deck():
#     return [Card(r, s) for s in SUITS for r in RANKS]

# def create_hand():
#     the_hand = [Card("0", "0") for i in range(5) for j in range(5)]
#     print(the_hand)
#     return the_hand


# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# SUITS = "H D C S".split()