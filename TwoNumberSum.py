def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentsum = array[left] + array[right]
        if currentsum == targetSum:
            return sorted([array[left],array[right]])
        elif currentsum < targetSum:
            left += 1
        elif currentsum > targetSum:
            right -=1
    return([])
    
twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164)
