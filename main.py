from src.Work import Work


def main() -> None:
    work = Work()
    _sum = work.my_sum(23, 10.5)

    print(_sum)


if __name__ == '__main__':
    main()

