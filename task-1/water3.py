def initial_state():
    return (8, 0, 0)

def is_goal(s):
    if s == (3,5,0):
        return True
    return False

def successors(s):
    a, b, c = s
    t = 3 - c 
    if (a > 0 and t > 0): # Verify whether cup 'a' contains water, and if cup 'c' requires water (when t is greater than zero).
        if a > t:
            yield((a-t, b, c+t), t)
        else:
            yield((0, b, c+a), a)

    if (b > 0 and t > 0): # Verify whether cup 'b' contains water, and if cup 'c' requires water (when t is greater than zero).
        if b > t:
            yield((a, b-t, c+t), t)
        else:
            yield((a, 0, c+b), b)
    t = 5-b
    if (a > 0 and t > 0): # Verify whether cup 'a' contains water and if cup 'b' requires water (with t greater than zero).
        if a > t:
            yield((a-t, b+t, c), t)
        else:
            yield((0, b+a, c), a)

    if (c > 0 and t > 0): # Verify whether cup 'c' contains water and if cup 'b' requires water (with t greater than zero).
        if c > t:
            yield((a, b+t, c-t), t)
        else:
            yield((a, b+c, 0), c)

    t = 8 - a
    if (b > 0 and t > 0): # if (b > 0 and t > 0): # Examine if cup 'b' contains water and whether cup 'a' requires water (given t is greater than zero).
        if b > t:
            yield((a+t, b-t, c), t)
        else:
            yield((a+b, 0, c), b)

    if (c > 0 and t > 0): #if (b > 0 and t > 0): # Examine if cup 'c' contains water and whether cup 'a' requires water (given t is greater than zero).
        if c > t:
            yield((a+t, b, c-t), t)
        else:
            yield((a+c, b, 0), b)
    


