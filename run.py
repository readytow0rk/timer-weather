import time
import colorama 
from pyowm import OWM


name = input('Timer or Weather ?\n  T or W:')


while name != 't'  :
    print('only Timer or Weather')
    name = input('"' + name + '"' + ' not allowed\n  T or W:' )
if name == 't':    
    while True:
        i = 0 #hours
        ii = 0 #minutes
        timeUser = int(input('Set seconds:'))
        comment = str(input('Write comment:'))
        for q in range(timeUser):
            time.sleep(1)
            i += 1
        print('time out')
        print(comment)
    



if name == 'w':
    colorama.init()

    print(colorama.Back.GREEN)


    owm = OWM("4383a10a783aec00988fb6992379ab92")
    mgr = owm.weather_manager()
    place = input('Where u live?')
    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature("celsius")["temp"]

      
    if temp < 5:
        print(
            "In "
            + place
            + " "
            + w.detailed_status
            + " now."
            + " \nIt about : "
            + str(temp)
            + " degree."
            + " "
            "\nPut on all your clothes )"
        )
    elif temp < 10:
        print(
            "In "
            + place
            + " "
            + w.detailed_status
            + " now."
            + " \nIt about : "
            + str(temp)
            + " degree."
            + " "
            "\n50/50 but  cold."
        )
    elif temp < 20:
        print(
            "In "
            + place
            + " "
            + w.detailed_status
            + " now."
            + " \nIt about : "
            + str(temp)
            + " degree."
            + " "
            "\nput on everything you want."
        )
    else:
        print(
            "In "
            + place
            + " "
            + w.detailed_status
            + " now."
            + " \nIt about : "
            + str(temp)
            + " degree."
            + " "
            "\nhell on the Eart."
        )
    input()