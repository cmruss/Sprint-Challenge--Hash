def intersection(arrays):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # loop through list elements in arrays
    for i in arrays:
        # and loop through each list
        for j in i:
            # if the number is already in the cache
            if j in cache:
                # increment its value
                cache[j] += 1
            else: # or if not there add with value of 1
                cache[j] = 1
    # loop through the cache
    for k in cache:
        # if the value counter equals the number of lists in arrays
        if cache[k] == len(arrays):
            # add the key to the result array
            result.append(k)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
