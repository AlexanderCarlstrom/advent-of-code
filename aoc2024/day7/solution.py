import sys
import re
import math

def p1():
  def is_valid(target, nums):
    if len(nums) == 1:
      return target == nums[0]

    return is_valid(target - nums[-1], nums[:-1]) or (target % nums[-1] == 0 and is_valid(target // nums[-1], nums[:-1]))

  D = open(f'{sys.argv[1]}.txt').read().strip().split('\n')
  sum = 0
  for line in D:
    result = list(map(int, re.findall(r'\d+', line)))

    target, nums = result[0], result[1:]
    if is_valid(target, nums):
      sum += target

  print(sum)


def p2():
  def is_valid(target, nums):
    if len(nums) == 1:
      return target == nums[0]

    if is_valid(target - nums[-1], nums[:-1]):
      return True

    if target % nums[-1] == 0 and is_valid(target // nums[-1], nums[:-1]):
      return True

    return int(str(target)[-len(str(nums[-1])):]) == nums[-1] and is_valid(int(str(target)[:-len(str(nums[-1]))]), nums[:-1])


  D = open(f'{sys.argv[1]}.txt').read().strip().split('\n')
  sum = 0
  for line in D:
    result = list(map(int, re.findall(r'\d+', line)))

    target, nums = result[0], result[1:]
    if is_valid(target, nums):
      sum += target

  print(sum)


# p1()
p2()
