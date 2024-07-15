#!/usr/bin/python3
"""
Module: 10-student

This module defines a class Student.
"""


class Student:
    """
    Defines a student by:
    - first_name
    - last_name
    - age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary containing the specified attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
