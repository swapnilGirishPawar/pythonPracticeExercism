def square_of_sum(number):
    sum = 0
    for i in range(1, number+1):
        sum += i

    return sum*sum


def sum_of_squares(number):
    sum = 0
    for i in range(1, number+1):
        sq = i*i
        sum += sq
    return sum


def difference_of_squares(number):

    return (square_of_sum(number)-sum_of_squares(number))


print(square_of_sum(10))
print(sum_of_squares(10))
print(difference_of_squares(10))
