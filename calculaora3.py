def calcular(expressao):
    tokens = expressao.split()

    for i in range(len(tokens)):
        if tokens[i] not in "+-*/":
            tokens[i] = float(tokens[i])

    i = 0
    while i < len(tokens):
        if tokens[i] == "*":
            resultado = tokens[i-1] * tokens[i+1]
            tokens[i-1:i+2] = [resultado]
            i = 0
        elif tokens[i] == "/":
            if tokens[i+1] == 0:
                return "Divisão por zero"
            resultado = tokens[i-1] / tokens[i+1]
            tokens[i-1:i+2] = [resultado]
            i = 0
        else:
            i += 1

    i = 0
    while i < len(tokens):
        if tokens[i] == "+":
            resultado = tokens[i-1] + tokens[i+1]
            tokens[i-1:i+2] = [resultado]
            i = 0
        elif tokens[i] == "-":
            resultado = tokens[i-1] - tokens[i+1]
            tokens[i-1:i+2] = [resultado]
            i = 0
        else:
            i += 1

    return tokens[0]


while True:
    expr = input("\nDigite uma expressão (ou 'sair'): ")

    if expr.lower() == "sair":
        print("Encerrando...")
        break

    try:
        resultado = calcular(expr)
        print("Resultado:", resultado)
    except:
        print("Expressão inválida!")