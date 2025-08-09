class InvalidChoiceError(ValueError):
    pass

choices = ("rock","paper","scissors")
user_input = input("Enter choice:")

if user_input not in choices:
    raise InvalidChoiceError("")