def get_indices_of_item_weights(weights, length, limit):
    # Your code here
    weight_dict = {}
    for i, weight in enumerate(weights):
        # check if counter exists
        counter = limit - weight
        if counter in weight_dict:
            # print(f"Counter found: {counter} for {weight}.")
            # check if current or found key is larger
            if i >= weight_dict[counter]:
                return (i, weight_dict[counter])
            return (weight_dict[counter], i)
        
        # add new item
        weight_dict[weight] = i

    return None
