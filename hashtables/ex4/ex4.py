def has_negatives(a):

    """
    YOUR CODE HERE
    """
    result = []
    for num in a:
        if num < 0:
            # if its negative just add the absolute
            # value to the results.. lol
            result.append(abs(num))
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
