def intersection(arrays):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for i in arrays:
        for j in i:
            if j in cache:
                print(f"gotten")
                cache[j] += 1
            else:
                cache[j] = 1
    for k in cache:
        if cache[k] == len(arrays):
            result.append(k)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
