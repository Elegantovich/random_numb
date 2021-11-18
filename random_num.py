import random


def randon_numb_tuple(*args):
    """Определяем случайное число из поступающего кортежа."""
    list_numb = list(args)
    print(random.choice(list_numb))


def randon_numb(a, b):
    """Определяем целое случайное число из пространства [a, b]."""
    numb = random.randint(a, b)
    print(numb)


def main():
    randon_numb(0, 1000)
    randon_numb_tuple(0, 17, 432)


if __name__ == '__main__':
    main()