from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


@deconstructible
class MaxFileSizeValidator(BaseValidator):
    message = 'Ensure the file size is not greater than %(limit_value)s KB.'
    code = 'file_size'

    def __init__(self, max_size_kb):
        super().__init__(max_size_kb)
        self.limit_value = max_size_kb * 1024  # Convert KB to Bytes

    def compare(self, a, b):
        return a > b

    def __call__(self, value):
        if value.size > self.limit_value:
            params = {
                'limit_value': self.limit_value / 1024,
                'show_value': value.size / 1024,
                'value': value
            }
            raise ValidationError(
                self.message, code=self.code, params=params
            )