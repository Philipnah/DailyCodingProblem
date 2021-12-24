class Solution:
    def solve(self, nums, k):
        amountOfNums = len(nums)

        # precompute the total
        total = 0
        for i in range(amountOfNums):
            total = total + nums[i]

		# check if the solution can be found
        for i in range(amountOfNums):
            if (total - nums[i])/(amountOfNums - 1) == k:
                return True

        return False



# test solution
# function = Solution()

# print(function.solve([1, 3], 2))