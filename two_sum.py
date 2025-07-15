array_test = [1, 4, 5, 7, 9, 13, 18]

def two_sum(nums, target):
  left = 0
  right = len(nums) - 1

  while left < right:
    expected_sum_value = target - nums[left] - nums[right]

    if expected_sum_value < 0:
      right -= 1
    elif expected_sum_value > 0:
      left += 1
    else:
      return [nums[left], nums[right]]

print(two_sum(array_test, 17))