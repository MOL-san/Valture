#encoding: utf-8

def agent(t=[], p={}, p2={}, name=""):
    if name != "":
        return player_name
    return player(t,p["card"],p2["card"],p["point"],p2["point"])
#この上書き換え非推奨

import random

table = None
my_card = None
enemy_card = None
my_score = None
enemy_score = None
player_name = None
card = None
diff = None

# table: 場に出ているカードの一覧
# my_card: 自分の持っているカードの一覧
# enemy_card: 相手の持っているカードの一覧
# my_score: 現在の自分の得点
# enemy_score: 現在の相手の得点
#
#
def player(table, my_card, enemy_card, my_score, enemy_score):
  global player_name, card, diff
  diff = my_score - enemy_score
  card = random.choice(my_card)
  return card


player_name = 'test'
