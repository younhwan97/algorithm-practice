str = input()
ppap = 'PPAP'

finish_loof = False
while len(ppap) < len(str) and finish_loof == False:
    for i in range(len(ppap)):
        if ppap[i] != str[i]:
            if ppap[i] == 'A' and i != 0:
                ppap = ppap[: i - 1] + "PPAP" + ppap[i:]
                print(ppap)
                break
                
        if i + 1 == len(ppap):
            finish_loof = True
            
if ppap == str:
    print("PPAP")
else:
    print("NP")