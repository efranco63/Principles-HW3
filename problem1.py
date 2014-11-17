import sys
from datetime import datetime

def readFile(filename):
    f = open(filename)
    
    # set a min and max date in datetime format that can easily be replaced in comparison
    min_date = datetime.strptime('01/20/2050 12:00:00 AM','%m/%d/%Y %I:%M:%S %p')
    max_date = datetime.strptime('01/20/1950 12:00:00 AM','%m/%d/%Y %I:%M:%S %p')
    tweet_count = 0
    
    for line in f:
        items = line.split(',')
        tweet_date = datetime.strptime(items[1], '%a %b %d %H:%M:%S %Z %Y')
        if tweet_date > max_date:
            max_date = tweet_date
        elif tweet_date < min_date:
            min_date = tweet_date
        tweet_count += 1
    
    min_date = min_date.strftime('%B %d %Y, %H:%M:%S')
    max_date = max_date.strftime('%B %d %Y, %H:%M:%S')
    
    print 'There were ' + str(tweet_count) + ' tweets between ' + str(min_date) + ' and ' + str(max_date)
        

if __name__ == '__main__':
    # Read the command text file
    readFile(sys.argv[1])