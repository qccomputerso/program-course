x = 0
# Declares variable x with a value of 0
# You can then use this variable for other stuff
# You can reassign variables by just setting x = 1, x = 2 etc
# x += 1: increments x by 1      x -= 1: decrements x by 1
# x *= 2: multiplies x by 2      x /= 2: divides x by 2

# Data types: check out more here https://www.w3schools.com/python/python_datatypes.asp
int
# Integer type: can store integers, can do basic number operations

float
# Float type: can store decimals and fractions, can do basic number operations

str
# String: A list of characters, think of it like text
# "abcdefg"[0] returns "a", "abcdefg"[1] returns ["b"]
# "abcdefg"[0:3] returns "abc", "abcdefg"[1:4] returns "bcd"
# "abcdefg"[3:] returns "defg", "abcdefg"[:4] returns "abcd"
# "1234567890"[::2] returns "13579", "1234567890"[::3] returns "1470" etc
# "123" + "abc" returns "123abc"
# "123"*123 returns "123123123123..." repeated 123 times

list
# List: Similar to string, but instead of a list of characters, all data types are supported
# Eg: [1, 2, 3, 4, 5][1] returns 2, ["ab", "cd", "ef"][1] returns "cd"
# Do I really need to explain all the operations with [] again
# [1, 2, 3, 4] + ["a", "b", "c", "d"] returns [1, 2, 3, 4, "a", "b", "c", "d"
# [4, 5]*4 returns [4, 5, 4, 5, 4, 5, 4, 5]
# x.append(y): adds item y to list x at the end of list
# x.insert(pos, y): inserts item y in list x at pos x
foo = [1, 2, 3, 4]
foo.insert(1, 1.5)
# foo is now [1, 1.5, 2, 3, 4]
# a in b: checks if item a is in b
# 1 in [1, 2, 3] returns true
# 4 in [1, 2, 3] returns false
# 4 not in [1, 2, 3] returns true
# len(x): returns length of x

bool
# Can have two values, true and false
# Useful in if/while blocks
# x and y: returns true only if x and y are both true
# x or y: returns true if x or y is true
# not x: returns true if x is false, and false if x is true

tuple
# Basically just a list except you can"t alter it
# Lists are declared using square brackets, tuples are declared using normal brackets

set
# A list without ordering
# Cannot have duplicate items
# {"a", "a"} is the same as {"a"}
# len(x): returns size of set x
# x.add(y): adds item y to set x
# Declare sets using {} brackets
# To declare an empty set, type set()

dict
# Example of dictionary:
# bar = {
#     "value1": "9",
#     "value2": 234524,
#     "value3": [1, 2, 3]
# }
# Access Item: bar["value1"] returns "9", bar["value2"] returns 234524, etc
# Add Item: bar["value4"] = { "value5": (3, 2, 1) }

# test = "value9"
# {
#     test: "adas"
# }

# returns { "value9": "adas" }

int("1") -> 1
str(1) -> "1"
float(1) -> 1.0
float("1") -> 1.0
list("ab c") -> ["a", "b", " ", "c"]