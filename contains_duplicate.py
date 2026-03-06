"""
Given an integer array nums, return true if any value appears
more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""


def main():
    nums = [1, 2, 2, 3]
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False


if __name__ == "__main__":
    main()
