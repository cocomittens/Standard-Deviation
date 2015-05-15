import math

# calculates the average of an array of integers
def getAvg(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

# calculates the standard deviation of an array of integers
def getStdDev(nums, avg):
    total = 0
    for num in nums:
        total += (num - avg)**2
    return math.sqrt(total / len(nums))

# gets data set
print("Enter a list of numbers, separated by a space: ")
nums = input().strip().split(' ')
nums = [int(n) for n in nums]

# gets avg + std deviation of data set
avg = getAvg(nums)
stddev = getStdDev(nums, avg)

# prints std deviation of data set
print("The Standard Deviation is: {stddev}".format(stddev=stddev))
