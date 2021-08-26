#!/home/mark/penvs/generic/bin/python

import time

def Timer():
    print("Time is " + str(time.time()))

def ms2time(millis):
    millis = int(millis)
    seconds=(millis/1000)%60
    print(f"s: {seconds}")
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    print(f"m: {minutes}")
    minutes = int(minutes)
    hours=(millis/(1000*60*60))
    print(f"h: {hours}")
    hours = int(hours)
    
    print (f"{hours:02d}:{minutes:02d}:{seconds:02d}")
