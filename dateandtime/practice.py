import pytz
import datetime

available_zones = {'1': "America/Kentucky",
                   '2': "America/New_York",
                   '3': "America/Sitka",
                   '4': "America/North_Dakota",
                   '5': "America/Indiana",
                   '6': "America/Denver",
                   '7': "Europe/Moscow",
                   '8': "Europe/Ulyanovsk",
                   '9': "Europe/Kirov"}

print("Please choose from the available timezones (or press 0 to quit).")
for place in available_zones:
    print("\t{}. {}".format(place, available_zones[place]))

while True:
    choice = input()

    if choice == 0:
        break

if choice in available_zones.keys():
    tz_to_display = pytz.timezone(available_zones[choice])
    world_time = datetime.datetime.now(tz=tz_to_display)
    print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'), world_time.tzname()))
    print("The local time is {}.".format(datetime.datetime.now(), strftime('%A %x %X')))
    print("UTC TIME IS {}.".format(datetime.datetime.utcnow().strftime('%A %x %X')))
    print()