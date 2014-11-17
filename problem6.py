import sys
from datetime import datetime

def readFile(filename):
    f = open(filename)
    
    times = {}
    
    for line in f:
        time = datetime.strptime(line.split(',')[1],'%a %b %d %H:%M:%S %Z %Y').strftime('%B %d %Y, %H')
        if time in times:
            times[time] += 1
        else:
            times[time] = 1   
    
    top_time = sorted(times.items(), key=lambda x: x[1], reverse=True)[0][0]
    top_count = sorted(times.items(), key=lambda x: x[1], reverse=True)[0][1]    
    
    print str(top_time) + 'h with ' + str(top_count) + ' tweets'
        
if __name__ == '__main__':
    # Read the command text file
    readFile(sys.argv[1])