for i in range(1, 18):
    if i % 15 == 0:
        print(f"fizzbuzz: {i}")
    elif i % 3 == 0:
        print(f"fizz: {i}")
    elif i % 5 == 0:
        print(f"buzz: {i}")
    else:
        print(f"not fizee: {i}")
