35. Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

approsch :
* ]Use Binary Search to find the target efficiently in O(log n).
* ]If target is not found, the final low pointer will give you the insert position. 

def searchInsert(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
Input: nums = [1,3,5,6], target = 5
Output: 2 # Target 5 is at index 2.

Input: nums = [1,3,5,6], target = 2
Output: 1 #If 2 is inserted between 1 and 3, its index would be 1.

Input: nums = [1,3,5,6], target = 7
Output: 4 # 7 would be inserted at the end.


    return low  # insert position 

66 ]  Problem Statement:
You are given a large integer represented as an array of digits, where each digit is between 0 and 9.
The digits are arranged so that the most significant digit is at the start of the array.
You are asked to add one to the integer and return the resulting digits as a new array.


def plusOne(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):  # Start from last digit
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0  # Set current position to 0 if it was 9
        
    # If loop completes, it means digits were like [9,9,9]
    return [1] + digits
 i ]Input: digits = [1, 2, 3]
    Output: [1, 2, 4] #  The integer is 123. Adding 1 gives 124.

ii ]Input: digits = [9]
    Output: [1, 0] # 9 + 1 = 10 → need to extend the array.
iii] 
