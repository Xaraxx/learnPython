# scopes2.py 
# Local vs global 

def local():
    # m doesn't belong to the scope defined by the local function 
    # so python will keep looking into the enclosing scope.
    # m is finally found in the global scope 
    print(m,'printing from the local scope')

m = 5
print(m,'printing from the global scope')

local()

