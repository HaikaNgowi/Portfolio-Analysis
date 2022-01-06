#Importing multiple classes from a module
from nine2 import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


#Importing an entire module
import nine2

my_beetle = nine2.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = nine2.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

from nine2 import *


