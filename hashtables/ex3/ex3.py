def intersection(arrays):
    result, num_lists = [], len(arrays)
    for i in range(num_lists):
        arrays[i] = set(arrays[i])

    for x in arrays[0]:
        k = 1
        while k < num_lists:
            if x not in arrays[k]:
                break
            k += 1
        if k == num_lists:
            result.append(x)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
