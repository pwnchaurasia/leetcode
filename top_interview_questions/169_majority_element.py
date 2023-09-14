import collections
import random
import time
import threading




def time_it(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print(f" time taken to execute is--- "
              f"{func.__name__} ---> {time_start} ---> {time_end} ---> {float(time_end - time_start)}")
        return result
    return wrapper



class Solution:
    @time_it
    def my_majorityElement(self, nums):
        element_count = {}
        for i in nums:
            if i in element_count:
                element_count[i] +=1
            else:
                element_count[i] = 1

        major = -999
        major_ele = None
        for i in element_count:
            if element_count[i] > major:
                major = element_count[i]
                major_ele = i
        print(major_ele)
        return major_ele

class Solution2:
    @time_it
    def other_majorityElement(self, nums):
        counts = collections.Counter(nums)
        major = max(counts.keys(), key=counts.get)
        print(major)
        return major


# nums = [3, 2, 3]
# nums = [2, 2, 1, 1, 1, 2, 2]
nums = [random.randint(1, 10) for i in range(10000000)]

sol = Solution()
th1 = threading.Thread(target=sol.my_majorityElement, args=(nums,))
th1.start()

sol = Solution2()
th2 = threading.Thread(target=sol.other_majorityElement, args=(nums,))
th2.start()
th1.join()
th2.join()



