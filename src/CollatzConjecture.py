from asyncio.windows_events import NULL


def steps(number):
    scount = 0
    if number > 0:
        while(number > 1):
            if number % 2 == 0:
                scount += 1
                number = number/2

            else:
                scount += 1
                number = (number*3)+1
        return scount
    else:
        raise ValueError("Only positive integers are allowed")


print(steps(0))
