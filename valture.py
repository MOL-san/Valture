#encoding: utf-8

# ハゲタカのえじき
import random
import copy
import sys
import os
import io

from colorama import Fore, Back

from attached_players import *
from kutsukawa import kutsu1
from aves import *
from blockly import agent


def print_table(table, player1, player2):  # 状況表示
    print "Table      : ", ", ".join(map(str, table))
    print "Table Point: ", sum(table)
    print 
    l = max(len(player1["name"]),len(player2["name"]))
    print "{0}: {1}".format(player1["name"].rjust(l), player1['point'])
    print "{0}: {1}".format(player2["name"].rjust(l), player2['point'])
    print 


def game(p1, p2, p1_name, p2_name, print_board=True):  # 本体
    if not print_board:
        sys.stdout = open(os.devnull,"w")

    log = [[]]

    winner = -1

    valtures = list(range(-5, 0)) + list(range(1, 11))
    random.shuffle(valtures)
    table = []
    p1_card = list(range(1, 16))
    p2_card = list(range(1, 16))

    player1 = {"card": copy.copy(p1_card), "point": 0, "name": p1_name}
    player2 = {"card": copy.copy(p2_card), "point": 0, "name": p2_name}

    print "=" * 30
    print "ゲーム開始"

    for i in range(15):
        print "-------------------------------------"
        print Fore.GREEN + "Turn " + str(i + 1) + Fore.RESET
        table.append(valtures.pop())


        print_table(table, player1, player2)

        try:
            p1_oper = p1(table, player1, player2)
            old_player1 = copy.copy(player1)
        except:
            print "{0} エラーにより失格".format(player1["name"])
            print "{0} 勝利".format(player2["name"])
            winner = 2
            break
        try:
            p2_oper = p2(table, player2, player1)
            old_player2 = copy.copy(player2)
        except:
            print "{0} エラーにより失格".format(player2["name"])
            print "{0} 勝利".format(player1["name"])
            winner = 1
            break

        if p1_oper not in p1_card or (player2 != old_player2):
            print "{0} 無効な操作({1})により失格".format(player1["name"],p1_oper)
            print "{0} 勝利".format(player2["name"])
            winner = 2
            break

        if p2_oper not in p2_card or (player1 != old_player1):
            print "{0} 無効な操作({1})により失格".format(player2["name"],p2_oper)
            print "{0} 勝利".format(player1["name"])
            winner = 1
            break

        print "{0}のカード:".format(player1["name"]), p1_oper
        print "{0}のカード:".format(player2["name"]), p2_oper

        p1_card.remove(p1_oper)
        p2_card.remove(p2_oper)
        player1["card"] = copy.copy(p1_card)
        player2["card"] = copy.copy(p2_card)

        win = 1

        if p1_oper == p2_oper:
            win = 0

        elif sum(table) > 0:
            if p2_oper > p1_oper:
                win = 2
        elif sum(table) < 0:
            if p2_oper < p1_oper:
                win = 2

        log[-1].append([table, p1_oper, p2_oper])

        print

        if win == 0:
            print "スキップ"
            continue
        elif win == 1:
            print "{0}の得点".format(player1["name"]), "->",
            player1['point'] += sum(table)
        else:
            print "{0}の得点".format(player2["name"]), "->",
            player2['point'] += sum(table)

        c = Back.LIGHTGREEN_EX
        if sum(table) < 0:
            c = Back.BLUE
        print c + str(sum(table)) + Back.RESET
        table = []

    if winner != -1:
        sys.stdout = sys.__stdout__
        log.extend([winner, player1["point"], player2["point"], False])
        return log

    print "-------------------------------------"
    p1_point = player1['point']
    p2_point = player2['point']

    winner = 0

    os.system("clear")
    print "{0} vs {1}".format(player1["name"],player2["name"])
    print " " * (len(player1["name"]) - 2) + str(p1_point).zfill(2), " " * (len(player2["name"]) + 1) + str(p2_point).zfill(2)
    if p1_point > p2_point:
        print "{0}の勝利".format(player1["name"])
        winner = 1
    elif p1_point < p2_point:
        print "{0}の勝利".format(player2["name"])
        winner = 2
    else:
        print "引き分け"
    print "====================================="

    log.extend([winner, p1_point, p2_point, True])
    sys.stdout = sys.__stdout__
    return log

if __name__ == "__main__":
    # 統計を取る

    # プレイヤーの設定
    p1_func = human
    p2_func = aves
    P1_NAME = p1_func(name="name")
    P2_NAME = p2_func(name="name")

    # 試合をする
    result = [0, 0, 0]
    MATCHES = 10

    SHOW_PROGRESS = False
    #SHOW_GAME =     None

    SHOW_GAME = not SHOW_PROGRESS

    l = max([len(P1_NAME), len(P2_NAME)])
    labels = [P1_NAME.ljust(l) + ":", P2_NAME.ljust(l) +
              ":", "DRAW".ljust(l) + ":"]

    for i in range(MATCHES):
        result[game(p1_func, p2_func,P1_NAME,P2_NAME, SHOW_GAME)[-4]] += 1

        if SHOW_PROGRESS:
            #os.system("clear")

            total = sum(result)
            print i + 1
            print labels[0], "#" * int(float(result[1]) / total * 100) 
            print labels[1], "#" * int(float(result[2]) / total * 100) 
            print labels[2], "#" * int(float(result[0]) / total * 100) 
    #os.system("clear")

    # 結果を集計
    P1_PERCENT = round(float(result[1]) / sum(result) * 100, 2)
    P2_PERCENT = round(float(result[2]) / sum(result) * 100, 2)
    DRAW_PERCENT = round(float(result[0]) / sum(result) * 100, 2)

    # テキストを綺麗に表示する
    l = max([len(P1_NAME), len(P2_NAME)])
    match_text = "MATCHES: " + "{}".format(MATCHES)
    p1_text = labels[0] + " {0}({1}%)".format(result[1],P1_PERCENT)
    p2_text = labels[1] + " {0}({1}%)".format(result[2],P2_PERCENT)
    draw_text = labels[2] + " {0}({1}%)".format(result[0],DRAW_PERCENT)

    text_len = max([len(p1_text), len(p2_text), len(draw_text)])
    print
    print match_text + "-" * (text_len - len(match_text) + 2)
    print "|" + p1_text.ljust(text_len) + "|"
    print "|" + p2_text.ljust(text_len) + "|"
    print "|" + draw_text.ljust(text_len) + "|"
    print "-" * (text_len + 2)

    # グラフを作る
    print
    print "GRAPH" 
    print "", labels[0] + " ", "#" * int(round(P1_PERCENT)) + "({0}%)".format(P1_PERCENT)
    print "", labels[1] + " ", "#" * int(round(P2_PERCENT)) + "({0}%)".format(P2_PERCENT)
    print "", labels[2] + " ", "#" * int(round(DRAW_PERCENT)) + "({0}%)".format(DRAW_PERCENT)
