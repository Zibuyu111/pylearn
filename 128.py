def longestConsecutive(nums):
    num_set = set(nums)
    max_len = 0
    for x in num_set:
        # 只有x是序列起点时才开始统计
        if x - 1 not in num_set:
            current_num = x
            current_len = 1
            # 向后延伸连续序列
            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1
            max_len = max(max_len, current_len)
    return max_len
