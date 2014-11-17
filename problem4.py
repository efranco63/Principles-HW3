import sys

def readFile(filename):
    f = open(filename)
    
    hashtags = {}
    
    for line in f:
        items = line.split(',')
        for i in items[4:]:
            tag = i.rstrip('\n')
            if tag in hashtags:
                hashtags[tag] += 1
            else:
                hashtags[tag] = 1
    
    count = 10
    for i in sorted(hashtags.items(), key=lambda x: (-x[1], x[0])):
        if count > 0:
            print i[0] + ', ' + str(i[1])
            count -= 1
        
if __name__ == '__main__':
    # Read the command text file
    readFile(sys.argv[1])