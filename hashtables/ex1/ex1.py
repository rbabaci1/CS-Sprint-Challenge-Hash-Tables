def get_indices_of_item_weights(weights, length, limit):
    storage = {}

    for i in range(length):
        diff, current = limit - weights[i], weights[i]
        if diff in storage:
            return (i, storage[diff])
        else:
            storage[current] = i
