# scopes3.py 
# Local, Enclosing and global 

def enclosing_func():
    m = 13

    def local():
        # m doesn't belong to the scope defined by the local 
        # function so python will keep looking into the next 
        # enclosing scoope. This time m is found in the enclosing 
        # scope.
        print(m, 'printing the local scope')

    # calling the function local
    local()

m = 5
print(m, 'printing the global scope')

enclosing_func()

