#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # loop through all the the ticket in the array of given tickets
    for ticket in tickets:
        # add the tickets source/destination to the hashtable as a pair using insert function
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # get the first item for the route where key is NONE using retrieve function
    first_ticket = hash_table_retrieve(hashtable, 'NONE')
    # insert it into the first position on the route
    route[0] = first_ticket

    # for the rest of the tickets in the route
    for i in range(1, len(route)):
        # get the index of the preceding ticket to be inserted from the route
        preceding_ticket = route[i - 1]
        # retrieve the value of the preceding ticket from the hastable
        preceding_ticket_value = hash_table_retrieve(hashtable, preceding_ticket)
        # insert it into postion in routes
        route[i] = preceding_ticket_value

    return route[:-1]
