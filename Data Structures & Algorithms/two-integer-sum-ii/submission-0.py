class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        stanga = 0
        dreapta = len(numbers)-1
        while stanga < dreapta:
            suma = numbers[stanga] + numbers[dreapta]
            if suma == target:
                return [stanga+1, dreapta+1]
            elif suma < target:
                stanga +=1
            elif suma > target:
                dreapta -=1