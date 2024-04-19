d = int(input())
e = int(input())

if ( d > 0 and e > 0 ) :
    print("1")
elif ( d > 0 and e < 0 ) :
    print("4")
elif ( d < 0 and e < 0 ) :
    print("3")
else :
    print("2")