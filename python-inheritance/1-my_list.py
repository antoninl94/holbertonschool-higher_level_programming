#!/usr/bin/python3
"""
This is the ''1-my_list'' module
"""


class MyList(list):
    """
    This is the subclass ''MyList'' that inherits from
    the baseclass ''list''
    """

    def print_sorted(self):
        """
        This function print the list sorted
        """
        if not isinstance(self, list):
            raise Exception
        else:
            print(sorted(self))
