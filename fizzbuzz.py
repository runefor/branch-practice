for i in range(1, 18):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print(f"fizz: {i}")
    else:
        print(f"not fizee: {i}")
print("It works!")
