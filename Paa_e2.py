import sys



x = sys.argv[1]
x = int(sys.argv[1])





if x <= 61:
    print ("Tropical Depression")


elif x <= 62 or x <= 88:
    print ("Category", "Tropical Storm"

elif x <= 89 or x <= 117:
     print ("Category", "Severe Tropical Storm")    

elif x <= 118 or x <= 220:
     print ("Category", "Typhoon")      

elif x >220: 
     print ("Category", "Super Typhoon")       
          



