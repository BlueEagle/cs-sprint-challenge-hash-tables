def intersection(arrays):
    # Your code here
    result = []

    appearance_map = {}
    for array in arrays:
        for item in array:
            # New Pokemon spotted!
            if not item in appearance_map:
                appearance_map[item] = 0
            
            # That's one appearance!
            appearance_map[item] += 1

            # Check if it appears in all lists
            if appearance_map[item] == len(arrays): result.append(item)


    

    # if len(arrays) == 0: return [] # No array found
    # if len(arrays) == 1: return arrays[0] # Only one array found


    # # Make an array of hash maps for searching each array
    # array_maps = []
    # for array in arrays[1:]:
    #     array_maps.append(dict.fromkeys(array))
    
    # for n in array[0]:




    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
