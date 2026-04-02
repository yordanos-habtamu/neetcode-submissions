class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr =[]
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if target == numbers[i] + numbers[j] :
                    if numbers[i] == numbers[j]:
                        continue
                    arr.append(i+1)
                    arr.append(j+1)
                else:
                    continue
        return arr