# Pontuação obtida em cada tipo de fase
pontos_faceis = 3 * 10      # três fases fáceis
pontos_medias = 2 * 25      # duas fases médias
pontos_dificeis = 1 * 50    # uma fase difícil
pontos_lendarias = 1 * 100  # uma fase lendária

# Soma total de pontos
total_pontos = pontos_faceis + pontos_medias + pontos_dificeis + pontos_lendarias

# Número total de fases jogadas
total_fases = 3 + 2 + 1 + 1

# Cálculo da média
media = total_pontos / total_fases

# Exibindo o resultado com f-string
print(f"A média de pontos por fase foi: {media}")
