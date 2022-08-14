# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.:
# (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8


# bidlo's solution
def row_sum_odd_numbers(n):
    start_odd_number = sum(range(n)) * 2 + 1
    result_odd_number = start_odd_number
    for i in range(n-1):
        start_odd_number += 2
        result_odd_number += start_odd_number
    return result_odd_number

print(row_sum_odd_numbers(5))

# Human's solution
def row_sum_odd_numbers_boss(n):
    return n**3