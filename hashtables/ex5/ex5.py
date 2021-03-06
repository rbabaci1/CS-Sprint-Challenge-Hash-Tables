def finder(files, queries):
    storage, result = {}, []

    for f in files:
        file_name = f.split("/")[-1]
        if file_name not in storage:
            storage[file_name] = []
        storage[file_name].append(f)

    for q in queries:
        if q in storage:
            result += storage[q]

    return result


if __name__ == "__main__":
    files = ["/bin/foo", "/bin/bar", "/usr/bin/baz"]
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
