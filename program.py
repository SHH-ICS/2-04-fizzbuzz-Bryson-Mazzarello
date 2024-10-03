result = ""

for myNumber in range(33):
    if myNumber % 15 == 0:
        result = str(result) + "Fizzbuzz" + "\n"
    elif myNumber % 5 == 0:
        result = str(result) + "Buzz" + "\n"
    elif myNumber % 3 == 0:
        result = str(result) + "Fizz" + "\n"
    else:
        result = str(result) + str(myNumber) + "\n"
print(result)