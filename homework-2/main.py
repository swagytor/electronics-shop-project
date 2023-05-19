from src.item import Item
from pathlib import Path

PATH_TO_SRC = f'{Path(__file__).parent.parent}/src'
PATH_TO_CSV = f'{PATH_TO_SRC}/items.csv'


if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv(PATH_TO_CSV)  # создание объектов из данных файла

    assert len(Item.all) == 6  # в файле 6 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('ываыа') == 'Строка не является числом!'
    assert Item.string_to_number('5.5.7') == 'Строка не является числом!'
