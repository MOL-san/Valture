from scipy.stats import rankdata
import numpy as np


def sumire(table=[], player={}, player2={}, name="", table_f=[]):
    
    exp_2 = []
    order = list(range(-5, 0)) + list(range(1, 11))
   
    if name:
        return "ENOSUMI"

    if len(player["card"]) == 1:
        return player["card"][0]


    for i in table_f:
        if i == table_f[-1]:
            break
        order.remove(i)
    # table_fは今までに出た札を取得するためにvalture.pyに追加


    for a in player["card"]:
        exp_1=[]
        for b in player2["card"]:
            exp_1.append(abs(a - b))
        exp_2.append(sum(exp_1))
    #期待値てきなのを求める(指針としては負けるならなるべく相手との差が大きく、勝つなら相手との差が小さくなるようにする)
    
    d = np.array(order)
    e = np.abs(d)
    order_list = e.tolist()
    order_list.sort()
    #orderを絶対値を取って昇順に並べる(うまくいってない)
 

    s1 = sum(table)
    #table pointを求める
    if s1 < 11:
        s2 = abs(s1)
        if order_list[0] > s2:
            order_list.insert(0, s2)
        elif order_list[-1] < s2:
            order_list.append(s2)
        else:
            for i in range(0, len(order_list)):
                if order_list[i] <= s2 < order_list[i + 1]:
                  order_list.insert(i+1, s2)
                  break
        o = order_list.index(s2)
    else:
        o = len(order_list) - 1
    #場のポイントが何枚で残りの札の中で何番目に重要かを求める
    
    list1 = list(rankdata(np.array(exp_2)))
    x = list1.index(o)
        
    return player["card"][x]
