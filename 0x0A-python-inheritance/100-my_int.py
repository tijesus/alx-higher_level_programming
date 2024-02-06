#!/usr/bin/python3
"""class that inherit int"""


class MyInt(int):
    """class that rebel"""
    def __eq__(self, value):
        """return the inbuilt result fot not equal to behaviour"""
        return super().__ne__(value)

    def __ne__(self, value):
        """return the inbuilt result fot equal to behaviour"""
        return super().__eq__(value)
