def has_negatives(numbers):
    storage, result = set(), []
    for n in numbers:
        diff = 0 - n
        if diff in storage:
            result.append(abs(diff))
        else:
            storage.add(n)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
