class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print(f"Нельзя сменить цвет на ({r}, {g}, {b})")

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            print("Некорректные стороны, изменение не применено")

    def __is_valid_sides(self, *sides):
        return (len(sides) == self.sides_count and
                all(isinstance(x, int) and x > 0 for x in sides))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

import math

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__radius = self.__calculate_radius()

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        # Реализация вычисления высоты треугольника (например, через формулу Герона)
        s = len(self) / 2  # Полупериметр
        a, b, c = self.get_sides()
        return (2 / a) * (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_square(self):
        a, _, _ = self.get_sides()
        return 0.5 * a * self.__height

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__height = self.__calculate_height()

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1] * self.sides_count
        super().__init__(color, *([sides[0]] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

    def set_sides(self, *sides):
        if len(sides) == 1:
            super().set_sides(*([sides[0]] * self.sides_count))
        else:
            print("Некорректные стороны, изменение не применено")

# Тестирование
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (длины окружности):
print(len(circle1))

# Проверка объема куба:
print(cube1.get_volume())
