def finder(files, queries):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for path in files:
        base = path.split("/")[-1]
        # print(base)
        if base not in cache:
            cache[base] = path
        # print(cache)
    for word in queries:
        if cache.get(word):
            result.append(cache[word])
    print(result)
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
