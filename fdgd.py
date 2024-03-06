s = 0
c = 0
x = ''
for i in range(0,17):
    x = input("на чьей стороне ты? ")
    if x == "конфеты":
        s += 1
    if x == "цветы":
        c += 1
print(c)
print(s)
if s >= c:
    print("конфет больше")
else:
    print("цветов больше")

    
