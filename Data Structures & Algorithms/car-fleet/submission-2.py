class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        arr = []
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            arr.append([position[i], speed[i], time])
        arr = sorted(arr, reverse=True)
        final_arr = []
        for i in range(0, len(arr)):
            if final_arr and (arr[i][2] <= final_arr[-1][2]):
                continue
            final_arr.append(arr[i])
        return len(final_arr)