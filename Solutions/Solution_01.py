#Solution_01.py

def ex_01(x,y):
    if x*y <= 1000:
        return x*y
    else:
        return x+y

#Test (a)

print(ex_01(20, 30))
print(ex_01(45,57))
print(ex_01(500, 2)) #Testing the extreme cases: if x*y = 1000, it returns the product. 
print(ex_01(1001, 1)) #Similarly, if x*y > 1000, the function returns the sum.

