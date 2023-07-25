# Function to take multiple arguments
def add(datatype, *args) :
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int' :
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str' :
        answer = ''

    # Traverse through the arguments
    for x in args :
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print ( answer )


# Integer
add ( 'int', 5, 6 )

# String
add ( 'str', 'Hi ', 'Geeks' )


# code
def add(a=None, b=None) :
    # Checks if both parameters are available
    # if statement will be executed if only one parameter is available
    if a != None and b == None :
        print ( a )
    # else will be executed if both are available and returns addition of two
    else :
        print ( a + b )


# two arguments are passed, returns addition of two
add ( 2, 3 )
# only one argument is passed, returns a
add ( 2 )
