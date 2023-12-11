for index in range(1,101):
    if index%3==0 and index%5==0:
        print("FizzBuzz")
    elif index%5==0:
        print("Buzz")
    elif index%3==0:
        print("Fizz")
    else:
        print(f"Turn number : {index}")
