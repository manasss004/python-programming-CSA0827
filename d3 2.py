def num_good_pairs(nums):
    # Create a dictionary to store the count of occurrences of each number
    num_counts = {}
    good_pairs = 0

    # Iterate through the array and count occurrences
    for num in nums:
        if num in num_counts:
            good_pairs += num_counts[num]  # Increment good_pairs by the current count
            num_counts[num] += 1  # Increment the count for this number
        else:
            num_counts[num] = 1  # Initialize the count for this number

    return good_pairs

# Example usage
nums = [1, 2, 3, 1, 1, 2, 2]
result = num_good_pairs(nums)
print("Number of good pairs:", result)
