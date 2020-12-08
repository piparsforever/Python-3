weight = float(input("Enter the package weight in lb: "))


premium_g = 125.00


def ground_shipping():
    if weight <= 2:
        return 1.50
    elif weight >= 2 and weight <= 6:
        return 3.00
    elif weight > 6 and weight <= 10:
        return 4.00
    else:
        return 4.75


def ground_shipping_price():
    cost = (weight * ground_shipping()) + 20
    return cost


def drone_shipping():
    if weight <= 2:
        return 4.50
    elif weight >= 2 and weight <= 6:
        return 9.00
    elif weight > 6 and weight <= 10:
        return 12.00
    else:
        return 14.25


def drone_shipping_price():
    cost = weight * drone_shipping()
    return cost


def cheapest_shipping_method():
    a = ground_shipping_price()
    b = drone_shipping_price()
    c = premium_g
    if a < b < c:
        return "Ground Shipping and it will cost $" + format(ground_shipping_price(), '.2f')
    elif b < a < c:
        return "Drone Shipping and it will cost $" + format(drone_shipping_price(), '.2f')
    else:
        return "Premium Ground Shipping and it will cost $" + format(premium_g, '.2f')


print("The cheapest shipping method will be " + str(cheapest_shipping_method()))
