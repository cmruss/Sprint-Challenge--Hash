def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    cache = {}
    index = 0
    # loop through the weights
    while index < length:
        # look for a value equal to the difference
        # of the limit and each weight 
        if (limit - weights[index]) not in cache:
            # add it to the cache and go to the next weight
            cache[weights[index]] = index
            index += 1
        else:
            # or if in cache, return it
            return [index, cache[limit- weights[index]]]