from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep Boop"

def main_section_3():
    print(" Polymorphism ")

    animals = [Dog(), Cat()]
    for animal in animals:
        print(f" {type(animal).__name__} says: {animal.speak()}")

    mixed_list = [Dog(), Cat(), Robot(), "Just a String"]
    
    for item in mixed_list:
        if isinstance(item, Animal):
            print(f" Valid Animal ({type(item).__name__}): {item.speak()}")
        else:
            print(f" Ignored Invalid Item ({type(item).__name__}): Not an Animal!")


if __name__ == "__main__":
    main_section_3()
