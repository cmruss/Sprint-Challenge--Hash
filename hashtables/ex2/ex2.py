#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    cache = {}
    route = [None] * length
    for ticket in tickets:
        if ticket.source == "NONE":
            # find the first ticket, add to results
            route[0] = ticket.destination
        # add each ticket to the cache
        cache[ticket.source] = ticket.destination
    for i in range(1, length):
        # print(f"i: {i}, route[i-1]:{cache[route[i-1]]}")
        route[i] = cache[route[i-1]]
    return route
