palavra = input("Digite uma palavra com 3 letras min e 10 max: ")
quant = len(palavra)

while quant < 3 or quant > 10:
    print("Digite outra palavra")
    palavra = input("Digite uma palavra com 3 letras min e 10 max: ")
    quant = len(palavra)
if palavra:
    print("Agora deu certo!!")