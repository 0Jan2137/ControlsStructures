###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 27
sum_even = 0
number = N
# Calculate the sum of even numbers

#for i in range(1, N + 1):
 #   if i % 2 == 0:
  #      sum_even += i

while True:
    if N < 1:
        break
    if N % 2 == 0:
        sum_even += N
    N -= 1
    

print(f"The sum of even numbers from 1 to {number} is: {sum_even}")