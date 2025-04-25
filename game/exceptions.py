class InvalidInputError(Exception):
    """Ошибка при некорректном вводе в меню или настройках."""
    pass

class InvalidRollError(Exception):
    """Ошибка при неверной попытке броска кубика."""
    pass