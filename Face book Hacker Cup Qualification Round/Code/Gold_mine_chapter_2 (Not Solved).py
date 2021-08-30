import itertools
from itertools import combinations

def GetPermutations(baseList):
    return list(itertools.permutations([1, 2, 3]))

def GetSubSeqs(perm):
    global ALL_PATHS
    ALL_PATHS.append(sum(map(lambda r: list(combinations(perm, r)), range(1, len(perm)+1)), []))


def GetAllPaths():

    ALL_PERMS = GetPermutations(i)
    print(f"ALL_PERMS : {ALL_PERMS}")
    for perm in ALL_PERMS:
        GetSubSeqs(perm)

def solve():
    global Tunnels,ALL_PATHS
    GetAllPaths()
    return ALL_PATHS


T = int(input())
Tunnels = []
ALL_PATHS = []
fh = open("Gold_mine_chapter_2_Output.txt","w")
for i in range(1,T+1):
    N,K = tuple(map(int,input().split()))
    GOLDS = [0]+list(map(int,input().split()))
    for _ in range(N):
        tempTunnel = input().split()
        Tunnels.append(tempTunnel)
    fh.write(f"Case #{i} {solve()}")    