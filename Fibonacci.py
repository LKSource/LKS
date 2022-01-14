var1 = 0
var2 = 1
value = 10
if value < 0:
    print("Enter positive value")
elif value == 1:
    print(0)
else:
    for i in range(1, value):
        var3 = var1 + var2
        var1 = var2
        var2 = var3
        print(var2)
