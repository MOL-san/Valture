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

    d = np.array(order)
    arr = np.abs(d)
    order_list = list(arr)
    order_list.sort()

    for a in player["card"]:
        exp_1=[]
        for b in player2["card"]:
            exp_1.append(abs(a - b))
        exp_2.append(sum(exp_1))


    s1 = sum(table)
    if s1 <= 11:
        s2 = abs(s1)
        if order_list[0] > s2:
            order_list.insert(0, s2)
        elif order_list[-1] < s2:
            order_list.append(s2)
        else:
            for i in range(0, len(order_list)-1):
                if order_list[i] <= s2 < order_list[i + 1]:
                  order_list.insert(i+1, s2)
                  break
        o = order_list.index(s2)
    else:
        o = -1

    
    list1 = list(rankdata(np.array(exp_2), method = "min"))
    if o in list1:
        x=list1.index(o)
    elif o-1 in list1:
        x=list1.index(o-1)
    elif o+1 in list1:
        x = list1.index(o+1)
    else:
        x=list1.index(max(list1))
        
    return player["card"][x]
