def max_difference(arr):
    min_element = arr[0]
    max_diff = 0

    for num in arr[1:]:
        max_diff = max(max_diff, num - min_element)
        min_element = min(min_element, num)
    return max_diff
array = [4, 5, 234, 2, 6, 82, 234,5234]
result = max_difference(array)
print(f"The maximum difference is: ",result)


