import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = float(price)
        self.quantity = int(quantity)
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            print('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path='items.csv'):
        with open(path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            [Item(**row) for row in reader]

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
        except:
            return 'Строка не является числом!'