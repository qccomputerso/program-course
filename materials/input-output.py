a = int(input("Enter a number: "))

if a > 0:
    print("The number is bigger than 0")

elif a == 0:
    print("The number is equal to 0")

else:
    print("The number is smaller than 0")

# input(x): write x onto the terminal, and then take in user input
# for example, if the user writes asdfgjkl 1234567890 into the terminal, 
# input will return a value of "asdfgjkl 1234567890"

# Sometimes you don't want input to be a string, and this is where type casting
# comes in handy. for example, int("13242") will return 13242 as an integer
# You can then do standard number operations on it