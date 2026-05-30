class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Inicializamos o preço mínimo com o valor do primeiro dia
        # e o lucro máximo como 0
        preco_minimo = prices[0]
        lucro_maximo = 0

        # Começamos a avaliar a partir do segundo dia (índice 1)
        for i in range(1, len(prices)):
            preco_actual = prices[i]

            # Se o preço de hoje for menor que o nosso mínimo histórico,
            # significa que encontramos um dia muito melhor para COMPRAR.
            if preco_actual < preco_minimo:
                preco_minimo = preco_actual
            else:
                # Se o preço de hoje for maior, simulamos uma VENDA
                lucro_hoje = preco_actual - preco_minimo
                # Ficamos sempre com o maior lucro registrado
                if lucro_hoje > lucro_maximo:
                    lucro_maximo = lucro_hoje

        return lucro_maximo


# --- CÓDIGO DE TESTE ---
validador = Solution()

historico_precios = [7, 1, 5, 3, 6, 4]
resultado = validador.maxProfit(historico_precios)

print(f"O lucro máximo possível para este histórico é: {resultado}")
# Deve exibir: 5