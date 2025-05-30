import random


def dashboard_Warning():

    try:
        # giving the ramdom realistic values to the parameters
        while true:
            # fuel level indicator
            fuel_level = random.randint(0, 100)
            #engine temoerature
            Engine_temp = random.randint(70, 120)
            #oil pressure
            oil_pressure = random.uniform(50, 100)

            if  80 < fuel_level <= 100:
                print(f"the fuel level is reached to = {fuel_level}")


    except KeyboardInterrupt:
        print("warning is done ")


dashboard_Warning()


