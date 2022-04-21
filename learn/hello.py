#!/usr/bin/python3

from array import array


def Fn(x):
    return x * x

name    = "Allen ZHU"
age     = 20
message = "Hello world!"

ary     = [0,1,2,3,4,5,"Hello"]

print( name, age, message.title() )
print( ary )
print( ary[-1], ary[-2] )

ary.append( "world" )
print( ary )
ary.insert( 0, "ZhuZheng" )
print( ary )
del ary[1]
print( ary )
ary.pop()
print( ary )
ary.remove("Hello")
print( ary )

for value in range( 1, 10 ):
    print( value )



print( Fn(3) )