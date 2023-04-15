# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


# NÃO SE ESQUEÇA DE INSERIR O LINK DO SEU REPOSITÓRIO NO GITHUB COM O CÓDIGO FONTE QUE VOCÊ DESENVOLVEU

def inverterTextoFornecidoPeloUsuario():
    print("===============================================")
    print("==> Digite o texto que deseja inverter: ")
    texto = str(input("==> "))

    textoInvertido = []

    for letra in texto:
        #insere na posição 0 (se houver elementos, empurra para os antecessores para a próxima posição)
        textoInvertido.insert(0, letra)

    #método para criar strings mesclando arrays[de strings]
    textoInvertido = ''.join(textoInvertido)
    print("================ Resultado ====================")
    print(f'==> R: {textoInvertido}')
    print("===============================================")

inverterTextoFornecidoPeloUsuario()