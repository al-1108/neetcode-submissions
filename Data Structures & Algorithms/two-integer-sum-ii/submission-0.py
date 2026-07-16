class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1, index2 = 0, len(numbers)-1
        sum = numbers[index1] + numbers[index2]
        while sum != target:
            if sum < target:
                index1 += 1
            if sum > target:
                index2 -= 1
            sum = numbers[index1] + numbers[index2]
        return [index1+1, index2+1]