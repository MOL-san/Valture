import random

#自分の手札と相手の手札で期待値的なのを求める作戦
#具体的には自分の手札のそれぞれに対して相手が出す札との差を求めて自分の手札と掛け算し、和で札を選択する。
#場の札の絶対値が残りの札の中で何番目かを計算して札を選択
#一回手動でエクセルを使ってやってみたところavesに対して41対-1で勝利
#面倒だったのでもう手動ではやらない



def sumire(table=[], player={}, player2={}, name=""):
    exp = []
    order_list = list(range(-5, 0)) + list(range(1, 11))


    if name:
        return "PLAYER"

    if len(card) == 1:
        return card[0]

    if player["point"] == 0 and player2["point"] == 0:
        return random.choice(player["card"])
        #最初はランダムで選択。それ以外で奇跡的にポイントが０対０だと困る。要改善。
    
    for i in player["card"]:
        x = player["card"][i]
        for j in player2["card"]:
            y = player["card"][j]
            z += (x - y)
        exp.append(z)
    
    #まだ絶対値を考慮できてない
    #場の札が残りで何枚目かを調べる＆リストから抜く
    o = order_list.index(sum(table))
    order_list.pop()
    #何枚目か、で手札を決める。rankづけ大変そう
    