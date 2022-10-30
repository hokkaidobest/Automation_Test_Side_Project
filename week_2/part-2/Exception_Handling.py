def division(x, y):
    # your code here
    class Error(Exception):
        pass

    class ZeroDivisionError(Error):
        pass

    class TypeError(Error):
        pass
    
    while True:
        try:
            if type(y) != int:
                raise TypeError
            elif y == 0:
                raise ZeroDivisionError
            else:
                print(x / y)
                break
        except TypeError:
            print("y should be integer")
            break
        except ZeroDivisionError:
            print("y cannot be 0")
            break
    
    print("---Finish---")

division(100, 10)   # Should print 10.0 and "---Finish---"
division(100, 0)    # Should Throw ZeroDivisionError, print "y cannot be 0" and "---Finish---"
division(100, "a")  # Should Throw TypeError, print "y should be integer" and "---Finish---"