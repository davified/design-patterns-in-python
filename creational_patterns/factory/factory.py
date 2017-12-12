class ShapeInterface:
    def draw(self):
        pass


class Circle(ShapeInterface):
    def draw(self):
        print('Circle.draw')


class Square(ShapeInterface):
    def draw(self):
        print('Square.draw')


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

