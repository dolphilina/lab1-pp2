"""Given a list of ints, 
return True if the array contains a 3 next to a 3 somewhere.
"""


def has_33(nums):
    for i in range(len(nums) - 1):
        if(nums[i] == 3 and nums[i + 1] == 3):
            """
            В каждой итерации проверяется, равны ли текущий элемент nums[i] и следующий за ним элемент nums[i + 1] числу 3.
            """
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))