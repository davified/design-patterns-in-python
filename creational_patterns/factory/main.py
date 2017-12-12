from factory import ShapeFactory


def main():
    circle = ShapeFactory.getShape('circle')
    circle.draw()


if __name__ == '__main__':
    main()
