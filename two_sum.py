class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dicionário que vai guardar: { VALOR_DO_NUMERO: SEU_INDICE }
        historico = {}

        # O enumerate nos dá o índice (i) e o número real (n)
        for i, n in enumerate(nums):
            complemento = target - n

            # Perguntamos ao dicionário de forma instantânea (O(1)):
            # "Você já viu o número que falta para completar o meu target?"
            if complemento in historico:
                # Se viu, encontramos o par! Retornamos o índice do complemento e o índice atual
                return [historico[complemento], i]

            # Se não viu, guardamos o número atual no dicionário para que os próximos números possam consultá-lo
            historico[n] = i

        return []


# --- CÓDIGO DE TESTE ---
validador = Solution()

lista_produtos = [2, 11, 7, 15]
valor_combo = 9

resultado = validador.twoSum(lista_produtos, valor_combo)
print(f"Os índices dos produtos que formam o combo são: {resultado}")
# Deve exibir [0, 2], pois nums[0] é 2 e nums[2] é 7. (2 + 7 = 9)