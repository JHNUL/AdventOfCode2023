import functools


@functools.total_ordering
class HandPart2:
    def __init__(self, content):
        self.cards, self.bid = content
        self.hand_values = {
            "five_of_a_kind": 7,
            "four_of_a_kind": 6,
            "full_house": 5,
            "three_of_a_kind": 4,
            "two_pair": 3,
            "one_pair": 2,
            "high_card": 1,
        }
        self.symbols = "|J23456789TQKA"

    def _resolve_value(self):
        freq = {}
        jokers = len(self.cards) - len(self.cards.replace("J", ""))
        for card in self.cards:
            if card not in freq:
                freq[card] = 0
            freq[card] += 1
        if len(freq) == 1:
            return self.hand_values["five_of_a_kind"]
        elif len(freq) == 2:
            # four of a kind
            if list(freq.values())[0] == 1 or list(freq.values())[0] == 4:
                if jokers > 0:
                    return self.hand_values["five_of_a_kind"]
                return self.hand_values["four_of_a_kind"]
            # full house
            if list(freq.values())[0] == 2 or list(freq.values())[0] == 3:
                if jokers > 1:
                    return self.hand_values["five_of_a_kind"]
                return self.hand_values["full_house"]
        elif len(freq) == 3:
            # tree of a kind
            if 3 in list(freq.values()):
                if jokers > 0:
                    return self.hand_values["four_of_a_kind"]
                return self.hand_values["three_of_a_kind"]
            # two pair
            if sorted(list(freq.values())) == [1, 2, 2]:
                if jokers == 2:
                    return self.hand_values["four_of_a_kind"]
                if jokers == 1:
                    return self.hand_values["full_house"]
                return self.hand_values["two_pair"]
        elif len(freq) == 4:
            if jokers > 0:
                return self.hand_values["three_of_a_kind"]
            return self.hand_values["one_pair"]
        elif jokers > 0:
            return self.hand_values["one_pair"]
        else:
            return self.hand_values["high_card"]

    def __lt__(self, other: 'HandPart2'):
        first = self._resolve_value()
        second = other._resolve_value()
        if first > second:
            return False
        if first == second:
            cards1 = self.cards
            cards2 = other.cards
            for i in range(0, len(cards1)):
                card1_val = self.symbols.index(cards1[i])
                card2_val = self.symbols.index(cards2[i])
                if card1_val > card2_val:
                    return False
                elif card1_val < card2_val:
                    return True
            return False
        return True

    def __eq__(self, other: 'HandPart2'):
        first = self._resolve_value()
        second = other._resolve_value()
        return first == second and self.cards == other.cards

    def __repr__(self) -> str:
        return f"{(self.cards, self.bid)}"
