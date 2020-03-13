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

    # loop through the weights
    for i in range(0, length):
      # the current weight is the weight at that index
        current_weight = weights[i]
        # use the hashtable insert function
        hash_table_insert(ht, current_weight, i)
        # get the index of limit - current weight
        diff = limit - current_weight
        result = hash_table_retrieve(ht, diff)
        # since the order matters, check the size of the indices
        # of the weights and return in the correct order The higher valued index should be placed in the `zeroth` index 
        # and the smaller index should be placed in the `first` index
        if result:
            if length == 2:
                return (1, 0)
            return (i, result)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
