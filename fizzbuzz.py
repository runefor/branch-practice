# if문 1개로 fizzbuzz 구현하기
for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
        print("fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) + "FizzBuzz" * (i % 15 == 0))
    else:
        print(f"{i}")
