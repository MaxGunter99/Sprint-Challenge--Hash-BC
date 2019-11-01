#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

import os

os.system( 'clear' )


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
    count = len( tickets )

    for i in range( len( tickets ) ):

        if tickets[i].source == 'NONE':

            print( 'START' )
            route.insert( 0 , tickets[i].destination )
            route.pop()
            count -= 1

    index_counter = 0

    while count > 0:

        for x in range( len( tickets ) ):

            if tickets[x].source == route[ index_counter ]:

                index_counter += 1
                route.insert( index_counter , tickets[x].destination )
                route.pop()
                print( route )
                count -= 1

    return route
