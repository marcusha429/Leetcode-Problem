class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_square_digit(num):
            sosd = 0
            while num != 0:
                digit = num % 10
                sosd += digit**2
                num = num // 10
            return sosd
        
        if n == 1:
            return True
        
        slow_ptr = n
        fast_ptr = sum_of_square_digit(n)

        while slow_ptr != fast_ptr:
            if fast_ptr == 1:
                return True
            slow_ptr = sum_of_square_digit(slow_ptr)
            fast_ptr = sum_of_square_digit(sum_of_square_digit(fast_ptr))
            
        return False
        