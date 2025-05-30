import random
import time


def dashboard_Warning():

        # giving the ramdom realistic values to the parameters
        while True:
            # fuel level indicator
            fuel_level = random.randint(0, 100)
            #engine temoerature
            Engine_temp = random.randint(70, 120)
            #oil pressure
            oil_pressure = random.uniform(0.5, 5.0)

            if  80 < fuel_level <= 100:
                print(f"the fuel level is reached to = {fuel_level}")
            if Engine_temp > 100:
                print(f"the engine temperature is reached to ={Engine_temp} C")
            if oil_pressure > 80:
                print(f"the oil pressure is reached to {oil_pressure:.2f} ")

            time.sleep(2)


    try:
        dashboard_Warning()
    except KeyboardInterrupt:
        print("warning is done ")





