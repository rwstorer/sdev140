class Car:
    def __init__(self, num_wheels:int=4):
        self.num_wheels: int = num_wheels
        self.steering: list = ['left','right']
        self.__is_moving: bool = False
    
    def go(self, direction='forward'):
        pass
    
    def is_moving(self) -> bool:
        self.__is_moving = not self.__is_moving
        return self.__is_moving


class eCar(Car):
    def __init__(self):
        super().__init__(self)
        self.__battery_level: int = 100
    
    def get_battery_level(self) -> int:
        return self.__battery_level
    
    def set_battery_level(self, battery_level: int):
        self.__battery_level = battery_level

e_car = eCar()
e_car.set_battery_level(50)
print(e_car.get_battery_level())
print(e_car.is_moving())