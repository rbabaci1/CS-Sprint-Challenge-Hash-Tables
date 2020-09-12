def intersection(arrays):
    result = []
    for i in range(len(arrays)):
        arrays[i] = set(arrays[i])

    for x in arrays[0]:
        k = 1
        while k < len(arrays):
            if x not in arrays[k]:
                break
            k += 1
        if k == len(arrays):
            result.append(x)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))
