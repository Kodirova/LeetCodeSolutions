class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {"I": 1, "V": 5, "X": 10,"L": 50,"C":100,"D": 500,"M":1000}
        result = ''
        for key, value in roman.items():
            x, y = divmod(num, value)
            result += key * x
            num = y

        return result