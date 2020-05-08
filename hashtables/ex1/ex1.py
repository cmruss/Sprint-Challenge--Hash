def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    cache = {}
    index = 0
    while index < length:
        if (limit - weights[index]) not in cache:
            cache[weights[index]] = index
            index += 1
        else:
            return [index, cache[limit- weights[index]]]