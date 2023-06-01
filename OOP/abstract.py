# """
# Абстракция
# """
# # # Абстракция (Абстрактный класс) - принцип ООП, в котором создается абстрактный класс (класс - пустышка), то есть в котором задаются названия аттрибутов и методов, для того чтобы в дочерних классах переопределить их нужным образом. (у нас есть название, но нет логики).

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):
#     @abstractmethod
#     def voice(self):
#         pass

#     @abstractproperty
#     def legs(self):
#         pass

# #     # @abstractmethod - декоратор, который требует переопределение метода в наследуемом классе
# #     # @abstractproperty - декоратор, который требует переопределение аттрибутов класса

# # obj = AbstractAnimal() #TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# class Dog(ConnectionAbortedError):
#     pass

# obj = Dog() # Error

# class Dog(AbstractAnimal):
#     def voice(self):
#         print('гав-гав')

# # obj = Dog() #TypeError: Can't instantiate abstract class Dog with abstract method legs

# class Dog(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('гав-гав')

# obj = Dog()
# obj.voice()
# print(obj.legs)

# class Cat(ABC):
#     legs = 4
#     def voice(self):
#         print('meow')

# dog = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length ** 2

# obj = Square(12)
# print(obj.name)
# print(obj.area())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from abc import ABC, abstractmethod, abstractproperty

class AbstractBird(ABC):
    def __init__(self, name) -> None:
       self.name = name

    @abstractmethod
    def fly(self):
      pass

    @abstractmethod
    def grow(self):
      pass

    @abstractmethod
    def sound(self):
      pass

class Bird(AbstractBird):
  def __init__(self) -> None:
     super().__init__('Птица:')

  def fly(self):
    print('летает')

  def grow(self):
    print('растёт')

  def sound(self):
    print('поёт')

obj = Bird()
print(obj.name)
obj.fly()
obj.sound()
obj.grow()
print()

class AbstractAnimal(ABC):
    def __init__(self, name) -> None:
       self.name = name
       
    @abstractmethod
    def run(self):
      pass

    @abstractmethod
    def grow(self):
      pass

    @abstractmethod
    def sound(self):
      pass

class Dog(AbstractAnimal):
    def __init__(self) -> None:
       super().__init__('Rex:')

    def run(self):
        print('бежит')

    def grow(self):
        print('растёт')

    def sound(self):
        print('гав-гав')

obj2 = Dog()
print(obj2.name)
obj2.run()
obj2.grow()
obj2.sound()
print()
      
class AbstractPlant(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def grow(self):
        pass

    @abstractmethod
    def photosynthesize():
       pass

class Plant(AbstractPlant):
    def __init__(self) -> None:
       super().__init__('Растение:')

    def grow(self):
       print('растёт')

    def photosynthesize(self):
       print('процесс фотосинтеза')

obj3 = Plant()
print(obj3.name)
obj3.grow()
obj3.photosynthesize()

       

