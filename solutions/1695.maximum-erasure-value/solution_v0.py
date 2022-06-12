def solution_v0(nums):
    subs = list()
    usubs = set()
    out = -float('inf')
    for num in nums:
        if num not in usubs:
            usubs.add(num)
            subs.append(num)
        else:
            while len(nums) > 0 and num in usubs:
                usubs.remove(subs[0])
                subs = subs[1:]
            subs.append(num)
            usubs.add(num)
        out = max(sum(subs), out)
    return out

def solution_v1(nums):
    subs = list()
    usubs = set()
    out = -float('inf')
    for num in nums:
        if num in usubs:
            while len(nums) > 0 and num in usubs:
                usubs.remove(subs[0])
                subs = subs[1:]
        subs.append(num)
        usubs.add(num)
        out = max(sum(subs), out)
    return out

def solution(nums):
    seen = set()
    curr_sum, max_sum, l = 0, 0, 0
    for num in nums:
        while num in seen:
            curr_sum -= nums[l]
            seen.remove(nums[l])
            l += 1
        curr_sum += num
        seen.add(num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    # print(solution(nums = [4, 2, 4, 5, 6]))
    print(solution(nums = [5,2,1,2,5,2,1,2,5]))