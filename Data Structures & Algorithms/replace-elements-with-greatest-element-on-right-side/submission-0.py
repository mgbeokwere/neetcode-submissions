class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            num = arr[i + 1]
            max_num = num
            for j in range(i + 1, len(arr)):
                if j == i + 1:
                    continue
                max_num = max(max_num, arr[j])
            arr[i] = max_num

        return arr
        

        