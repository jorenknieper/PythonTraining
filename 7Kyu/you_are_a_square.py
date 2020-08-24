#check if perfect square
def is_square(n):   
    if n > -1 :
         return n**.5 % 1 == 0
    else:
        return False