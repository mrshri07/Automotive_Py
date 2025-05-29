import datetime
import random
import csv
import time
from datetime import (datetime)
from sqlite3.dbapi2 import Timestamp


from email.contentmanager import raw_data_manager
from email.utils import specialsre
from fileinput import filename

#accessing the file
filename = "Sensor_log.csv"

# writing the headers of the csv file table
header = ["Timestamp" , "Temperature(C)" ,"Speed km/h", "RPM"]
# checking the file excistence
try:
    with open(filename, "x", newline=" ") as file:
        writer = csv.writer(file)
        writer.writerow(header)
except FileExistsError:
    pass

try:
    print("Simulating the sensors , press the CRTL+C to STOP\n")
    while True:
#         simulating the values of this varibales
            temp = round(random.uniform( 70.0 , 110.0 ), 2)  #a and b are the mini adn max temp,
            speed =  round(random.uniform( 0 , 180),2 )      #engine speed
            rpm = round(random.uniform(400, 6000))            #rpm

            #     getting the timestamps from the datetime
            timestamp = datetime.now().strftime("%Y-%M-D %H:%M:%S")

#             printing console
            print(f"[{timestamp}] temp : {temp} | speed: {speed} km/h | rmp : {rpm} ")

#             time sleep
            time.sleep(1)
# few  lines added
except KeyboardInterrupt:
    print("\n simulation stopped")


