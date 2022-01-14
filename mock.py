inputstring = "asdfgh#@,madz,asdf#@"
lst = inputstring.split(',')

print(lst)

d12 = {}
d3 = {}
dsi = {}

check = True

for c in lst[0]:
    if c not in d12 : d12[c] = 1
    else: d12[c] += 1
    
for c in lst[1]:
    if c not in d12 : d12[c] = 1
    else: d12[c] += 1
    
for c in lst[2]:
    if c not in d3 : d3[c] = 1
    else: d3[c] += 1

for k in d3.keys():
    if k in d12.keys():
        if d3[k] > d12[k]:
            check = False
            break
        
for k in d3.keys():
    if k not in d12.keys():
        check = False
        break

print(d12)
print(d3)
if check == True:
    for c in lst[2]:
        if c not in dsi.keys(): dsi[c] = 0

    for c in dsi.keys():
        for i in range(0, len(lst[0])):
            if c == lst[0][i]:
                if dsi[c] < i : dsi[c] = i
    
    for c in dsi.keys():
        for i in range(0, len(lst[1])):
            if c == lst[1][i]:
                if dsi[c] < i : dsi[c] = i
    
    ls = list(dsi.values())
    print(list(dsi.values()))
    
    for i in range(0, len(ls) - 1):
        if ls[i] > ls[i + 1]:
            check = False
            break
    
    if check == True:
        print("inside")
        print(1)
    else:
        print(0)    
else:
    print("here")
    print(0)
