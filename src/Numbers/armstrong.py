def is_armstrong_number(number):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(number))
        temp //= 10

    if number == sum:
        return True
    else:
        print(sum)
        return False


print(is_armstrong_number(153))
