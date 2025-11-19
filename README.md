📘 Projeto: Cálculo de Pontuação por Fase – Reinos da Lógica

Este projeto foi desenvolvido para praticar lógica de programação e manipulação de variáveis em Python.
O desafio simula a jornada de Marcelo, um estudante apaixonado por RPG, que completou fases com diferentes níveis de dificuldade, acumulando pontos conforme sua performance.

🎮 Descrição do Desafio

Marcelo jogou 7 fases no total:

3 fases fáceis → 10 pontos cada

2 fases médias → 25 pontos cada

1 fase difícil → 50 pontos cada

1 fase lendária → 100 pontos

O objetivo do programa é:

Criar variáveis contendo os pontos obtidos em cada tipo de fase.

Calcular o total de pontos.

Calcular a média de pontos por fase.

Exibir o resultado usando f-string.

🧠 Lógica Utilizada

O cálculo segue a fórmula:

média = total_de_pontos / total_de_fases

🧾 Código Utilizado
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

▶ Como executar

Instale o Python (se ainda não tiver).

Abra o projeto no VS Code.

Execute o arquivo pelo terminal ou usando Run > Run Without Debugging.

📁 Estrutura do Projeto
/
├── desafio_pontos.py
└── README.md

✨ Objetivo educacional

Este exercício foi feito para treinar:

Variáveis

Operações aritméticas

Organização de código

Uso de f-strings

Lógica básica em Python
