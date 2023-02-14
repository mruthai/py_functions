
# Exercise #3
# Write a program to implement a Linear Search Algorithm. 


# Hint: Linear Searching will require searching a list for a given number.

nums_list = [10,23,45,11,15,70]
target = 70

def lin_se(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return True
        else:
            continue
            
    return False

print(lin_se(nums_list,target))


