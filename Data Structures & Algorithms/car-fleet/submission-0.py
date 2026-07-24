class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        arr = []
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            arr.append([position[i], speed[i], time])
        arr = sorted(arr, reverse=True)
        print(arr)
        stack = []
        for i in range(0, len(arr)):
            if stack and (arr[i][2] <= stack[-1][2]):
                continue
            stack.append(arr[i])
        return len(stack)