x = 0
total = 0
while x < 100:
    #if x % 2 == 1:
    if x & 1:   
        print(x, end=" ")
        total += x
    x += 1
print ("sum =", total )

