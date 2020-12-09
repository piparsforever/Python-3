def over_nine_thousand(lst):
    x = 0
    for i in lst:
        if x <= 9000:
            x += i
    return x


print(over_nine_thousand([8000, 900, 120, 5000]))


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


def over_nine_thousand(lst):
    lst_sum = 0
    for i in lst:
        if lst_sum < 9000:
            lst_sum += i
    return lst_sum


print(over_nine_thousand([8000, 900, 120, 5000, 6000]))


####################################################################
# Mana versija
def over_nine_thousand(lst):
    x = 0
    index = 0
    for i in lst:
        while x < 90000:
            x = i + i
            index += 1
        return x


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
