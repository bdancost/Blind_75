class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Usamos um set (Tabela Hash) para guardar os números já visitados
        visited_numbers = set()

        for current_number in nums:
            # Em Python, buscar em um 'set' custa O(1) de tempo
            if current_number in visited_numbers:
                return True

            # Se não foi visto ainda, adicionamos ao conjunto
            visited_numbers.add(current_number)

        return False


# --- TEST CODE ---
validator = Solution()

product_ids = [10, 25, 30, 42, 25]
has_duplicates = validator.containsDuplicate(product_ids)

print(f"Does the inventory list have duplicates? {has_duplicates}")
# Deve exibir: True (já que o ID 25 se repete)