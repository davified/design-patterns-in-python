from prototype import SedanBuilder, JeepBuilder, Director


def main():
    director = Director()
    director.setBuilder(SedanBuilder())
    sedan = director.getCar()

    sedan_copy = sedan.clone()
    sedan_copy.specification()


if __name__ == '__main__':
    main()
