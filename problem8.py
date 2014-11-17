import sys

def readFile(filename):
    f = open(filename)
    
    NewYork = {}
    SanFran = {}
    
    for line in f:
        lat = float(line.split(',')[3])
        lon = float(line.split(',')[2])
        hashtags = line.split(',')[4:]
        
        if lat >= 40.4957 and lat <= 40.9176 and lon >= -74.2557 and lon <= -73.6895:
            for h in hashtags:
                tag = h.rstrip('\n')
                if tag in NewYork:
                    NewYork[tag] += 1
                else:
                    NewYork[tag] = 1
        
        if lat >= 37.7038 and lat <= 37.8545 and lon >= -122.5155 and lon <= -122.3247:
            for h in hashtags:
                tag = h.rstrip('\n')
                if tag in SanFran:
                    SanFran[tag] += 1
                else:
                    SanFran[tag] = 1    
        
    print 'New York:'
    
    count = 5
    for i in sorted(NewYork.items(), key=lambda x: (-x[1], x[0])):
        if count > 0:
            print i[0] + ', ' + str(i[1])
            count -= 1
    
    print 'San Francisco:'
    
    count = 5
    for i in sorted(SanFran.items(), key=lambda x: (-x[1], x[0])):
        if count > 0:
            print i[0] + ', ' + str(i[1])
            count -= 1


if __name__ == '__main__':
    # Read the command text file
    readFile(sys.argv[1])