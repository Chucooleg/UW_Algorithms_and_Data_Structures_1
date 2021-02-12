# 1. Write a method that takes in a list of integers and returns their sum
def sum(values):
  if len(values) == 0:
    return 0
  else:
    return values[0] + sum(values[1:])

print(sum([1, 3, 5, 7, 9, 100]) )

# 2. Write a method that determines if the passed string is a palindrome or not
# A palindrome is a word or a phrase that has the same characters forwards and backwards. For example, "never odd or even", "racecar" are palindromes. Given a string containing a word ("racecar") or sequence of words ("never odd or even"), write a function is_palindrome that determines if the passed string is a palindrome or not, returning boolean true or false respectively. You can assume that there is no punctuation and all characters are lowercase. You are not allowed to reverse the string.
def is_palindrome(string):
  string2 = ''
  for c in string:
    if c!= ' ':
      string2 += c 

  if len(string2) < 2:
    return True
  if len(string2) == 2:
    return string2[0] == string2[1]
  return string2[0] == string2[-1] and is_palindrome(string2[1:-1])

print(is_palindrome(string='never odd or even'))


# 3. Implement a recursive method to count how many possible ways a child can 
#    run up n stairs 1 step, 2 steps, or 3 steps at a time.
# 3. A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a recursive method to count how many possible ways the child can run up n stairs. For example, calling your method with an argument of 4 should return 7 since a child can go up the stairs in the following combinations:

# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 1 + 3
# 2 + 1 + 1
# 2 + 2
# 3 + 1

# 1
# 1

# 2
# 1 1 
# 2

# 3
# 1 1 1
# 1 2
# 2 1
# 3

# Challenge: Build on your solution for the previous problem, but include memoization.
def step_ways(steps):
  # base cases
  if steps == 0:
    return 0
  if steps == 1:
    return 1
  if steps == 2:
    return 2
  if steps == 3:
    return 4
  # recursive
  ans = step_ways(steps-3) + step_ways(steps-2) + step_ways(steps-1)
  return ans

print(step_ways(steps=10))


# Challenge: Write a cached version of step_ways().
def step_ways_cached(steps, cache={0:0, 1:1, 2:2, 3:4}):
  if steps not in cache:
    cache[steps] = step_ways_cached(steps-3, cache) + step_ways_cached(steps-2, cache) + step_ways_cached(steps-1, cache)
  return cache[steps]

print(step_ways_cached(steps=10))
