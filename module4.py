# Han Jiang, 10/25/2025

# Q1: The program asks the user for input N (positive integer) and reads it

N = int(input("Please enter a positive integer N: "))

# Q2: Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

nums = []
for i in range(N):
    num = int(input(f"Please enter {i+1}th number: "))
    nums.append(num)

#print(nums)

# Q3: In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
# or the index (from 1 to N) of this X if the user inputed it before.

X = int(input("Please enter an integer: "))
if X in nums:
    index = nums.index(X) + 1
else:
    index = -1

print(index)
