def main(lst):
    n = lst[0]
    for i in lst:
        if i < n:
            n = i
        print(n, i)


if __name__ == "__main__":
    main([8, 44, 3, 7, 90, 2, 0, -2, -50, 0])
