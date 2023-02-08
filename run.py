import time
import colorama
from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
colorama.init()

print(colorama.Back.WHITE)
print(colorama.Fore.BLACK)


name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
name = input("Timer or Weather ?\n  T or W:")


accepted_inputs = ["w", "W", "t", "T"]
while name not in accepted_inputs:
    colorama.init()
    print(colorama.Back.RED)
    print(colorama.Fore.WHITE)
    print("only Timer or Weather")
    name = input('"' + name + '"' + " not allowed\n  T or W:")
if name == str("t" or "T"):
    timer = input('what you want a set up ? \n Seconds, Minutes or Hours? \n S or M or H')
    accepted_inputs = ['s', 'S', 'm', 'M', 'h', 'H']
    while timer not in accepted_inputs:
        print("only Seconds, Minutes or Hours")
        timer = input('"' + timer + '"' + " not a time \n  S or M or H : ")
    if timer == str('s' or 'S'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # seconds
            timeUser = int(input("Set seconds:"))
            # accepted_inputs = ["0-9"]
            # while timeUser not in accepted_inputs:
            #     print('error')
            # timeUser = int(input("Set seconds:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(1)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('m' or 'M'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # minutes
            timeUser = int(input("Set minutes:"))
            comment = str(input("Write comment:"))
            for q in range(timeUser):
                time.sleep(60)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W:")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")
    if timer == str('h' or 'H'):
        if True:
            colorama.init()
            print(colorama.Back.YELLOW)
            i = 0  # hours
            timeUser = int(input("Set hours : "))
            comment = str(input("Write comment : "))
            for q in range(timeUser):
                time.sleep(3600)
                i += 1
            print("Time out ! ")
            print("Your comment is: " + comment)
            name = input("Timer or Weather ?\n  T or W : ")

    accepted_inputs = ["w", "W", "t", "T"]
    while name not in accepted_inputs:
        colorama.init()
        print(colorama.Back.RED)
        print(colorama.Fore.BLACK)
        print("only Timer or Weather")
        name = input('"' + name + '"' + " not allowed\n  T or W:")


if name == str("w" or 'W'):
    while True:
        place = input("Where u live?")
        try:
                
            colorama.init()

            print(colorama.Back.WHITE)
            print(colorama.Fore.BLACK)
            

            owm = OWM("4383a10a783aec00988fb6992379ab92")
            mgr = owm.weather_manager()
            
            
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
            elif temp < 50:
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
            break


        except NotFoundError:
            print(colorama.Back.RED)
            print(colorama.Fore.WHITE)
            print('"' + place + '"' + ' is not a city \nWrite exists City or Country')
          
            
        

