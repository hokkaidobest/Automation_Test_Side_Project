def division(x, y):
    # your code here

    try:
        if type(y) != int:
            raise TypeError
        elif y == 0:
            raise ZeroDivisionError
        
        # When all the conditions are passed, do the calculation
        print(x / y)
    except TypeError:
        print("y should be integer")
    except ZeroDivisionError:
        print("y cannot be 0")
    finally:
        print("---Finish---")

division(100, 10)   # Should print 10.0 and "---Finish---"
division(100, 0)    # Should Throw ZeroDivisionError, print "y cannot be 0" and "---Finish---"
division(100, "a")  # Should Throw TypeError, print "y should be integer" and "---Finish---"