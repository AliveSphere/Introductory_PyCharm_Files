# Charles Buyas cjb8qf


# import random


# print("\nWelcome to the everything calculator!\n")
# number_counter = 0
# while number_counter == 0:
#     user_num = int(input("Input a number, any number!: "))
# first_choice = str(input("What would you like to do? (Add = A, Subtract = S, Multiply = M, Divide = D): ")).upper()
#     user_num_2 = int(input("What's your second number?: "))
#     if first_choice == 'A':
#         num_ = user_num + user_num_2
#         print("Answer:", num_)
#     if first_choice == 'S':
#         num_ = user_num - user_num_2
#         print("Answer:", num_)
#     if first_choice == 'M':
#         num_ = user_num * user_num_2
#         print("Answer:", num_)
#     if first_choice == 'D':
#         num_ = user_num / user_num_2
#         print("Answer:", num_)
#     user_prompt = str(input("Continue? (Y or N): ")).upper()
#     if user_prompt == 'Y':
# second_choice = str(input("What would you like to do? (Add = A, Subtract = S, Multiply = M, Divide = D): ")).upper()
#         user_num_3 = int(input("What's your third number?: "))
#         if second_choice == 'A':
#             num_2 = num_ + user_num_3
#             print("Answer:", num_2)
#             number_counter += 1
#         if second_choice == 'S':
#             num_2 = num_ - user_num_3
#             print("Answer:", num_2)
#             number_counter += 1
#         if second_choice == 'M':
#             num_2 = num_ * user_num_3
#             print("Answer:", num_2)
#             number_counter += 1
#         if second_choice == 'D':
#             num_2 = num_ / user_num_3
#             print("Answer:", num_2)
#             number_counter += 1
#     if user_prompt == 'N':
#         break


# centered average
# list_of_int = input("Please input a list of numbers separated by a space: ").split(" ")
# print(list_of_int)
# max_val = max(list_of_int)
# min_val = min(list_of_int)
# print("The max is:", max_val)
# print("The min is:", min_val)
# list_of_int.remove(max_val)
# list_of_int.remove(min_val)
# print(list_of_int)
# avg = 0
# counter = 0
# for i in list_of_int:
#     avg += int(i)
#     counter += 1
# print("The average is:", int(avg/counter))


# def centered_average(val_lst):
#     val_lst.remove(max(val_lst))
#     val_lst.remove(min(val_lst))
#     for i in range(len(val_lst)):
#         val_lst[i] = int(val_lst[i])
#     return sum(val_lst)/len(val_lst)
# values = input("Please input a list of numbers separated by a space: ").split(" ")
# print("Average is:", centered_average(values))


# def palindrome(word):
#     reverse = ""
#     for i in word:
#         reverse = i + reverse
#     if reverse == word:
#         return True
#     else:
#         return False
# print(palindrome("mom"))


# user_cost = input("Please enter the cost of loans, insurance, gas, oil, tires, and maintenance separated by spaces: ")
# cost_list = user_cost.split(" ")
# for i in range(len(cost_list)):
#     cost_list[i] = int(cost_list[i])
# print("Total monthly payment:", sum(cost_list), "\nAnnual payment:", (sum(cost_list))*12)


# actual_value = int(input("What's the value of the property in question?: "))
# ass_value = float(actual_value * 0.6)
# print("The assessed value is: $" + format(ass_value, '.2f'))
# tax = float(ass_value/100) * 0.72
# print("The property tax is: $" + format(tax, '.2f'))


# seats = input("How many tickets were sold for Class A, Class B, and Class C seats? (enter separated by spaces): ")
# seat_list = seats.split(" ")
# for i in range(len(seat_list)):
#     seat_list[i] = int(seat_list[i])
# a_total = seat_list[0] * 20
# b_total = seat_list[1] * 15
# c_total = seat_list[2] * 10
# total = float(a_total + b_total + c_total)
# print("Total ticket sales were: $", format(total, '.2f'))


# file = open("my_name.txt", 'w')
# file.write("Charlie Buyas.")
# file.close()


# file = open("my_name.txt", 'r')
# for line in file:
#     print(line)
# file.close()


# file = open("number_list.txt", 'w')
# counter = 1
# while counter < 101:
#     file.write(str(counter) + '\n')
#     counter += 1
# file.close()


# total = 0
# file = open("number_list.txt", 'r')
# for line in file:
#     line.strip('\n')
#     total += int(line)
# print("Total: ", total)
# file.close()


# lotto_num = []
# for i in range(1, 8):
#     lotto_num.append(random.randint(0, 9))
# for x in range(len(lotto_num)):
#     print(lotto_num[x])
# print(lotto_num)


# monthly_rain = input("Enter total rainfall each month in one year separated by a space: ")
# rain_list = monthly_rain.split(" ")
# for i in range(len(rain_list)):
#     rain_list[i] = int(rain_list[i])
# year_total = sum(rain_list)
# month_avg = year_total/12
# high = max(rain_list)
# low = min(rain_list)
# print("Total rainfall for the year:", year_total, "\nMonthly average:", month_avg, "\nHigh and low:", high, low)


# def larger_than_n(list_, number):
#     final_list = []
#     for i in range(len(list_)):
#         if list_[i] > number:
#             final_list.append(list_[i])
#     return final_list
