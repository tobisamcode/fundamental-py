from _typeshed import Self


class BMI:
    def __init__ (self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        KILOGRAMS_PER_POUND = 0.45359237
        METERS_PER_INCH = 0.0254

        bmi = self.__weight * KILOGRAMS_PER_POUND / ((self.__height * METERS_PER_INCH) ** 2)
        return round(bmi * 100) / 100

    def getStatus(self):
        bmi = self.getBMI