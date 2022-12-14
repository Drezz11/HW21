class BaseError(Exception):
    message = 'Что-то пошло не так'


class NotEnoughSpaceError(BaseError):
    message = 'Не достаточно места'


class NotEnoughProductError(BaseError):
    message = 'Не достаточно товара'


class TooManyDifferentProductError(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'

class UnknownStorageError(BaseError):
    message = 'Неизвестный склад'
