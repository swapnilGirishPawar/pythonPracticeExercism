arr = []


def convert(number):
    for i in range(1, number + 1):
        if number % i == 0:
            arr.append(i)

    if arr.__contains__(3):
        print("Pling")
    if arr.__contains__(5):
        print("Plang")
    if arr.__contains__(7):
        print("Plong")
    if arr.__contains__(1 and number):
        return print(str(number))
    


convert(3)
