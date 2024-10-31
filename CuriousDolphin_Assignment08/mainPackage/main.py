# Name: Group CuriousDolphin (Quynh Doan, Denise Huynh, Andrew Mehlman)
# email: doanqb@mail.uc.edu, mehlmadm@mail.uc.edu, huynhd2@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 10/31/2024
# Course #/Section: IS 4010-001
# Semester/Year: Fall Semester 2024
# Brief Description of the assignment: In this sagacious assignment you will collaborate with peers to develop a VS project modeling something in the real world. Pick a thing in the world of your assigned group that has meaning to all group members. 
# Brief Description of what this module does: This module demonstrates the functionality of two custom classes, DigitalClock and Temperature, through practical examples. The DigitalClock class allows setting and displaying the current time, configuring an alarm, and checking if the current time matches the alarm to trigger an alert. The Temperature class enables setting and displaying the temperature with restrictions on lowering it, allowing only controlled increases, and providing warnings when needed.
# Citations: N/A
# Anything else that's relevant: N/A

from digitalclockPackage.clock import DigitalClock
from tempPackage.temp import Temperature

#main.py
if __name__ == "__main__":
    # clock   
    # Instantiate a DigitalClock object with default time
    clock = DigitalClock()  # Default initialization with time "12:00 AM"
    print("\n=== Digital Clock Demo ===")
    
    # Demonstrate dunder __str__ method to display the clock's initial state
    print("\nInitial clock state (using __str__):")
    print(clock)
    
    # Demonstrate non-dunder set and get methods for current time
    print("\nSetting current time to '7:30 AM'...")
    clock.set_current_time("7:30 AM")
    print(f"Current Time (using get_current_time): {clock.get_current_time()}")

    # Demonstrate non-dunder set and get methods for alarm time
    print("\nSetting alarm time to '8:00 AM'...")
    clock.set_alarm("8:00 AM")
    print(f"Alarm Time (using get_alarm_time): {clock.get_alarm_time()}")

    # Checking alarm (expected to not ring as current time doesn't match alarm time)
    print("\nChecking alarm status (current time is '7:30 AM'):")
    clock.check_alarm()

    # Update current time to match alarm time and check alarm
    print("\nSetting current time to '8:00 AM' to trigger alarm...")
    clock.set_current_time("8:00 AM")
    print(f"Updated Current Time: {clock.get_current_time()}")
    clock.check_alarm()  # This should trigger the alarm

    # Demonstrate dunder __repr__ method to show the official object representation
    print("\nObject representation (using __repr__):")
    print(repr(clock))

    #temp
    # Instantiate a Temperature object
    print("\n=== Temperature Demo ===")
    temp = Temperature(68)  # Initialize with temperature 68°F

    # Demonstrate __str__ method to display the temperature
    print("\nInitial temperature state (using __str__):")
    print(temp)

    # Get and Set Temperature
    print("\nSetting temperature to 72F...")
    temp.set_temp(72)
    print(f"Current Temperature (using get_temp): {temp.get_temp()}F")

    # Attempt to set a lower temperature (should print a warning and still update)
    print("\nAttempting to decrease temperature to 70F...")
    temp.set_temp(70)
    print(f"Updated Temperature: {temp.get_temp()}F")

    # Increase temperature to demonstrate get_warm method
    print("\nIncreasing temperature by 5F...")
    temp.get_warm(5)

    # Demonstrate __repr__ method to show the official object representation
    print("\nObject representation (using __repr__):")
    print(repr(temp))


