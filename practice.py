import math
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

    def __eq__(self, other):
        if other is None or not isinstance(other, Figure):
            return False
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __str__(self):
        return f"Фигура: {self.name}, цвет фигуры: {self.color}"

    def __repr__(self):
        return self.__str__()


class Circle(Figure):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius**2

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if (radius <= 0) or not isinstance(radius, (int, float)):
            raise ValueError(f"Значение радиуса должно быть целым положительным цислом")
        self.__radius = radius

    @staticmethod
    def is_valid_radius(radius):
        if not isinstance(radius, (int, float)):
            raise ValueError("Радиус должен быть числом")
        return radius > 0

    @classmethod
    def from_diameter(cls, name, color, diametr):
        return cls(name, color, diametr / 2)


class Rectangle(Figure):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class FigureManager:
    def __init__(self):
        self.list_figures = []

    def add_figures(self, *args):
        for obj in args:
            if not isinstance(obj, Figure):
                raise AttributeError("Передан неправильный объект")
            self.list_figures.append(obj)

    def get_figure_by_name(self, name):
        if not isinstance(name, str):
            raise AttributeError(f"Имя должно быть строкой")
        for elem in self.list_figures:
            if elem.name == name:
                return elem
        return f"Объекта с таким именем нет в списке, или список пуст"

    def get_figures_by_color(self, color):
        result = [element for element in self.list_figures if element.color == color]
        if not result:
            raise ValueError(f"Фигура с цветом - {color} не найдена")
        return result

    def get_largest_figure(self):
        result = max(self.list_figures, key=lambda element: element.get_area())
        return result.get_area()

    @staticmethod
    def sorted_figures_by_area(*args):
        return sorted(args, key=lambda figure: figure.get_area())

    @classmethod
    def from_figure_list(cls, *figures):
        manager = cls()
        manager.add_figures(*figures)
        return manager

    def remove_figure_by_name(self, name):

        if not isinstance(name, str):
            raise AttributeError(f"Имя должно быть строкой")
        figure_to_remove = self.get_figure_by_name(name)
        if isinstance(figure_to_remove, Figure):
            self.list_figures.remove(figure_to_remove)
            return "Объект удален из списка"
        return "Объекта с таким именем нет в списке, или список пуст"

    def update_figure_color(self, name, new_color):
        if not isinstance(name, str) or not isinstance(new_color, str):
            raise AttributeError("Имя и цвет должны быть строками")
        figure_to_update = self.get_figure_by_name(name)
        if isinstance(figure_to_update, Figure):
            setattr(figure_to_update, "color", new_color)
            return "Цвет фигуры обновлен"
        return "Фигура не найдена"

    def get_total_area(self):
        return sum(figure.get_area() for figure in self.list_figures)

    def clear_all(self):
        self.list_figures.clear()

    def __str__(self):
        return "\n".join(str(element) for element in self.list_figures)

    def __repr__(self):
        return self.__str__()


circle = Circle("Круг", "Синий", 5)
circle2 = Circle("Круг", "Желтный", 11)
circle3 = Circle("Круг", "Желтный", 2)
circle4 = Circle("Круг", "Желтный", 1)
# print(circle.get_area())
# circle.radius = 10
# print(circle.radius)
# print(circle.get_area())
manager = FigureManager()
manager.add_figures(circle, circle2)
# print(manager)
# print("----")
# print(manager.get_figure_by_name("Квадрат"))
# print(manager.get_figure_by_name("Oval"))
# print(manager.remove_figure_by_name("Круг"))
# print("-------")
# print(manager)
# print(manager.update_figure_color("Квадрат", "Blue"))
# print(manager)
# print(manager.get_total_area())
# print(circle < circle2)
# print(manager.get_figures_by_color("Синий"))
# print(manager.get_largest_figure())
# print(circle2.is_valid_radius(1))
# print(manager.sorted_figures_by_area(circle4, circle, circle2, circle3))
circle_from_diametr = Circle.from_diameter("Круг", "Фиолетовый", 20)
print(circle_from_diametr.radius)
