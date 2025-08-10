import hello_v4
import hello_v4 as hi

# specific import: functions, variables
# import can also add alias
from hello_v4 import say_goodbye as geh_bye
from hello_v4 import var1, var2

hi.say_hello()

# hi can be skipped
geh_bye()

print(var1,var2)