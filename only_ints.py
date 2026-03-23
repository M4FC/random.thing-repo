def only_ints(a,b):
    if type(a) == int and type(b) == int:
        return a%1==0 and b%1==0
    else:
        return False

print(only_ints(2,2))