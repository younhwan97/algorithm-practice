value = input()
   
## PPPAPAP => P (PPAP) AP

while len(value) > len("PPAP"):
    index = value.find("PPAP")

    if index >= 0:
        value = value.replace("PPAP", "P")
    else:
        break

if value == "PPAP":
    print("PPAP")
else:
    print("NP")