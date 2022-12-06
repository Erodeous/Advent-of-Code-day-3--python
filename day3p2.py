import sys
arr = [x.strip() for x in sys.stdin]
score=0

for i in range(int(len(arr)/3)):
    print(arr[i*3])
    print(arr[i*3+1])

    print(arr[i*3+2])


    for j in arr[i*3]:
        if j in arr[i*3+1] and j in arr[i*3+2]:
            if j==(j.upper()): score+= ord(j)-64+26
            else: score+= ord(j)-96
            break
    
print(score)
