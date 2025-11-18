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
