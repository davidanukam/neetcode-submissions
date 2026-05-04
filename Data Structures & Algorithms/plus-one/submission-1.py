class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits

        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i > 0:
                    digits[i - 1] += 1
                else:
                    new = [1]
                    new.extend(digits)
                    digits = new
        return digits