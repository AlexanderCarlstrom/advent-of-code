import sys

def parse():
  D = open(sys.argv[1]).read().strip().split('\n')

  nums1 = []
  nums2 = []

  for line in D:
    nums = [ int(num) for num in list(filter(None, line.split(' ')))]
    nums1.append(nums[0])
    nums2.append(nums[1])

  return nums1, nums2

def solve_p1():
  nums1, nums2 = parse()
  nums1 = sorted(nums1)
  nums2 = sorted(nums2)
  sum = 0
  for i in range(len(nums1)):
    sum += abs(nums1[i] - nums2[i])

  print(sum)


def solve_p2():
  nums1, nums2 = parse()
  scores = [ num * nums2.count(num) for num in nums1]

  print(sum(scores))


solve_p2()