#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination


def reconstruct_trip(tickets, length):
    routes, res = {}, []

    for i in range(length):
        ticket = tickets[i]
        source, destination = ticket.get_source(), ticket.get_destination()
        routes[source] = destination

    current = routes["NONE"]

    while current != "NONE":
        res.append(current)
        current = routes[current]
        if current == "NONE":
            res.append(current)
            break
    return res

