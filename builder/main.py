from builder.Builder import JeepBuilder, SedanBuilder, Director


def main():
    director = Director()
    director.setBuilder(SedanBuilder())
    car = director.getCar()
    car.specification()


if __name__ == '__main__':
    main()
