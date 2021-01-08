from attached_players import choice_min, choice_max, choice_random, sakura1, sakura2, sakura3
import random


def analysis():
    p1, p2 = sakura2, sakura2
    # p1, p2 = choice_random, choice_random

    p1_cards = {i: [0, 0, 0] for i in list(range(-5, 0)) + list(range(1, 11))}
    p2_cards = {i: [0, 0, 0] for i in list(range(-5, 0)) + list(range(1, 11))}

    matches = 10000

    for i in range(matches):
        log = game(p1, p2, False)

        win = 2
        if log[-4] == 1:
            win = 0
        elif log[-4] == 2:
            win = 1

        for turn in log[0]:
            if turn[1] > turn[2]:
                for c in turn[0]:
                    p1_cards[c][win] += 1

            elif turn[1] < turn[2]:
                for c in turn[0]:
                    p2_cards[c][win] += 1

    for c in list(range(-5, 0)) + list(range(1, 11)):
        result1 = p1_cards[c]
        result2 = p2_cards[c]

        p1_cards[c].append(result1[0] / sum(result1) * 100)
        p2_cards[c].append(result2[0] / sum(result2) * 100)

    return p1_cards, p2_cards


def show_graph(log):
    for c in list(range(-5, 0)) + list(range(1, 11)):
        result = log[c]

        print(c, round(result[-1]), "%")

        print("win :", "+" * int(result[-1]))
        print("lose:", "-" * int(result[1] / sum(result) * 100))


def kutsu1(t=[], p={}, p2={}, name=""):
    if name:
        return "KUTSU-v1"

    return t[-1] + 6 if t[-1] < 0 else t[-1] + 5

    # valture_card = {
    #     -5: 1,
    #     -4: 2,
    #     -3: 3,
    #     -2: 4,
    #     -1: 5,
    #     1: 6,
    #     2: 7,
    #     3: 8,
    #     4: 9,
    #     5: 10,
    #     6: 11,
    #     7: 12,
    #     8: 13,
    #     9: 14,
    #     10: 15,

    # }

    # return valture_card[t[-1]]


if __name__ == "__main__":
    from valture import game

    p1_cards, p2_cards = analysis()

    priority = {p1_cards[i][-1]: i for i in p1_cards}

    show_graph(p1_cards)
    print("\n", "=" * 100, "\n")
    show_graph(p2_cards)
