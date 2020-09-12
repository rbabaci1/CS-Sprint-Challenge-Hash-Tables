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
    routes, res = {}, ["NONE"] * length

    for i in range(length):
        ticket = tickets[i]
        source, destination = ticket.get_source(), ticket.get_destination()
        routes[source] = destination

    current, i = routes["NONE"], 0
    while current != "NONE":
        res[i] = current
        current = routes[current]
        i += 1
    return res

