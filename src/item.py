import csv
import os.path

from pathlib import Path
from src.exceptions import InstantiateCSVError

PATH_TO_SRC = f'{Path(__file__).parent.parent}/src'
PATH_TO_CSV = f'{PATH_TO_SRC}/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = int(price)
        self.quantity = int(quantity)
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join([repr(attr) for attr in self.__dict__.values()])})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path=PATH_TO_CSV):
        if os.path.exists(path):
            cls.all.clear()
            with open(path, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                if len(reader.fieldnames) != 3:
                    raise InstantiateCSVError('Файл item.csv поврежден')
                [Item(**row) for row in reader]
        else:
            raise FileNotFoundError("Отсутствует файл item.csv")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = round(self.price * Item.pay_rate, 2)

    @staticmethod
    def string_to_number(number):
        try:
            if number.count('.') == 1:
                number = float(number)
            return int(number)
        except ValueError:
            return 'Строка не является числом!'
