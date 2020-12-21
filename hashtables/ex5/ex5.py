def finder(files, queries):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # add each query to the cache
    for word in queries:
        # initialize as array for storage of matching paths:
        # for faster lookup not really implemented
        cache[word] = []
    for path in files:
        # take the base for matching query
        base = path.split("/")[-1]
        # if we find the base 
        if base in cache:
            # add the path to the results 
            result.append(path)
            # add the path to the cache
            cache[base].append(path)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
