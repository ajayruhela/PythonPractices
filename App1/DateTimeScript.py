#!/usr/bin/python
import time;  # This is required to include time module.
import calendar;

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
print ("time", time.gmtime(0)) # start of time
print ("time", time.gmtime())  # current UTC time 

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

# formated time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

# calendar
cal = calendar.month(2018, 4)
print ("Here is the calendar:")
print (cal)