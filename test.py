def main():
    a = is_even()
    for i in range(1, 11):
        if is_even(i): 				# this line failed last time
            print(" is even")
        else:
            print("is odd")


def is_even(x):
    return x % 2 == 0


if __name__ == "__main__":
    main()
