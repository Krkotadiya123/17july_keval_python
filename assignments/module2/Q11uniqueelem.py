"""Q.11Write a Python function that takes a list and returns a new list with unique
elements of the first list."""
def unique_list(numbers):
    unique = []
    for i in numbers :
        if i not in unique:
            unique.append(i)
    return unique

print(unique_list([1, 2, 3, 1, 2]))