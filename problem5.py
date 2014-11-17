import sys
from datetime import datetime

def readFile(filename):
    f = open(filename)
    
    times = {}
    
    for line in f:
        time = line.split(',')[1]
        if time in times:
            times[time] += 1
        else:
            times[time] = 1
    
    top_time = sorted(times.items(), key=lambda x: x[1], reverse=True)[0][0]
    top_count = sorted(times.items(), key=lambda x: x[1], reverse=True)[0][1]    
    
    # convert top time to datetime format
    top_time = datetime.strptime(top_time,'%a %b %d %H:%M:%S %Z %Y')
    # convert top time to output form
    top_time = top_time.strftime('%B %d %Y, %H:%M:%S')
    
    print str(top_time) + ' with ' + str(top_count) + ' tweets'
        
if __name__ == '__main__':
    # Read the command text file
    readFile(sys.argv[1])