def getDistances(dist,nodes): 
    for k in nodes:
        for i in nodes:
            for j in nodes: 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    return dist

def toChar(v):
    steps = 0
    for u in string:
        if (u in DIST.keys() and DIST[u][v] != INF):
            steps += DIST[u][v]
        else:
            return False
    return steps            


def solve():
    global NODES,INF,MIN_STEPS,DIST
    if len(string) < 2:
        return 0

    LOOK_UP = {}

    for u in NODES:
        if u not in LOOK_UP.keys():
            LOOK_UP[u]={}
        for v in NODES:
            if v not in LOOK_UP[u].keys():
                LOOK_UP[u][v] = {}
            if u==v:
                LOOK_UP[u][v] = 0
                continue
            LOOK_UP[u][v] = INF
    
    for u in NODES:
        if u not in transMap.keys():
            continue
        for v in transMap[u]:
            LOOK_UP[u][v] = 1
    
    DIST = getDistances(LOOK_UP, NODES)
    for char in NODES:
        tempSteps = toChar(char)    
        if tempSteps == False:
            continue
        if tempSteps < MIN_STEPS:
            MIN_STEPS = tempSteps
    if MIN_STEPS == INF :
        return -1        
    return MIN_STEPS       

INF = float("inf")
T = int(input())
fh = open("ouput_consistency_2.txt","w")
for i in range(T):
    string = input()
    K = int(input())
    transMap = {}
    NODES = []
    MIN_STEPS = INF
    DIST = ""
    for _ in range(K):
        temp = input()
        if temp[0] not in transMap.keys():
            transMap[temp[0]]=[]            
        transMap[temp[0]].append(temp[1])
        NODES.append(temp[0])
        NODES.append(temp[1])
    NODES = list(set(NODES))    

    fh.write(f"Case #{i+1}: {solve()}\n")    






















