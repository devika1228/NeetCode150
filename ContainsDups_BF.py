#contains dups 
#brute force
def containsDuplicate(nums):
    for i in range(len(nums)): # Iterate through each element
        # Compare with every other element
        for j in range(i + 1, len(nums)): # Iterate through the rest of the list
            if nums[i] == nums[j]: # Found a duplicate
                return True 
    return False

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(containsDuplicate(nums))  # Output: True

    nums = [1, 2, 3, 4]
    print(containsDuplicate(nums))  # Output: False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums))  # Output: True

# Time Complexity: O(n^2)
# Space Complexity: O(1)

