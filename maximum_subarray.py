class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Inicializamos ambas variables con el primer elemento del arreglo
        current_sum = nums[0]
        max_sum = nums[0]

        # Recorremos el arreglo desde el segundo elemento (índice 1)
        for i in range(1, len(nums)):
            current_num = nums[i]

            # Decisión clave: ¿Continuamos el subarreglo anterior o empezamos uno nuevo?
            if current_sum < 0:
                current_sum = current_num
            else:
                current_sum += current_num

            # Actualizamos la máxima suma global si el acumulado actual es mayor
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


# --- TEST CODE ---
validator = Solution()

financial_records = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
highest_growth = validator.maxSubArray(financial_records)

print(f"The maximum contiguous subarray sum is: {highest_growth}")
# Debe mostrar: 6 (correspondiente al subarreglo [4, -1, 2, 1])