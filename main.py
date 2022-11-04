from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import BaseError

store: Store = Store(
    items={
        'картошка': 10,
        'печенька': 10,
    },
    capacity=100,
)
shop = Shop(
    items={
        'печенька': 5,
    },
    capacity=20,
    max_unique_items=5,
)

storages: Dict[str, AbstractStorage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    print('Добрый день!\n')

    while True:
        for storage_name, storage in storages.items():
            print(f"В {storage_name} хранится:\n{storage.get_items()}")

        raw_request: str = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "stop" или "стоп", чтобы закончить:'
        )
        if raw_request in ('stop', 'стоп'):
            break
        try:
            request = Request(request=raw_request, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except BaseError as error:
            print(error.message)

if __name__ == '__main__':
    main()
