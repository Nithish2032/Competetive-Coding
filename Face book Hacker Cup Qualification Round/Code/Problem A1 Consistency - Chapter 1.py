def solve():
    NV = 0
    SV = 0
    NC = 0
    SC = 0
    Vfreqs = {}
    Cfreqs = {}
    if len(string)<2:
        return 0
    for i in range(len(string)):   
        if string[i] in "AEIOU":
            if string[i] not in Vfreqs.keys():
                Vfreqs[string[i]] = 0
                NV += 1
            Vfreqs[string[i]] += 1
            SV += 1             
        else:
            if string[i] not in Cfreqs.keys():
                Cfreqs[string[i]] = 0
                NC += 1
            Cfreqs[string[i]] += 1
            SC += 1 
    
    TOV = SC+2*(SV-(max(Vfreqs.values()) if len(Vfreqs)>0 else 0))  
    TOC = SV+2*(SC-(max(Cfreqs.values()) if len(Cfreqs)>0 else 0))
    return min(TOC,TOV)    

            

T = int(input())
fh = open("ouput_consistency_1.txt","w")
for i in range(T):
    string = input()
    fh.write(f"Case #{i+1}: {solve()}\n")