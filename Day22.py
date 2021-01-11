from collections import deque

Deck = deque[int]
with open('data/advent2020/input22_test.txt') as file:
    player_input: list[str] = file.read().strip().split('\n\n')
decks: list[Deck] = [deque(map(int, player.split('\n')[1:])) for player in player_input]
round_number = 0
winner, loser = 0, 0  # To avoid warning

while all(decks):
    round_number += 1
    drawn_cards: list[int] = [deck.popleft() for deck in decks]
    print(f'Round {round_number}: cards: {drawn_cards}, decks: {decks}')
    winner, loser = (0, 1) if drawn_cards[0] > drawn_cards[1] else (1, 0)
    for i in winner, loser:
        decks[winner].append(drawn_cards[i])
print(f'Player {winner + 1} wins')
print(sum([(i + 1) * card for i, card in enumerate(reversed(decks[winner]))]))
