import random


def choice_min(t=[], p={}, p2={}, name=""):  # 常に最小を返す
    if name:
        return "CHOICE-SMALL"
    return min(p["card"])


def choice_max(t=[], p={}, p2={}, name=""):  # 常に最大を返す
    if name:
        return "CHOICE-BIG"
    return max(p["card"])


def choice_random(t=[], p={}, p2={}, name=""):  # ただのランダム
    if name:
        return "RANDOM-PLAYER"

    return random.choice(p['card'])


def sakura1(t=[], p={}, p2={}, name=""):  # 分割ランダム
    if name:
        return "SAKURA-v1"

    card = p["card"]
    card.sort()
    ind = 0

    if len(card) == 1:
        return card[0]

    ind = len(card) // 3

    small = card[:ind]
    big = card[ind:]

    if sum(t) > 0 or not small:
        return random.choice(big)
    return random.choice(small)


def sakura2(t=[], p={}, p2={}, name=""):  # 15を必ずとる
    if name:
        return "SAKURA-v2"

    card = p["card"]
    card.sort()
    ind = 0

    if len(card) == 1:
        return card[0]

    if sum(t) >= 10 and 15 in card:
        return 15

    elif 15 in card:
        card.remove(15)

    ind = len(card) // 3

    small = card[:ind]
    big = card[ind:]

    # print(small, big)

    if sum(t) > 0 or not small:
        return random.choice(big)
    return random.choice(small)


def sakura3(t=[], p={}, p2={}, name=""):  # 15,-5についてカードを設定
    if name:
        return "SAKURA-v3"

    card = p["card"]
    card.sort()
    ind = 0

    if len(card) <= 2:
        return card[0]

    # HIGHは敵の具合による
    HIGH = 1
    LOW = 5

    if sum(t) == 1 and HIGH in card:
        return HIGH
    if sum(t) == -5 and LOW in card:
        return LOW

    if HIGH in card:
        card.remove(HIGH)
    if LOW in card:
        card.remove(LOW)

    ind = len(card) // 3

    small = card[:ind]
    big = card[ind:]

    if sum(t) > 0 or not small:
        return random.choice(big)
    return random.choice(small)


def human(t=[], p1={}, p2={}, name=""):  # 人用
    if name:
        return input("名前:")

    print("持ち札:" + ", ".join(map(str, p1["card"])))
    choice_card = input("card: ")
    return int(choice_card)
