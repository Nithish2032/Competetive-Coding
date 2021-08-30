def solve():
    MIN = 0
    CELLS_LIST =[]
    WAYS = 0
    #checking rows
    for i in range(N): 
        tempMIN = 0
        tempCELLS = []
        for j in range(N):
            element = matrix[i][j]
            if element == "O":
                tempMIN = 0
                break
            elif element == ".":
                tempMIN += 1
                tempCELLS.append((i,j))

        if tempMIN > 0:
            if tempMIN < MIN:
                MIN =  tempMIN 
                WAYS = 1
                CELLS_LIST.clear()
                CELLS_LIST.append(set(tempCELLS))
            elif tempMIN == MIN:
                if set(tempCELLS) in CELLS_LIST:
                    continue
                CELLS_LIST.append(set(tempCELLS))                
                WAYS += 1
                
            if MIN == 0:
                MIN = tempMIN
                WAYS =1
                CELLS_LIST.append(set(tempCELLS))                   
    
    #checking columns
    for i in range(N):
        tempMIN = 0
        tempCELLS = []
        for j in range(N):
            element = matrix[j][i]

            if element == "O":
                tempMIN = 0
                break
            elif element == ".":
                tempMIN += 1
                tempCELLS.append((j,i))

        if tempMIN > 0:
            if tempMIN < MIN:
                MIN =  tempMIN 
                WAYS = 1
                CELLS_LIST.clear()
                CELLS_LIST.append(set(tempCELLS))
            elif tempMIN == MIN:
                if set(tempCELLS) in CELLS_LIST:
                    continue
                CELLS_LIST.append(set(tempCELLS)) 
                WAYS += 1 
            if MIN == 0:
                MIN = tempMIN
                WAYS =1
                CELLS_LIST.append(set(tempCELLS)) 
    if MIN ==0:
        return "Impossible"
    return f"{MIN} {WAYS}"



T = int(input())
fh = open("output.txt","w")
for i in range(T):
    N = int(input())
    matrix = [["X" for j in range(N)] for i in range(N)]
    for j in range(N):
        matrix[j] = list(input())        
    fh.write(f"Case #{i+1}: {solve()}\n")

















