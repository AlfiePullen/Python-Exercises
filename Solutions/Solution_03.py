def Ex_03(x):
    result = ""               # Create an empty string to store the
                              # characters found at even indexes.

    for i in range(len(x)):
        if i % 2 == 0:
            result += x[i]    # Add (concatenate) the character at
                              # index i to the end of the result string.

    return result     
