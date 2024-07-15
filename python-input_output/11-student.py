#!/usr/bin/python3
"""simple module documentation"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with the provided first name, last name,
        and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return self.__dict__
        return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with those in
        the provided json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
