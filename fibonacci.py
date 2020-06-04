fibonacci = lambda num: 1 if num==0 or num == 1 else fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(int(input())))
