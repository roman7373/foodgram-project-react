from django.core.exceptions import ValidationError

def validate_time(value):
    if value <= 0:
        raise ValidationError("Некорректное время приготовления!")
    return value


def validate_amount(value):
    if value <= 0:
        raise ValidationError("Некорректное кол-во ингредиентов!")
    return value
