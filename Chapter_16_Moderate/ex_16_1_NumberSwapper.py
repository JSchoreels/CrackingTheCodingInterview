def swapper(a, b):
    print(f"a={a} b={b}")
    a = a+b
    b = a-b
    a = a-b
    print(f"a={a} b={b}")


swapper(29,101)