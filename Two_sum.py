nums = [2, 7, 11, 15]
target = 9
def twosum(nums,target):
    hash_map = {} #empty set
    for i,num in enumerate(nums): #2=0,7=1,10=2,15=3 [0,1,2] = i
        if target-num in hash_map: #hash_map is empty
            
            return[hash_map[target-num],i]
        hash_map[num] = i
    return[]
print(twosum(nums,target))   