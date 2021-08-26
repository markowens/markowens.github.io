#!/home/mark/penvs/generic/bin/python

def ms2time(millis):
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    print (f"{hours}:{minutes}:{seconds}")
