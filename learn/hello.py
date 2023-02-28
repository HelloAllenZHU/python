#!/usr/bin/python3

#######################################HelloWorld
# print( "Hello world!" )

#######################################变量
# num = 0
# f   = 1.0
# s   = "Hello"
# b   = True
# print( num )
# print( f )
# print( s )
# print( type( s ) )
# print( b )
# print( bool( 1 ) )

#######################################字符串处理
# str0 = "Hello"
# num  = 0
# str1 = "world"
# print( str0 + str( num ) + str1 )
# print( str0.upper() + " " + str1.lower() )

#######################################数组
# ary0 = [0, 1, 2, 3]
# ary1 = ["a", "b", "c"]
# print( len( ary0 ) )
# print( ary0, ary1 )
# print( min( ary0 ) )
# print( max( ary0 ) )
# print( sum( ary0 ) )

## 追加元素
# ary0.append( 4 )
# ary1.append( "d" )
# print( ary0, ary1 )

## 插入元素
# ary0.insert( 0, 1 )
# ary1.insert( 1, "e" )
# print( ary0, ary1 )

## 移除元素
# ary0.remove( 4 )
# ary1.remove( "d" )
# print( ary0, ary1 )

## 弹出最后一个
# ary0.pop()
# ary1.pop()
# print( ary0, ary1 )

## 删除
# del ary0[0]
# del ary1[0]
# print( ary0, ary1 )

## 排序
# ary0.sort()                   # 永久排序
# ary0.sort( reverse=True )     # 反向排序
# ary1.sorted()                 # 临时排序
# print( ary0, ary1 )

## 反向排序
# ary0.reverse()
# ary1.reverse()
# print( ary0, ary1 )

## 切片
# print( ary0[0:1], ary1[0:2] )

#######################################控制流程
# # if else：==、!=、<=、>=、and、or、in
# a = 0
# b = 1
# c = 2
# ary = [0, 1, 2]
# if a in ary:
#     print( a )
# if a == 0:
#     print( a )
# elif b == 1:
#     print( b )
# else:
#     print( c )

# while
# a = 3
# while a >= 0:
#     print( a )
#     a -= 1
# else:
#   print( "完成" )

# # for
# word = "python"
# for char in word:
#     print( char )

# ary = ["a", "b", "c", "d", "e"]
# for index, value in enumerate( ary ):
#     print( str( index ) + " is " + value )

# for item in ary:
#     print( item )

# for index in range( 0, len( ary ) ):
#     print( ary[index] )

# for item in range( 3 ): # 打印 0 到 2 
#     print( item )

# dict = { "name": "Allen ZHU", "age": "20" }
# for key, value in dict.items():
#     print( key + " is " + value )

#######################################函数
# def FuncA( param = "python" ):
#   print("Hello " + param )
#   return param

# ret = FuncA( "Allen ZHU" )
# print( ret )

#######################################面向对象
# # 定义类
# class Animal():
#     # 构造函数
#     def __init__( self, name ): 
#         self.__name = name      # self.__name 为私有成员
#         self.name   = name      # self.name   为公有成员

#     def eat( self ):
#         print( self.name +" eats" )

#     def sleep( self ):
#         print( self.name + " sleeps" )

# # 继承
# class Dog( Animal ):
#     def __init__( self, name ):
#         self.name = name

#     def eat( self ):
#         print( "Dog " + self.name + " eats" )

# # 定义对象
# cat = Animal( "Cat" )
# cat.eat()
# cat.sleep()

# # 定义子类
# dog = Dog( "Jack" )
# dog.eat()
# dog.sleep()

#######################################try...catch
# a = 0

# try:
#     print( 5 / a )
# except:
#     print( "exception" )
# else:
#     print( "something else." )

#######################################module
# # xxx.py
# def funcA():
#     print( "Hello world" )

# # yyy.py
# import xxx

# xxx.funcA()

# import xxx as x

# x.funcA()

# from xxx import funcA

# xxx.funcA()

# from xxx import funcA as A

# xxx.A()

#######################################http
import requests

res = requests.get( "https://www.baidu.com" )
print( res.text )