#!/usr/bin/python3
"""
This is the ``task_02_verboselist`` module
"""
class VerboseList(list):
    """
    This is the ``VerboseList`` subclass
    """

    def append(self, int):
        """
        This function append int to a list
        """
        print(f"Added [{int}] to the list.")
        super().append(int)

    def extend(self, int):
        """
        This function extend the list
        """
        print(f"Extended the list with [{len(int)}] items.")
        super().extend(int)
    
    def remove(self, int):
        """
        This function remove a number equal to int
        """
        if int not in self:
            raise ValueError
        print(f"Removed [{int}] from the list.")
        super().remove(int)

    def pop(self, int=-1):
        """
        This function remove the number at the index
        """
        if self[int] == None:
            raise IndexError
        print(f"Popped [{self[int]}] from the list.")
        ret = super().pop(int)
        return ret
