class Employee:
    def __init__(self) -> None:
        self.employee_name: str
        self.employee_number: int

class ProductionWorker(Employee):
    def __init__(self) -> None:
        super().__init__()
        self.hourly_pay_rate: float
        self.shift_number: int # valid values: 1 or 2
    
    def set_shift_number(self):
        # set it
        pass
    
    def set_hourly_pay_rate(self):
        # set it
        pass

    def get_shift_number(self) -> int:
        # get it
        pass
    
    def get_hourly_pay_rate(self) -> float:
        # get it
        pass

prd_wrkr = ProductionWorker()
# set the hourly rate
# set the shift number
# print the hourly rate
# print the shift number
