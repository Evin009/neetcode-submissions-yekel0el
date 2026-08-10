class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # improved sol with binary search

        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            to_find = target - numbers[i]

            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == to_find:
                    return [i+1,mid+1]
                elif numbers[mid] > to_find:
                    r  = mid - 1
                else:
                    l = mid + 1
        return []