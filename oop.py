from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, mileage: int, fuel_level: int):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self._fuel_level = fuel_level

    @abstractmethod
    def drive(self):
        pass

    @property
    @abstractmethod
    def refuel(self):
        pass

    @refuel.setter
    @abstractmethod
    def refuel(self, amount):
        pass

    @staticmethod
    def is_valid_fuel_amount(amount):
        return isinstance(amount, int) and (1 < amount < 30)

    def __str__(self):
        return f"Объект {self.__class__.__name__}, марка - {self.brand}, модель - {self.model}, пробег {self.mileage} км, количество топлива {self._fuel_level} литров"


class Car(Vehicle):
    def __init__(self, brand: str, model: str, mileage: int, fuel_level: int):
        super().__init__(brand, model, mileage, fuel_level)

    @classmethod
    def with_default_mileage(cls, brand, model, fuel_level):
        return cls(brand=brand, model=model, mileage=0, fuel_level=fuel_level)

    def drive(self, distance):
        return f"Объект {self.__class__.__name__} проехал {distance} км "

    @property
    def refuel(self):
        return f"Количество бензина - {self._fuel_level}"

    @refuel.setter
    def refuel(self, amount):
        if not self.is_valid_fuel_amount(amount):
            raise ValueError(
                "Количество бензина должно быть целым положительным числом, не превышающим 30"
            )
        self._fuel_level = self._fuel_level + amount


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, mileage: int, fuel_level: int):
        super().__init__(brand, model, mileage, fuel_level)

    def drive(self, distance):
        return f"Объект {self.__class__.__name__} проехал {distance} км "

    @property
    def refuel(self):
        return f"Количество бензина - {self._fuel_level}"

    @refuel.setter
    def refuel(self, amount):
        if not self.is_valid_fuel_amount(amount):
            raise ValueError(
                "Количество бензина должно быть целым положительным числом,не превышающим 30"
            )
        self._fuel_level = self._fuel_level + amount


class Fleet:
    def __init__(self):
        self.vehicle_list = []

    def add_vehicle(self, car: Vehicle):
        if isinstance(car, Vehicle):
            self.vehicle_list.append(car)
        return f"Объект добавлен в список"

    def add_more_vehicle(self, *cars):
        for car in cars:
            if isinstance(car, Vehicle):
                self.vehicle_list.append(car)
        return f"Несколько объектов успешно добавлены в список"

    def search_vehicle(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Марка должна быть строкой")
        result = "".join(str(car) for car in self.vehicle_list if car.brand == brand)
        if not result:
            return f"Такого объекта нет в списке"
        return result

    def delete_vehicle(self, brand):
        if not isinstance(brand, str):
            raise ValueError("Марка должна быть строкой")
        delete_items = [car for car in self.vehicle_list if car.brand == brand]
        if not delete_items:
            return f"Такого объекта нет в списке"
        for car in delete_items:
            self.vehicle_list.remove(car)
        return f"Объект марки {brand} удален из списка"

    def update_mileage_vehicle(self, brand, mileage):
        if not isinstance(brand, str) or not isinstance(mileage, int):
            raise ValueError(
                "Марка автомобиля должна быть строкой или пробег в километрах"
            )
        for car in self.vehicle_list:
            if car.brand == brand:
                car.mileage = mileage
                return f"Пробег успешно изменён для автомобиля марки {brand}"
        return f"Объект с маркой {brand} не найден"

    def __str__(self):
        return "\n".join(str(car) for car in self.vehicle_list)

    def __repr__(self):
        return self.__str__()


car1 = Car("Toyota", "Camry 40", 25000, 30)
print(car1)
print(car1.drive(50))
print(car1.refuel)
car1.refuel = 25
print(car1.refuel)
motorcycle1 = Motorcycle("Yokohama", "GT-501", 12000, 35)
print(motorcycle1)
print(motorcycle1.drive(20))
print(motorcycle1.refuel)
fleet = Fleet()
fleet.add_vehicle(car1)
lst = [
    Car("Mazda", "Familia", 60000, 27),
    Motorcycle("Takeshi", "GS-503", 55000, 28),
    Car("KIA", "Optima", 22000, 18),
]
car4 = Car("Toyota", "Camry 40", 25000, 30)
test = Car.with_default_mileage("Test", "Test", 25)
fleet.add_more_vehicle(car4, motorcycle1, test)
fleet.add_more_vehicle(*lst)
print(fleet)
print("-----")
print(fleet.search_vehicle("Takeshi"))
print(fleet.delete_vehicle("1"))
print(fleet.update_mileage_vehicle("Toyota", 3500))
print(fleet)
