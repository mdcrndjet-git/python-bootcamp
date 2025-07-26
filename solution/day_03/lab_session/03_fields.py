import json
from abc import ABC, abstractmethod
from collections import UserList


class Field(ABC):
    def __init__(self, label, value=None, required=False):
        self.label = label
        self.value = value
        self.required = required

    @abstractmethod
    def validate(self):
        raise NotImplementedError()

    def is_valid(self):
        if self.required and (self.value is None or str(self.value).strip() == ""):
            return False
        return self.validate()

    def __repr__(self):
        return f"{self.__class__.__name__}(label={self.label}, value={self.value})"


class Email(Field):
    ACCEPTED_ADDRESSES = ("@gmail.com", "@outlook.com")

    def validate(self):
        return isinstance(self.value, str) and any(self.value.endswith(address) for address in Email.ACCEPTED_ADDRESSES)


class IntegerField(Field):
    def validate(self):
        return isinstance(self.value, int) or (str(self.value).isdigit())


class FloatField(Field):
    def validate(self):
        try:
            float(self.value)
            return True
        except (ValueError, TypeError):
            return False


class TextField(Field):
    CHAR_LIMIT = 100

    @property
    def length(self):
        return len(str(self.value))

    def validate(self):
        return isinstance(self.value, str) and self.length <= self.CHAR_LIMIT


class BooleanField(Field):
    BOOL_MAP = {
        'true': True, 'yes': True,
        'false': False, 'no': False,
        True: True, False: False
    }

    def __bool__(self):
        try:
            return self.BOOL_MAP[self.value]
        except KeyError:
            raise ValueError(f"Invalid boolean string: {self.value}")

    def validate(self):
        return self.value in self.BOOL_MAP


class Form(UserList):
    def validate(self):
        return all(field.is_valid() for field in self.data)

    def get_errors(self):
        return [field.label for field in self.data if not field.is_valid()]

    def as_dict(self):
        return {
            field.label: {
                "value": field.value,
                "required": field.required
            }
            for field in self.data
        }

    def save(self, filepath):
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.as_dict(), f, indent=2)
            print(f"Form saved to {filepath}")
        except Exception as e:
            print(f"Failed to save form: {e}")

    def __repr__(self):
        return f"Form(fields={list(self.data)})"
