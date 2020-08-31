from poker.hand import Hand
from poker.card import Card
import unittest


class TestHand(unittest.TestCase):
    def test_hand_type(self):
        hand = Hand()
        self.assertEqual(type(hand.cards), list)

    def test_hand_representation(self):
        hand = Hand()
        cards = [Card("7", "Hearts"), Card("8", "Hearts")]
        hand.add_cards(cards)
        cards.sort(reverse=True)
        self.assertEqual(repr(hand), "8 of Hearts, 7 of Hearts")

    def test_receive_and_store_cards(self):
        hand = Hand()
        cards = [Card("7", "Hearts"), Card("8", "Hearts")]
        hand.add_cards(cards)
        cards.sort(reverse=True)
        self.assertEqual(hand.cards, cards)

    def test_high_card_hand_value(self):
        hand = [
            Card("7", "Diamonds"),
            Card("Ace", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.value, 13)

    def test_hand_return_high_card(self):
        hand = [
            Card("7", "Diamonds"),
            Card("Ace", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "High Card")

    def test_hand_return_pair(self):
        hand = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Pair")

    def test_hand_return_two_pair(self):
        hand = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("7", "Clubs"),
            Card("7", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Two Pair")

    def test_hand_return_three_of_kind(self):
        hand = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Spades"),
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Three of a Kind")

    def test_hand_return_four_of_kind(self):
        hand = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts"),
            Card("Ace", "Spades")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Four of a Kind")

    def test_hand_return_full_house(self):
        hand = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts"),
            Card("7", "Spades"),
            Card("7", "Spades")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Full House")

    def test_hand_return_flush(self):
        hand = [
            Card("2", "Diamonds"),
            Card("4", "Diamonds"),
            Card("6", "Diamonds"),
            Card("8", "Diamonds"),
            Card("10", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Flush")

    def test_hand_return_straight(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("6", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Straight")

    def test_hand_return_straight_flush(self):
        hand = [
            Card("2", "Diamonds"),
            Card("3", "Diamonds"),
            Card("4", "Diamonds"),
            Card("5", "Diamonds"),
            Card("6", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Straight Flush")

    def test_hand_return_royal_flush(self):
        hand = [
            Card("Ace", "Diamonds"),
            Card("King", "Diamonds"),
            Card("Queen", "Diamonds"),
            Card("10", "Diamonds"),
            Card("Jack", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Royal Flush")

    def test_hand_value_royal_flush(self):
        hand = [
            Card("Ace", "Diamonds"),
            Card("King", "Diamonds"),
            Card("Queen", "Diamonds"),
            Card("10", "Diamonds"),
            Card("Jack", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        # as it stands ((hand score ** hand score) * sum of hand cards values)
        self.assertEqual(cards.score, 1000 + sum([13, 12, 11, 10, 9]))

    def test_hand_value_low_straight(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("6", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.score, 500 + sum([1, 2, 3, 4, 5]))

    def test_hand_value_low_two_pair(self):
        hand = [
            Card("2", "Clubs"),
            Card("2", "Diamonds"),
            Card("7", "Clubs"),
            Card("7", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.score, (300 + sum([1, 1, 6, 6])))

    def test_hand_value_pair(self):
        hand = [
            Card("2", "Clubs"),
            Card("2", "Diamonds"),
            Card("8", "Clubs"),
            Card("7", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.score, (200 + sum([1, 1])))

    def test_hand_high_card_hand_value(self):
        hand = [
            Card("Ace", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("6", "Diamonds")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.score, (100 + sum([13])))

    def test_hands_value_vs_other_hand_value(self):
        hand_a = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("2", "Clubs"),
            Card("3", "Diamonds")
        ]
        # hand_a_value = (20 * sum([13, 13])) + sum([13, 13, 1, 2])
        # print(hand_a_value)
        hand_b = [
            Card("Ace", "Clubs"),
            Card("Queen", "Diamonds"),
            Card("10", "Clubs"),
            Card("10", "Diamonds")
        ]
        # hand_b_value = (20 * sum([10, 10])) + sum([13, 11, 10, 10])
        # print(hand_b_value)
        cards_a = Hand()
        cards_a.add_cards(hand_a)
        cards_b = Hand()
        cards_b.add_cards(hand_b)
        self.assertEqual(cards_a > cards_b, True)

    def test_hands_equality(self):
        hand_a = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("2", "Clubs"),
            Card("3", "Diamonds")
        ]
        cards_a = Hand()
        cards_a.add_cards(hand_a)
        cards_b = Hand()
        cards_b.add_cards(hand_a)
        self.assertEqual(cards_a == cards_b, True)

    def test_hands_low_pair_vs_high_card(self):
        hand_a = [
            Card("Ace", "Clubs"),
            Card("Queen", "Diamonds"),
            Card("Jack", "Clubs"),
            Card("King", "Diamonds"),
            Card("9", "Diamonds")
        ]
        hand_b = [
            Card("2", "Clubs"),
            Card("4", "Diamonds"),
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("5", "Diamonds")
        ]
        cards_a = Hand()
        cards_a.add_cards(hand_a)
        cards_b = Hand()
        cards_b.add_cards(hand_b)
        self.assertEqual(cards_a < cards_b, True)

    def test_remove_cards(self):
        hand_a = [
            Card("Ace", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("2", "Clubs"),
            Card("3", "Diamonds")
        ]
        cards_a = Hand(hand_a)
        cards_b = Hand(hand_a)
        cards_a.remove_cards()
        self.assertEqual(cards_a == cards_b, False)

    def test_hand_value_low_straight_7_cards(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("6", "Diamonds"),
            Card("10", "Diamonds"),
            Card("3", "Hearts")
        ]
        cards = Hand()
        cards.add_cards(hand)
        self.assertEqual(cards.hand, "Straight")
