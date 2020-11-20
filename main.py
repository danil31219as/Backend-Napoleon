class Solution:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}

    def romanToInt(self, s: str) -> int:
        numbers = [Solution.roman_dict[simbol] for simbol in s]
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i + 1] -= numbers[i]
                numbers[i] = 0
        return sum(numbers)


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt(input()))
