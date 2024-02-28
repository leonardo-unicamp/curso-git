from time import sleep


def zzz():
    sleep(5)


def greet():
    print("Hello!")


def compute():
    return 42


def main() -> None:
    zzz()
    greet()
    compute()


if __name__ == "__main__":
    main()
