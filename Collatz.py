def collatz(num):
    print(num)
    if num <= 1:
        pass
    elif num % 2 == 0:
        collatz(num // 2)
    else:
        collatz(num * 3 + 1)


def main():
    num = 0
    try:
        num = int(input('Enter a number: '))
        collatz(num)
    except ValueError:
        print('You have to enter an integer.')

if __name__ == '__main__':
    main()