from django.core.exceptions import ValidationError


def validate_value(value):
    if value <= 0:
        raise ValidationError("Некорректное значение!")
    return value
