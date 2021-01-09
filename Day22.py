from collections import deque

with open('data/advent2020/input22.txt') as file:
    players = [player.split('\n') for player in file.read().strip().split('\n\n')]

round_number = 0
hands = [deque(map(int, player[1:])) for player in players]
while all(hands):
    round_number += 1
    drawn_cards: list[int] = [hand.popleft() for hand in hands]
    print(f'Round {round_number}: cards: {drawn_cards}, hands: {hands}')
    winner, loser = (0, 1) if drawn_cards[0] > drawn_cards[1] else (1, 0)
    for i in winner, loser:
        hands[winner].append(drawn_cards[i])
print(f'Player {winner + 1} wins')
card_values: list[int] = [(i + 1) * card for i, card in enumerate(reversed(hands[winner]))]
print(sum(card_values))
