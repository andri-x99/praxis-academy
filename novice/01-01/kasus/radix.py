def radix(nums):
    max1 = max(arr)
    exp  = 1
    while max1/exp > 0:
        counting(arr,exp)
        exp*=10

# nums = [8,5,1,7,4,9,30]
# radix(nums)
# for i in range(len(nums))
#     print(nums[i]),
