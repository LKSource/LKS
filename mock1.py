inputstring = "20"

num = int(inputstring)


def checkprime(num):
    if num in (1, 2, 3): return True
    if num % 2 == 0 or num % 3 == 0: return False
    return True


if num <= 0:
    print(-1)
else:
    lst = []
    for i in range(1, num + 1):
        if checkprime(i):
            lst.append(i)
    print(lst)
    rslt = ""
    for i in range(0, len(lst) - 1):
        if lst[i + 1] - lst[i] == 2:
            if rslt != "" : rslt += ","
            rslt += str(lst[i]) + ":" + str(lst[i + 1])
    if rslt == "":
        print(0)
    else:
        print(rslt)

lst = [1, 3, 5, 7]
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst1[::3])
print (lst[::3])
for i in lst[::3]:
    str = "Infosysoffice"
    print(str[i])
