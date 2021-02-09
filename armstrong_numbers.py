def is_armstrong_number(number):

    # convert number to string
    string_num = str(number)
    # convert number to list
    string_to_chars = [char for char in string_num]
    # count the number of digits
    no_of_digits = len(string_num)

    #initialize sum variable
    sum_of_power = 0
    
    # raise each digit to the power of no_of_digits
    for each_digit in string_to_chars:
        # add each result
        sum_of_power += int(each_digit)**no_of_digits

    # check if number = sum of its digit raised to the power of no_of_digits
    if number == sum_of_power:
        return True
    else:
        return False
