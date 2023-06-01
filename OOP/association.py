# Ассоциация - принцип ООП, в котором два класса связаны друг с другом. Связь обозначает то что внутри одного объекта будет существовать другой объект от другого класса
# агрегации - слабая связь
# композиция - сильная связь

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         #когда мы создаем внутри класса объект от другого класса - композиция

# a = Iphone('grey')
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a

# class Nokia:
#     def __init__(self, battery: Battery, color: str) -> None:
#         self.color = color
#         self.battery = battery
#         # когда объект создается из вне класса и передается внутр - агрегация

# battery = Battery()
# nokia1 = Nokia(battery, 'gray')
# print(nokia1.battery._power)
# del nokia1

# nokia2 = Nokia(battery, 'black')
# # при удалении объекта Nokia, батарейка остается

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Композиция

# class Wall:
#     def __init__(self, direction) -> None:
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type}'
    
# class Room:
#     def __init__(self) -> None:
#         self.west_wall = Wall('West')
#         self.east_wall = Wall('East')
#         self.south_wall = Wall('South')
#         self.north_wall = Wall('North')

# obj = Room()
# print(obj.west_wall)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Агрегация
# class Stream:
#     def __str__(self) -> str:
#         return 'Stream object'
    
# class Logger:
#     def __init__(self, stream=None) -> None:
#         self.stream = stream

#     def print_the_logs(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream')

# stream1 = Stream()
# Logger1 = Logger(stream1)
# Logger2 = Logger(stream1)
# Logger3 = Logger(stream=Stream())
# Logger1.print_the_logs()
# Logger2.print_the_logs()
# Logger3.print_the_logs()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Engine:
#     country = 'Germany'

#     def __init__(self, power) -> None:
#         self.power = power

#     def __str__(self) -> str:
#         return f'Power: {self.power}'
    
# class AudiCar:
#     brand = 'Audi'
#     country = 'Germany'

#     def __init__(self, model, power) -> None:
#         self.engine = Engine(power)
#         self.model = model

#     def __str__(self) -> str:
#         return f'{self.brand} {self.model} -> Engine: {self.engine} -> engine country: {self.engine.country}'
    
# car = AudiCar('A8', 400)
# print(car)

