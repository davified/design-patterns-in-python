class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d" % self.__wheels[0].size)


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        for i in range(4):
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)

        return car


class AbstractBuilder:
    def getWheel(self): pass

    def getEngine(self): pass

    def getBody(self): pass


class JeepBuilder(AbstractBuilder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = 'Jeep'
        return body


class SedanBuilder(AbstractBuilder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 10
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 300
        return engine

    def getBody(self):
        body = Body()
        body.shape = 'Sedan'
        return body
