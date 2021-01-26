base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# 1. For our first problem, write a function that converts a given base-62 string
#    into an integer. Only a single string will be provided, and it will be up to
#    11 characters in length.

def to_base_10(videoId):
  ans = 0
  for i in reversed(range(len(videoId))): # N-1 -> 0
    power = (len(videoId)-1) - i 
    ans += base_62.index(videoId[i]) * (62**power)
  return ans
  
# 2. Write a function that does the opposite of the previous one. 
# That is, it encodes a base 10 number into base 62
# producing a string that represents the same number.

def to_base_62(number):
  i = 1
  ans = ''
  while number > 0:
    lsb = base_62[number % (62**i)]
    ans = str(lsb) + ans
    number = number // 62
  return ans
  
  
  
"""
When sharing a link with a friend have you ever noticed the seemingly random letters and numbers that shortened links are usually made up of?

https://youtu.be/LpuPe81bc2w

In most cases, it's just a base-62 encoded integer. 

In this assignment, you're being tasked to write a pair of functions to convert a base-62 number to base-10 and back again.

Hint: Use an array/string that contains all the numbers and digits: "0123456789AB...YZab...yz". For each letter in the base-62 number, look up the value in the string ("0123456789ABC..."). This gives you the base-62 value for that digit. Keep a running total and remember to keep multiplying by 62
"""
