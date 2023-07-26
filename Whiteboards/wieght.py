#U: must take 1 weight 1 and 1 from wieght 2
#set carrying capacity and then conditional statements to decide what can and cannot be carried
#P: If value of weight 1 and value of weight 2 <= max weight return can carry both
    #or if weight 1 <= max weight and weight 1 + weight 2> max w
    # weight if wiehgt 2<= max weight and weight 1 + weight 2> max w
    # else return 0
#e:
def carrying_weight(v1, w1, v2, w2, maxw):
    if w1 + w2 <= maxw:
        return v1 + v2
    elif v1 >= v2 or w2 > maxw and w1 <= maxw and w1 + w2 > maxw:
        return v1
    elif v2 >= v1 or w1 >maxw and w2 <= maxw and w1 + w2 > maxw:
        return v2
    else:
        return 0
print(carrying_weight(5,3,7,4,4))