import sys

def readFile(file1,file2):
    
    both = []
    hash1 = []
    hash2 = []
    
    f = open(file1)
    for line in f:
        items = line.split(',')        
        for tag in items[4:]:
            tag_clean = tag.rstrip('\n')
            hash1.append(tag_clean)
                
    f = open(file2)
    for line in f:
        items = line.split(',')        
        for tag in items[4:]:
            tag_clean = tag.rstrip('\n')
            hash2.append(tag_clean)
    
    hash1 = set(hash1)
    hash2 = set(hash2)
    
    for tag in hash1:
        if tag in hash2:
            both.append(tag)
    
    both.sort()
    
    for tag in both:
        print tag

if __name__ == '__main__':
    # Read the command text file
    readFile(sys.argv[1],sys.argv[2])