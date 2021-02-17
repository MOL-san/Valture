#encoding: utf-8
import random
import copy

def pick_random_card(cards):
    choiced = cards.pop(random.randint(0,len(cards)-1))
    return choiced

def game(table,card,cards,p1_cards,p2_cards,p1_score,p2_score):
    p1_c = card
    if p1_c in p1_cards: p1_cards.remove(p1_c)
    p2_c = pick_random_card(p2_cards)

    for i in range(15):
        table_point = sum(table)
        if p1_c == p2_c:
            pass
        elif table_point < 0:
            if p1_c < p2_c:
                p1_score += table_point
            else:
                p2_score += table_point
            table = []
        else:
            if p1_c > p2_c:
                p1_score += table_point
            else:
                p2_score += table_point
            table = []

        if not p1_cards:
            break
        p1_c = pick_random_card(p1_cards)
        p2_c = pick_random_card(p2_cards)
        table.append(pick_random_card(cards))

    if p1_score > p2_score: return True
    else: return False
        
#def game(table,card,cards,p1_cards,p2_cards,p1_score,p2_score):
def aves(table=[],player1={},player2={},name=""):
    if name != "": return "aves"

    if "left" not in player1: player1["left"] = list(range(-5,0)) + list(range(1,11))
    player1["left"].remove(table[-1])

    p1_cards = player1["card"]
    p2_cards = player2["card"]
    p1_score = player1["point"]
    p2_score = player2["point"]
    N = 500

    win_count = {c:0 for c in p1_cards}
    for card in p1_cards:
        for i in range(N):
            win_count[card] += game(table[:],card,player1["left"][:],p1_cards[:],p2_cards[:],p1_score,p2_score)
    
    max_win = max(win_count, key=win_count.get)
    lower = win_count[max_win] * 0.9
    cards = []
    for k in win_count:
        if win_count[k] >= lower: cards.append(k)

    choiced = max(cards)
    choiced = min(cards)
    choiced = random.choice(cards)

    """
    diff = player1["point"] - player2["point"]
    if diff > 10:
        choiced = min(cards)
    elif diff < -5:
        choiced = max(cards)
    else:
        choiced = random.choice(cards[1:-1] if cards[1:-1] else cards)
    """

    print (float(win_count[choiced]) / N) * 100,"%"
    print win_count

    return choiced

def aves2(table=[],player1={},player2={},name=""):
    if name != "": return "AvesII"

    diff = player1["point"] - player2["point"]
    p1_cards = sorted(player1["card"])

    if diff > 5:
        list_range = p1_cards[0:len(p1_cards)/3]
    elif diff < -5:
        list_range = p1_cards[len(p1_cards)/3*2:len(p1_cards)]
    else:
        list_range = p1_cards[len(p1_cards)/3:len(p1_cards)/3*2]
    if not list_range: list_range = p1_cards

    return random.choice(list_range)

 
def aves3(table=[],player1={},player2={},name=""):
    if name != "": return "AVESIII"

    card = table[-1]
    list_range = []
    diff = player1["point"] - player2["point"]
    p1_cards = sorted(player1["card"])

    if card == -5:
        list_range = [12]
    elif card == -4:
        list_range = [10,11,12]
    elif card == -3:
        list_range = [9,10,11]
    elif card == -2:
        list_range = [7,8]
    elif card == -1:
        list_range = [p1_cards[0]]
    elif card == 1:
        list_range = [p1_cards[0]]
    elif card == 2:
        list_range = [p1_cards[0]]
    elif card == 3:
        list_range = [7,8,9,10]
    elif card == 4:
        list_range = [7,8,9,10]
    elif card == 5:
        list_range = [7,8,9,10]
    elif card == 6:
        list_range = [13,14,15]
    elif card == 7:
        list_range = [14,15,15]
    elif card == 8:
        if diff < -5:
            list_range = [13,14,15]
        list_range = [p1_cards[0]]
    elif card == 9:
        if diff < -5:
            list_range = [13,14,15]
        list_range = [p1_cards[0]]
    else:
        if diff < -5:
            list_range = [13,14,15]
        list_range = [p1_cards[0]]

    common = list(set(list_range) & set(p1_cards))
    if not common:
        if diff > 5:
            list_range = p1_cards[0:len(p1_cards)/3]
        elif diff < -5:
            list_range = p1_cards[len(p1_cards)/3*2:len(p1_cards)]
        else:
            list_range = p1_cards[len(p1_cards)/3:len(p1_cards)/3*2]
        if not list_range: list_range = p1_cards
    else:
        list_range = common

    return random.choice(list_range)
