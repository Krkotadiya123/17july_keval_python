"""Write a Python program to remove duplicates from a list."""

def my_list():

    duplicated_list = [1,1,2,1,3,4,1,2,3,4]
    deduplicated_list = list(set(duplicated_list))
    return deduplicated_list

print(my_list())







