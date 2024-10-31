# Name: Group CuriousDolphin (Quynh Doan, Denise Huynh, Andrew Mehlman)
# email: doanqb@mail.uc.edu, mehlmadm@mail.uc.edu, huynhd2@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 10/31/2024
# Course #/Section: IS 4010-001
# Semester/Year: Fall Semester 2024
# Brief Description of the assignment: In this sagacious assignment you will collaborate with peers to develop a VS project modeling something in the real world. Pick a thing in the world of your assigned group that has meaning to all group members. 
# Brief Description of what this module does: This module defines a DigitalClock class that simulates a digital clock with alarm functionality. The class allows users to set and retrieve the current time, set an alarm time, and check if the current time matches the alarm, triggering an alert if they do. It also includes human-readable and official string representations to display the clock’s current time and alarm status.
# Citations: N/A
# Anything else that's relevant: N/A

#clock.py
class DigitalClock:
    """
    A Digital Clock that displays time and allows setting alarms.
    """
    def __init__(self, current_time="12:00 AM"):
        """
        Initializes the clock with the current time.
        :param current_time: str, the initial time displayed on the clock.
        """
        self._current_time = current_time
        self._alarm_time = None

    def get_current_time(self):
        """
        Returns the current time on the clock.
        """
        return self._current_time

    def set_current_time(self, time):
        """
        Sets the current time on the clock.
        :param time: str, the time to set on the clock.
        """
        self._current_time = time

    def get_alarm_time(self):
        """
        Returns the set alarm time.
        """
        return self._alarm_time

    def set_alarm_time(self, time):
        """
        Sets the alarm time.
        :param time: str, the alarm time to set.
        """
        self._alarm_time = time

    def set_alarm(self, time):
        """
        Sets an alarm for a specified time.
        :param time: str, the time to set the alarm.
        """
        self.set_alarm_time(time)
        print(f"Alarm set for {self._alarm_time}")

    def check_alarm(self):
        """
        Checks if the current time matches the alarm time and triggers the alarm.
        """
        if self._current_time == self._alarm_time:
            print("Alarm ringing!")
        else:
            print("No alarm set for now.")

    def __str__(self):
        """
        Returns a human-readable representation of the clock and its settings.
        """
        return f"DigitalClock: Current Time: {self.get_current_time()}, Alarm Time: {self.get_alarm_time() or 'No alarm set'}"

    def __repr__(self):
        """
        Returns an official string representation of the DigitalClock object.
        """
        return f"DigitalClock(current_time='{self.get_current_time()}')"


