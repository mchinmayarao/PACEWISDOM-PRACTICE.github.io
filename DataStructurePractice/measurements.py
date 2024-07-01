lower ,upper = 1100,1780
cups = [[200,250],[400,450],[800,850]]

res = []
ress = []
def solve(ind, low, high):
    if low>lower and high<upper:
        return True
    if high>upper  or ind>=len(cups):
        return False
    
    curL = low + cups[ind][0]
    curH = high + cups[ind][1]

    if solve(ind, curL,curH):
        res.append(([[cups[ind][0],cups[ind][1]], [curL,curH]]))
        return True
    if solve(ind + 1 , low,high):
        res.append(([[cups[ind+1][0],cups[ind+1][1]], [low,high]]))
        return True
    
    return False

print("status: " , solve(0,0,0))
print("lower , upper : " , lower, upper)
print("cups : " , cups)

print("trace: \n")
for e in res:
    print(e)
