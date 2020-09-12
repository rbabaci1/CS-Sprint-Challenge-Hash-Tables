#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination


def hash_tickets(tickets, length):
    res = {}
    for i in range(length):
        ticket = tickets[i]
        source, destination = ticket.get_source(), ticket.get_destination()
        res[source] = destination
    return res


def reconstruct_trip(tickets, length):
    routes = hash_tickets(tickets, length)
    res = [routes["NONE"]] * length

    for i in range(1, len(res)):
        res[i] = routes[res[i - 1]]
    return res
