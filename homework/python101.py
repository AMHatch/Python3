#Problem 1


# bill = float(input("How much was the meal? :"))

# service_input = input("How was the service? Good? Fair? or Bad?:")

# service = service_input.lower()

# if service == 'good':
#     tip = bill * 0.2  
# elif service == 'fair':
#     tip = bill * 0.15
# elif service == 'bad':
#     tip = bill * 0.1
# else:
#     print("That's not a valid Input. Please choose between Good, Fair and Bad.")

# total = tip + bill

# print('Your tip is $' + str("%.2f" % tip))
# print('Your total is $' + str("%.2f" % total))



#Problem 2 

# bill = float(input("How much was the meal? :"))

# service_input = input("How was the service? Good? Fair? or Bad?:")

# split = input("how many people ate?")

# service = service_input.lower()

# if service == 'good':
#     tip = bill * 0.2  
# elif service == 'fair':
#     tip = bill * 0.15
# elif service == 'bad':
#     tip = bill * 0.1
# else:
#     print("That's not a valid Input. Please choose between Good, Fair and Bad.")

# total = tip + bill

# split_total = float(total) / float(split)

# print('The tip is $' + str("%.2f" % tip))
# print('The total is $' + str("%.2f" % total))
# print('Each person pays $' + str("%.2f" % split_total))

#Problem 3

# answer = 'yes'
# coins = 0

# while answer == 'yes':
#     print('You have ' + str(coins) + ' coins!')
#     answer_input = input('Do you want another?')
#     answer = answer_input.lower()
#     coins += 1
#print('Bye!')

#problem 4

# height = int(input('Height?'))
# width = int(input('Width?'))
# gap = (width - 2) * " "
# hcount = height - 1

# print('*' * width)

# while hcount - 1 > 0:
#     print('*' + gap + '*')
#     hcount += -1

# print('*' * width)


#Problem 5

# print('''
#     *
#    ***
#   *****
#  *******
# ''')

# ^^^ sarcasim but it works ^^^

# gap = " "
# count = 1
# gap_count = 3

# while count < 11 and gap_count >= 0:
#     print(gap * gap_count + '*' * count)
#     count += 2
#     gap_count += -1

#problem 6
# twas a tricky one. 


a = 1

# while a <= 10:
#     b = 1
#     while b <= 10:
#         c = (a * b)
#         print(str(a) + " x " + str(b) + " = " + str(c))
#         b += 1
#     print('')
#     a += 1


