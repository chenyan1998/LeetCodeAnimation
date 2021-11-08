
nums = [1,2,3,4,2,4]
target = 4 
def twoSum(nums,target):
    l = len(nums)
    print(l)
    ans = []
    for i in range(l-1):
        for j in range(i+1,l):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
                print([i,j])
                break 
    return ans 

twoSum(nums,target)



