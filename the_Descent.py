# Shortest Answer

while True:
    print(max([(int(input()),x) for x in range(8)])[1])
    
    
# My answer
while True:
    highest= 0
    idx = 0
    for i in range(8):
        mountain_h = int(input())  
        
        if highest < mountain_h:
            highest = mountain_h
            idx = i 
    
    print(idx)