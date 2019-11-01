#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    
    if length == 1:

        return None
    
    else:

        print( weights , limit )

        for x in range( len( weights ) ):

            for y in range( len( weights ) ):

                if weights[ x ] + weights[ y ] == limit:

                    if x == y:

                        None

                    else:
                        
                        return ( y , x )


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
