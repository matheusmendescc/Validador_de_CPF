"""
----- FORMULA CPF -----

CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# Validador de CPF

# Estrutura de repetição

while True:
    cpf = input('Digite um CPF válido: ')
    novo_cpf = cpf[:9]                      # Considerar somente os 9 primeiros digitos

    contagem_reversa_1 = 11                 # Contagem reversa para multiplicação (Digito 1)
    contagem_reversa_2 = 12                 # Contagem reversa para multiplicação (Digito 2)
    total_1 = 0                             # Acúmulo total dos valores para a primeira operação
    total_2 = 0                             # Acúmulo total dos valores para a segunda operação

    #Descobrir o primeiro digito pós os 9 iniciais

    for i in range(9):
        contagem_reversa_1 -= 1             # Contagem reversa regredindo até o 2 (Fórmula)
        total_1 += int(novo_cpf[i]) * contagem_reversa_1
        digito_1 = 11 - (total_1 % 11)      # Formula para encontrar o primeiro digito

        if digito_1 > 9:
            digito_1 = 0

    novo_cpf_1 = novo_cpf + str(digito_1)        # Transformando a variavel digito_1 em string

    for m in range(10):
        contagem_reversa_2 -= 1                 # Contagem reversa regredindo até o 2 (Fórmula)
        total_2 += int(novo_cpf_1[m]) * contagem_reversa_2
        digito_2 = 11 - (total_2 % 11)
        if digito_2 > 9:
            digito_2 = 0


    novo_cpf_final = novo_cpf_1 + str(digito_2)

# Validar o CPF com condicional IF

    if novo_cpf_final == cpf:
        print('CPF VÁLIDO!')
        break
    else:
        print('CPF INVÁLIDO!')
        print('Tente novamente!\n--------------------')
        continue