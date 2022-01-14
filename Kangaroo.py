x1 = 6
v1 = 2
x2 = 4
v2 = 2


def kangaroo(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2: return "YES"
    if x1 == x2 and v1 != v2: return "NO"
    if x1 != x2 and v1 == v2: return "NO"
    if x1 > x2 and v1 > v2: return "NO"
    if x2 > x1 and v2 > v1: return "NO"    
    
    if ((v1 < v2) or ((x2 - x1) % (v1 - v2) != 0)):
        return 'NO'
    else:
        return 'YES'


print(kangaroo(x1, v1, x2, v2))

while x1 != x2:
    x1 += v1
    x2 += v2
    if x1 >= 10000 or x2 >= 10000: break

print(x1, x2)
if x1 == x2 :
    print("YES")
else:
    print("NO")
