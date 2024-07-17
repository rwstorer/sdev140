class Person:
    def __init__(self) -> None:
        pass

class Customer(Person):
    def __init__(self,
                 customer_number: int,
                 wants_mail: bool = False) -> None:
        super().__init__()
        self.cust_num: int = customer_number
        self.wants_mail: bool = wants_mail

my_cust = Customer(1)

