#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Your code here

    tickets_dict = {}
    for ticket in tickets:
        tickets_dict[ticket.source] = ticket.destination

    route = []
    while len(route) < length:
        if len(route) == 0:
            route.append(tickets_dict["NONE"])
        route.append(tickets_dict[route[len(route)-1]])
    
    # I first attempted this in O(n),
    # then I realized that O(2n) is O(n).

    return route
