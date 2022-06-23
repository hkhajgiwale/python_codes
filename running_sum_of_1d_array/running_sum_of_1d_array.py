nums = [3,1,2,10,1]

sum = nums[0]
last_num = nums[len(nums)-1]
new_array = [sum]

for i in range(len(nums)):
    if i == (len(nums)-1):
        break
    else:
        sum = sum + nums[i+1]
        new_array.append(sum)
        
print(new_array)
