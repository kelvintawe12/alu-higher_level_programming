#!/usr/bin/python3
"""
Module: 9-student

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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__
