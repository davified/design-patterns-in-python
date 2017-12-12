from abstract_factory import ShapeFactory2D, ShapeFactory3D

def main():
    circle = ShapeFactory2D.getShape(1)
    square = ShapeFactory2D.getShape(4)

    sphere = ShapeFactory3D.getShape(1)
    cube = ShapeFactory3D.getShape(6)

    circle.draw()
    square.draw()
    sphere.build()
    cube.build()


if __name__ == '__main__':
    main()
