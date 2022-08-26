# Recursive Multiply: Write a recursive function to multiply two positive integers without using the
# *operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
# of those operations.

def mult_rec(a,b, shift=0, result=0):
    if b == 0:
        return result
    else:
        if b & 1 == 1:
            return mult_rec(a, b >> 1, shift=shift+1, result=result+(a<<shift))
        else:
            return mult_rec(a, b >> 1, shift=shift+1, result=result)

def mult_rec_book(a,b):
    if a == 1:
        return b
    if b == 1:
        return a
    if a == 0 or b == 0:
        return 0
    if b & 1:
        return (mult_rec_book(a, b>>1) << 1) + a
    else:
        return mult_rec_book(a, b>>1) << 1

assert mult_rec(3,5) == 15
assert mult_rec(0,5) == 0
assert mult_rec(3,0) == 0
assert mult_rec(2,6) == 12
assert mult_rec_book(3,5) == 15
assert mult_rec_book(0,5) == 0
assert mult_rec_book(3,0) == 0
print(mult_rec_book(2,6))
assert mult_rec_book(2,6) == 12