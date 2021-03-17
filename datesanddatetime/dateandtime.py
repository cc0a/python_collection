import time

print("The epoch on this system starts at: " + time.strftime('%c', time.gmtime(0)))

print("The current time zone is {0}: ".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is: " + time.tzname[1])

print("The local time is: " + time.strftime('%Y-%m-%d %H-%M-%S'))