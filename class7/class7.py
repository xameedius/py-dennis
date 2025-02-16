def reverse_list(lst):
    new_list = []
    for _ in range(len(lst)):
        x = lst.pop()
        new_list.append(x)
    return new_list
print(reverse_list([1, 2, 3, 4]))
