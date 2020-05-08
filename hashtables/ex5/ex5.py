def finder(files, queries):

    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for word in queries:
        cache[word] = []

    for path in files:
        base = path.split("/")[-1]
        # print(base)
        if base in cache:
            result.append(path)
        # print(cache)
        # elif base in cache:
        #     cache[base].append(path)

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
