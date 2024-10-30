class Temperature:

    def __init__(temp):
        temp._temperature = 75


    def get_temp(temp):
        return temp._temperature
    
    def set_temp(temp, new_temp):
        if new_temp < temp._temperature:
            print("The temperature cannot decrease. It's getting warmer!")
            temp._temperature = new_temp
              

    def get_warm(temp, increase):
        temp._temperature += increase
        print(f"The temperature is getting warmer: {temp._temperature} F")
   
temperature = Temperature()
print(f"The initial temperature is: {temperature._temperature} F")

temperature.get_warm(15)