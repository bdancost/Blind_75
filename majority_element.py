from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        majority_count = len(nums) // 2

        for num in nums:
            # Incrementa a contagem do número no dicionário
            counts[num] = counts.get(num, 0) + 1

            # Assim que a contagem passar da metade, retorna o número
            if counts[num] > majority_count:
                return num

        return -1


# =====================================================================
# --- TESTES MANUAIS ---
# =====================================================================

validator = Solution()

# Teste 1: [3, 2, 3] -> Deve retornar 3
nums1 = [3, 2, 3]
print(f"Teste 1: {validator.majorityElement(nums1)}")  # 3

# Teste 2: [2, 2, 1, 1, 1, 2, 2] -> Deve retornar 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(f"Teste 2: {validator.majorityElement(nums2)}")  # 2