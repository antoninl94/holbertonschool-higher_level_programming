#!/usr/bin/python3
"""
This is the ``task_00_abc`` module
"""
from abc import *


class Animal(ABC):
    """
    This is the ``Animal`` class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    This is the ``Dog`` subclass
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    This is the ``Cat`` subclass
    """
    def sound(self):
        return "Meow"
