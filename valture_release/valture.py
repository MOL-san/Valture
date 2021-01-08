# ハゲタカのえじき
import random
import copy
import sys
import os
import io

from colorama import Fore, Back

from attached_players import *
from kutsukawa import kutsu1


def print_table(table, player1, player2):  # 状況表示
    print("Table:", ", ".join(map(str, table)))
    print("Table Point:", sum(table))
    print()
    print(f"{player1['name']}:", player1['point'])
    print(f"{player2['name']}:", player2['point'])
    print()


def game(p1, p2, print_board=True):  # 本体
    if not print_board:
        sys.stdout = io.StringIO()

    log = [[]]

    winner = -1

    valtures = list(range(-5, 0)) + list(range(1, 11))
    random.shuffle(valtures)
    table = []
    p1_card = list(range(1, 16))
    p2_card = list(range(1, 16))

    player1 = {"card": copy.copy(p1_card), "point": 0, "name": p1(name="name")}
    player2 = {"card": copy.copy(p2_card), "point": 0, "name": p2(name="name")}

    print("=====================================")
    print("ゲーム開始")

    for i in range(15):
        print("-------------------------------------")
        print(Fore.GREEN + "Turn " + str(i + 1) + Fore.RESET)
        table.append(valtures.pop())

        old_player1 = copy.copy(player1)
        old_player2 = copy.copy(player2)

        print_table(table, player1, player2)

        try:
            p1_oper = p1(table, player1, player2)
        except:
            print(f"{player1['name']} エラーにより失格")
            print(f"{player2['name']} 勝利")
            winner = 2
            break
        try:
            p2_oper = p2(table, player2, player1)
        except:
            print(f"{player2['name']} エラーにより失格")
            print(f"{player1['name']} 勝利")
            winner = 1
            break

        if p1_oper not in p1_card or (player2 != old_player2):
            print(f"{player1['name']} 無効な操作により失格")
            print(f"{player2['name']} 勝利")
            winner = 2
            break

        if p2_oper not in p2_card or (player1 != old_player1):
            print(f"{player2['name']} 無効な操作により失格")
            print(f"{player1['name']} 勝利")
            winner = 1
            break

        print(f"{player1['name']}のカード:", p1_oper)
        print(f"{player2['name']}のカード:", p2_oper)

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

        print()

        if win == 0:
            print("スキップ")
            continue
        elif win == 1:
            print(f"{player1['name']}の得点", end=" -> ")
            player1['point'] += sum(table)
        else:
            print(f"{player2['name']}の得点", end=" -> ")
            player2['point'] += sum(table)

        c = Back.LIGHTGREEN_EX
        if sum(table) < 0:
            c = Back.BLUE
        print(c + str(sum(table)) + Back.RESET)
        table = []

    if winner != -1:
        sys.stdout = sys.__stdout__
        log.extend([winner, player1["point"], player2["point"], False])
        return log

    print("-------------------------------------")
    p1_point = player1['point']
    p2_point = player2['point']

    winner = 0

    print(f"{player1['name']} vs {player2['name']}")
    print(" " * (len(player1["name"]) - 2) + str(p1_point).zfill(2),
          " " * (len(player2["name"]) + 1) + str(p2_point).zfill(2))
    if p1_point > p2_point:
        print(f"{player1['name']}の勝利")
        winner = 1
    elif p1_point < p2_point:
        print(f"{player2['name']}の勝利")
        winner = 2
    else:
        print("引き分け")
    print("=====================================")

    log.extend([winner, p1_point, p2_point, True])
    sys.stdout = sys.__stdout__
    return log

if __name__ == "__main__":
    # 統計を取る

    # プレイヤーの設定
    p1_func = person
    p2_func = kutsu1
    P1_NAME = p1_func(name="name")
    P2_NAME = p2_func(name="name")

    # 試合をする
    result = [0, 0, 0]
    MATCHES = 1

    SHOW_PROGRESS = 0
    SHOW_GAME = 1

    l = max([len(P1_NAME), len(P2_NAME)])
    labels = [P1_NAME.ljust(l) + ":", P2_NAME.ljust(l) +
              ":", "DRAW".ljust(l) + ":"]

    for i in range(MATCHES):
        result[game(p1_func, p2_func, SHOW_GAME)[-4]] += 1

        if SHOW_PROGRESS:
            os.system("clear")

            total = sum(result)
            print(i + 1)
            print(labels[0], "#" * int(result[1] / total * 100))
            print(labels[1], "#" * int(result[2] / total * 100))
            print(labels[2], "#" * int(result[0] / total * 100))
    os.system("clear")

    # 結果を集計
    P1_PERCENT = round(result[1] / sum(result) * 100, 2)
    P2_PERCENT = round(result[2] / sum(result) * 100, 2)
    DRAW_PERCENT = round(result[0] / sum(result) * 100, 2)

    # テキストを綺麗に表示する
    l = max([len(P1_NAME), len(P2_NAME)])
    match_text = "MATCHES: " + "{:,}".format(MATCHES)
    p1_text = labels[0] + f" {'{:,}'.format(result[1])}({P1_PERCENT}%)"
    p2_text = labels[1] + f" {'{:,}'.format(result[2])}({P2_PERCENT}%)"
    draw_text = labels[2] + f" {'{:,}'.format(result[0])}({DRAW_PERCENT}%)"

    text_len = max([len(p1_text), len(p2_text), len(draw_text)])
    print()
    print(match_text + "-" * (text_len - len(match_text) + 2))
    print("|" + p1_text.ljust(text_len) + "|")
    print("|" + p2_text.ljust(text_len) + "|")
    print("|" + draw_text.ljust(text_len) + "|")
    print("-" * (text_len + 2))

    # グラフを作る
    print()
    print("GRAPH")
    print("", labels[0] + " ", "#" * round(P1_PERCENT) + f"({P1_PERCENT}%)")
    print("", labels[1] + " ", "#" * round(P2_PERCENT) + f"({P2_PERCENT}%)")
    print("", labels[2] + " ", "#" * round(DRAW_PERCENT) + f"({DRAW_PERCENT}%)")
