from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Modifica nums in-place usando partição de Quick Sort (3-Way Partition).
        Não retorna nada.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Troca 0 para a região dos menores (à esquerda)
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 já está na região central, apenas avança
                mid += 1
            else:  # nums[mid] == 2
                # Troca 2 para a região dos maiores (à direita)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# =====================================================================
# --- TESTES ---
# =====================================================================

validator = Solution()

# Teste 1
array1 = [2, 0, 2, 1, 1, 0]
validator.sortColors(array1)
print(f"Resultado Teste 1: {array1}")  # [0, 0, 1, 1, 2, 2]

# Teste 2
array2 = [2, 0, 1]
validator.sortColors(array2)
print(f"Resultado Teste 2: {array2}")  # [0, 1, 2]