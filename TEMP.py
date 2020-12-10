def over_nine_thousand(lst):
    x = 0
    for i in lst:
        if x == 9000:
            x += i
        elif x < 9000:
            x += i
    return x


print(over_nine_thousand([8000, 900, 120, 5000, 6000]))


def over_nine_thousand(lst):
    x = []
    for i in lst:
        x.append(i)
        if sum(x) >= 9000:
            return sum(x)
        elif sum(lst) < 9000:
            return sum(lst)
        elif len(lst) == 0:
            return 0


print(over_nine_thousand([8000, 900, 120, 5000, 6000]))


x = open("Txt_temp.rtf", "r")
count = 0
for i in x:
    count += 1
print("Line count =", count)
