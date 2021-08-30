
def Get_All_Paths(node,PATH):
    global ALL_PATHS
    PATH=f"{PATH} {node}".strip()   
    if node !='1' and len(Tunnels[node])==1:
        ALL_PATHS.append(PATH)
        return    
    for nxt in Tunnels[node]:
        if nxt not in PATH.split() :   
            Get_All_Paths(nxt,PATH)

def Get_Profits():
    for path in ALL_PATHS:
        profit=0
        for Cave in path.split():
            profit += Golds[int(Cave)] 
        TOTAL_PROFITS[path]=profit
    #print(f"TOTAL_PROFITS : {TOTAL_PROFITS}")        

def NO_COMMON_TUNNEL(path1,path2):
    path1 = path1.split()
    for i in range(len(path1)-1):
        if f"{path1[i]} {path1[i+1]}" in path2:
            return False
    return True        

def solve():
    global Cave_Count,Golds,Tunnels,ALL_PATHS
    Get_All_Paths("1","")
    Get_Profits()
    MAX_PROFIT = max(TOTAL_PROFITS.values())
    if len(ALL_PATHS) == 1:
        return TOTAL_PROFITS[ALL_PATHS[0]]

    for path1 in ALL_PATHS:
        for path2 in ALL_PATHS:
            if path1 == path2:
                continue
            profit = 0
            if NO_COMMON_TUNNEL(path1,path2):
                profit = TOTAL_PROFITS[path1]+TOTAL_PROFITS[path2]-Golds[1]
            if profit > MAX_PROFIT:
                MAX_PROFIT = profit   
    return MAX_PROFIT               

T = int(input())
fh = open("Output_Gold_Mine_Chapter_1.txt","w")
for i in range(1,T+1):
    ALL_PATHS = []
    TOTAL_PROFITS = {}
    Cave_Count = int(input())
    Golds = [0]+list(map(int,input().split()))
    Tunnels = {}
    if Cave_Count == 0:
        fh.write(f"Case #{i}: {0}\n")
        continue

    if Cave_Count == 1:
        fh.write(f"Case #{i}: {Golds[1]}\n")
        continue      

    for _ in range(Cave_Count-1):
        Src_Cave,Dest_Cave = tuple(input().split())
        if Src_Cave not in Tunnels.keys():
            Tunnels[Src_Cave] = []
        if Dest_Cave not in Tunnels.keys():
            Tunnels[Dest_Cave] = []
        Tunnels[Src_Cave].append(Dest_Cave)
        Tunnels[Dest_Cave].append(Src_Cave)
    #print(f"{Tunnels}")    
    # print("\n",solve())    
    fh.write(f"Case #{i}: {solve()}\n")
        





















