from abc import ABC, abstractmethod


class BaseItem:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def __str__(self):
        return f"Объект {self.__class__.__name__}, имя объекта {self.name}, цена {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not self.is_valid_price(value):
            raise ValueError("Значение цены должно быть положительным числом")
        self._price = value

    @abstractmethod
    def prepare(self):
        pass

    @staticmethod
    def is_valid_price(value):
        return isinstance(value, (int, float)) and value > 0

    @classmethod
    def from_string(cls, data_str):
        name_elem, price_elem = data_str.split(",")
        return cls(name_elem, float(price_elem))


class Drink(BaseItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def prepare(self):
        return f"Готовим напиток {self.name}"


class Food(BaseItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def prepare(self):
        return f"Готовим блюдо {self.name}"


class Menu:
    def __init__(self):
        self.menu_list = []

    def add_item(self, item):
        if isinstance(item, BaseItem):
            self.menu_list.append(item)
        return f"Объект успешно добавлен"

    def add_more_items(self, *items):
        for item in items:
            self.menu_list.append(item)
        return f"Объекты успешно добавлены"

    def get_item_by_name(self, name):
        result = [item for item in self.menu_list if item.name == name]
        if not result:
            raise ValueError("Такого объекта нет в списке")
        return result[0]

    def update_item_price(self, name, price):
        result = self.get_item_by_name(name)
        result.price = price
        return f"Цена объекта успешно изменена"

    def delete_item(self, name):
        result = self.get_item_by_name(name)
        self.menu_list.remove(result)
        return f"Объект успешно удален"

    def __str__(self):
        return "\n".join(str(item) for item in self.menu_list)


class Order:
    def __init__(self):
        self.items = []

    def add_to_order(self, item):
        if not isinstance(item, (Drink, Food)):
            raise ValueError(f"Передан не правильный объект")
        self.items.append(item)

    def add_more_to_order(self, *items):
        for elem in items:
            if not isinstance(elem, BaseItem) or len(items) == 0:
                raise ValueError("Список пуст или содержит не допустимые объекты")
            self.items.append(elem)
        return "Объекты успешно добавлены"

    def total(self):
        result = sum(item.price for item in self.items)
        return f"Сумма объектов составляет - {result}"

    def summary(self):
        result = [item.prepare() for item in self.items]
        total = sum(item.price for item in self.items)
        result.append(f"Итого: {total} rub")
        return "\n".join(result)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)


drink1 = Drink("Kola", 85)
drink2 = Drink("Fanta", 90)
# drink2.price = 200
# print(drink2.price)
food1 = Food("Борщ", 125)
food2 = Food("Стейк", 1200)
print(Food.is_valid_price(food1.price))
# print(drink1.prepare())
# print(food1.prepare())
menu1 = Menu()
# menu1.add_item(drink1)
# menu1.add_item(food1)
# print(menu1)
# print("---------")
# menu1.add_more_items(drink2, food2)
# print(menu1)
lst = [drink1, drink2, food1]
menu1.add_more_items(*lst)
# print(menu1)
# print(menu1.get_item_by_name("Борщ"))
order1 = Order()
# order1.add_to_order(menu1.get_item_by_name("Fanta"))
# order1.add_to_order(menu1.get_item_by_name("Kola"))
# order1.add_to_order(menu1.get_item_by_name("Борщ"))
# print(order1)
# print(order1.total())
# print(order1.summary())
# lst = [food1, drink1]
# order1.add_more_to_order(*lst)
# # print(order1)
# food3 = Food.from_string("123, 45")
# print(food3)
menu1.update_item_price("Борщ", 225)
print(menu1)
menu1.delete_item("Борщ")
print("---")
print(menu1)
