# abstract shape classes
class Shape2DInterface:
    def draw(self):
        pass


class Shape3DInterface:
    def draw(self):
        pass


# Concrete shape classes
class Circle(Shape2DInterface):
    def draw(self):
        print('Circle.draw')


class Square(Shape2DInterface):
    def draw(self):
        print('Square.draw')


class Sphere(Shape3DInterface):
    def build(self):
        print('Sphere.build')


class Cube(Shape3DInterface):
    def build(self):
        print('Cube.build')


class ShapeFactory:
    @staticmethod
    def getShape(type):
        try:
            if type == 'circle':
                return Circle()
            elif type == 'square':
                return Square()
        except RuntimeError:
            print('shape not found')


# Abstract shape factory
class ShapeFactoryInterface:
    def getShape(sides):
        pass


class ShapeFactory2D(ShapeFactoryInterface):
    def getShape(sides):
        if sides == 1:
            return Circle()
        elif sides == 4:
            return Square()


class ShapeFactory3D(ShapeFactoryInterface):
    def getShape(sides):
        if sides == 1:
            return Sphere()
        elif sides == 6:
            return Cube()
