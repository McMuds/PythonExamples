# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for number in numbers:
    if number % 2 == 0:
        print(number)



# 2. Print the difference between the largest and smallest value:
sorted_list = sorted(numbers)
largest = sorted_list[-1]
smallest = sorted_list[0]
print(f"The difference between the largest and smallest numbers is {largest-smallest}")

# 3. Print True if the list contains a 2 next to a 2 somewhere.
prev_number_is_2 = False
for number in numbers:
    # print(f"Bool/Curr: {prev_number_is_2} / {number}")
    if prev_number_is_2 and number == 2:
        print ("True")
    elif number == 2:
        # print(f"Elif: Bool/Curr: {prev_number_is_2} / {number}")
        prev_number_is_2 = True
    else:
        prev_number_is_2 = False
# Note - this will print multiple "True's". If only one is required, set a boolean 
# and outside the loop, do the print based on that
# answer:
result = False
index = 0
for number in numbers:
    if not(index == 0) and (number == 2 and numbers[index-1] == 2):
        result = True
    index += 1
print(result)


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
number_sum = 0
sum_flag = True
# numbers.append(3)  #this was for testing. also, I suspect it could be more elegant.
print(f"Q4: Before the loop: {numbers}")
for number in numbers:
    if sum_flag:
        if number == 6:
            sum_flag = False
        else:
            number_sum += number
    else:
        if number == 7:
            sum_flag = True
print (f"The total is  {number_sum}")

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
q5_total = 0
i = 0
print(f"Q5: Before the loop: {numbers}")
for number in numbers:
    if (i == 0 and number == 13) or numbers [i-1] == 13:
        print(f"Ignoring number {number}.")
    else:
        q5_total += number
    i += 1
print(f"The total ignoring 13s and subsequent numbers is {q5_total}.")