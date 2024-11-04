import random
from nat_module import Nat

nat_numbers = [Nat(random.randint(1, 100)) for _ in range(5)]

for nat_number in nat_numbers:
    nat_number.display_value()
    nat_number.display_divs()
    print()