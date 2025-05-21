import math
from turtle import width


class Figure:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_area(self):
        pass

    def __str__(self):
        return f"Фигура: {self.name}, цвет фигуры: {self.color}"


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
        if not isinstance(figure, Figure):
            raise AttributeError(f"Передан неправильный объект")
        for obj in args:
            self.list_figures.append(obj)

    def get_figure_by_name(self, name):
        if not isinstance(name, str):
            raise AttributeError(f"Имя должно быть строкой")
        for elem in self.list_figures:
            if elem.name == name:
                return elem
        return f"Объекта с таким именем нет в списке, или список пуст"

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


figure = Figure("Квадрат", "Зеленый")
circle = Circle("Круг", "Желтный", 5)
circle2 = Circle("Круг", "Желтный", 11)
# print(circle.get_area())
circle.radius = 10
print(circle.radius)
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
print(manager.update_figure_color("Квадрат", "Blue"))
print(manager)
print(manager.get_total_area())
