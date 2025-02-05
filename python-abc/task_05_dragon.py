#!/usr/bin/python3
"""
This is the ``task_05_dragon`` module
"""


class SwimMixin:
    """
    This is the ``SwimMixin`` class
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    This is the ``FlyMixin`` class
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    This is the ``Dragon`` subclass
    """

    def roar(self):
        print("The dragon roars!")
