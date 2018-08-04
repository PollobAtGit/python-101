from fib import i_will_not_be_imported

# packages are defined by automatic directory hierarchy
from sound.echo.symphony import *

print(i_will_not_be_imported())
print(__name__)

# print(fib(10))

print(dir())
print(dir(i_will_not_be_imported))

print(definition_from_symphony(10))
print(sound.echo.symphony.definition_from_other_sys())
