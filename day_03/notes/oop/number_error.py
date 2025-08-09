class NotANumberError(ValueError):
    pass

class NotPositiveNumber(ValueError):
    pass

class NotWithinRangeNumber(ValueError):
    pass

user_input = input("Enter a number from [1-100]: ")

is_numeric = user_input.replace('.','').isnumeric()
is_numeric_sign = user_input[1:].replace('.','').isnumeric()

"""
print(f"{is_numeric} ^ {is_numeric_sign}")
"""

if not is_numeric and not is_numeric_sign:
    raise NotANumberError("Input is not a number")

"""
if not user_input.isnumeric() and not user_input[1:].isnumeric():
    raise NotANumberError("Input is not a number")
"""

if '.' in user_input:
    number = float(user_input)
else:
    number = int(user_input)

if number < 0:
    raise NotPositiveNumber("Input is not a positive number")

if not (0 <= number <= 100):
    raise NotWithinRangeNumber("Number is not in range[1-100]")
