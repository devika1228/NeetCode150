#Contains Dups
#Using a set to track duplicates

def contains_duplicates(nums):
    seen = set() # Create a set to store seen numbers
    # Iterate through each number in the list
    for num in nums:# Iterate through each number 
        if num in seen:# If the number is already in the set, it's a duplicate
            return True
        seen.add(num) # Add the number to the set
    # If no duplicates were found, return False
    return False

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(contains_duplicates(nums))  # Output: True

    nums = [1, 2, 3, 4]
    print(contains_duplicates(nums))  # Output: False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicates(nums))  # Output: True

# Time Complexity: O(n)
# Space Complexity: O(n)

