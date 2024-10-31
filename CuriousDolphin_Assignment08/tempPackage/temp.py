# Name: Group CuriousDolphin (Quynh Doan, Denise Huynh, Andrew Mehlman)
# email: doanqb@mail.uc.edu, mehlmadm@mail.uc.edu, huynhd2@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 10/31/2024
# Course #/Section: IS 4010-001
# Semester/Year: Fall Semester 2024
# Brief Description of the assignment: In this sagacious assignment you will collaborate with peers to develop a VS project modeling something in the real world. Pick a thing in the world of your assigned group that has meaning to all group members. 
# Brief Description of what this module does: This module defines the Temperature class, which models a temperature control system. The class allows for initializing a temperature, retrieving its value, and increasing it by a specified amount. It restricts direct lowering of the temperature and provides warnings when attempted. Additionally, the class includes formatted string representations to display the temperature in a user-friendly format.
# Citations: N/A
# Anything else that's relevant: N/A

#temp.py
class Temperature:
    def __init__(self, temp):
        self._temperature = temp

    def __str__(self):
        """
        Returns a human-readable representation of the temperature.
        """
        return f"Temperature: {self.get_temp()} F"

    def __repr__(self):
        """
        Returns an official string representation of the Temperature object.
        """
        return f"Temperature({self.get_temp()} F)"

    def get_temp(self):
        """
        Returns the current temperature.
        """
        return self._temperature

    def set_temp(self, new_temp):
        """
        Sets the temperature, preventing it from decreasing.
        :param new_temp: int, the new temperature to set.
        """
        if new_temp < self._temperature:
            print("The temperature cannot decrease. It's getting warmer!")
        self._temperature = new_temp

    def get_warm(self, increase):
        """
        Increases the temperature by a specified amount.
        :param increase: int, the amount to increase the temperature by.
        """
        self._temperature += increase
        print(f"The temperature is getting warmer: {self._temperature} F")
