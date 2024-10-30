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

    def current_time(self):
        """
        Returns the current time on the clock.
        """
        return self._current_time

    def current_time(self, time):
        """
        Sets the current time on the clock.
        :param time: str, the time to set on the clock.
        """
        # Validation could be added here to ensure time format is correct
        self._current_time = time

    def alarm_time(self):
        """
        Returns the set alarm time.
        """
        return self._alarm_time

    def alarm_time(self, time):
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
        self.alarm_time = time
        print(f"Alarm set for {self.alarm_time}")

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
        return f"DigitalClock: Current Time: {self.current_time}, Alarm Time: {self.alarm_time or 'No alarm set'}"

    def __repr__(self):
        """
        Returns an official string representation of the DigitalClock object.
        """
        return f"DigitalClock(current_time='{self.current_time}')"

