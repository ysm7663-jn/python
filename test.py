def func(data, target):
    print(data)
    for i in range(len(data[0])):
        if len(data) == 1 and target == data[0][i]:
            return True

        if len(data) == 1 and target != data[0][i]:
            return False

        if len(data) == 0:
            return False

    mid = len(data) // 2

    for i in range(len(data[mid])):
        if target == data[mid][i]:
            return True
        else:
            if target > data[mid][0]:
                return func(data[mid:], target)
            else:
                return func(data[:mid], target)

data = [[1, 3, 5, 7],[10, 11, 16, 20],[23, 30, 34, 50]]
target = 30
print(func(data, target))