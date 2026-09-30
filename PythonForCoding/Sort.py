nums = [5,3,6,2,1]
# sort elements in ascending order
# sort changes the original array
nums.sort()
print(nums)

words = ["Sana","Mina","Nayeon","Chaeyoung","Momo","Dahyun","Tzuyu","Jihyo","Jeongyeon"]
# sorts the words lexicographically by default
words.sort()
print(words)


# sort in descending 
nums.sort(key=None, reverse=True)
# Here Key is optional parameter just pass the reverse flag
print(nums)

# custom sort using a function
# in key parameter we can pass a custom function which will decide how the array will be sorted

def get_length(s:str)->int:
    return len(s)

words.sort(key= get_length)
print(words)

# in descending way
words.sort(key= get_length, reverse=True)
print(words)

# based on absolute value
arr = [-1,87,-34,65,-20,54,-45,-97]

def get_abs(num:int) -> int:
    return abs(num)
arr.sort(key=get_abs)
print(arr)


# sort using lambda
#  We can use a lambda function to define a function in a single line and pass it directly to the .sort() method

# we pass the last character of string for sorting
# syntax include keyword lambda
# The input variable name word can be anything
# the colon after which we define the function body
# the expression  word[len(word)-1] which is the return value

words.sort(key=lambda word:word[len(word)-1])
print(words)


# sorted() copy
# It returns the new list with sorted elements in spcified order

numbers = [5, -3, 2, -4, 6, -2, 4]
sorted_numbers = sorted(numbers, key=abs)
print(sorted_numbers)


