import os


def main():
    while True:
        i = input("What's the word? ")
        if i != "bla":
            os.system('clear')
            continue
        if i == "bla":
            break
    print("Welcome!")


if __name__ == "__main__":
    main()
