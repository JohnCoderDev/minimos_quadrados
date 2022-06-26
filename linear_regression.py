from math import exp, log

# Calcula os coeficientes da regressão linear
def linearregression(xdata: list, ydata: list) -> list:
    """
    (param) xdata: dados do eixo x
    (param) ydata: dados do eixo y

    Calcula os coeficientes linear e angular da 
    regressão linear e retorna os valores em uma lista,
    sendo o primeiro valor o coeficiente angular e o segundo
    valor o coeficiente linear. Retorna também o valor de R.

    Levanta um erro caso o número de dados dos eixos
    sejam diferentes.
    """
    if len(xdata) != len(ydata):
        raise "Número de entradas não são iguais"

    # Pega o valor das somas da regressão linear
    # linear
    xsquaresum = xsum = 0
    xyproductsum = ysum = 0
    ndata = len(xdata)

    for x, y in zip(xdata, ydata):
        xsquaresum += x**2
        xsum += x
        xyproductsum += x * y
        ysum += y
    
    denominator = ndata * xsquaresum - xsum ** 2
    a = (ndata * xyproductsum - xsum * ysum) / denominator
    b = (ysum * xsquaresum - xsum * xyproductsum) / denominator

    return [a, b]

# Main function
def main() -> None:
    # Coleta os dados x
    xdata = input("Digite os dados do eixo x separados por vírgula:\n").split(",")
    xdata = [float(x) for x in xdata]
    
    # Coleta os dados y
    ydata = input("Digite os dados do eixo y separados por vírgula:\n").split(",")
    ydata = [float(y) for y in ydata]

    while True:
        print("\nSelecione o tipo de regressão linear\n")
        types = ["y = a x + b", 
                "y = b * e^(a x)",
                "y = b * a^x", 
                "y = 1 / (a x + b)",
                "y = b * n^(a x)"]

        for i, v in enumerate(types):
            print(f'{i + 1}. {v}')
        
        userresponse = int(input("\nDigite sua escolha (0 para sair): "))
        
        if userresponse in range(1, len(types) + 1) or userresponse == 0:
            break
        
    # Aplica a regressão linear conforme o tipo
    # escolhido
    if userresponse == 0:
        exit()

    elif userresponse == 1:
        coefficients = linearregression(xdata, ydata)

    elif userresponse == 2:
        ydata = [log(y) for y in ydata]
        
        coefficients = linearregression(xdata, ydata)
        coefficients[1] = exp(coefficients[1])

    elif userresponse == 3:
        ydata = [log(y) for y in ydata]

        coefficients = linearregression(xdata, ydata)
        coefficients[0] = exp(coefficients[0])
        coefficients[1] = exp(coefficients[1])

    elif userresponse == 4:
        ydata = [1 / y for y in ydata]
        coefficients = linearregression(xdata, ydata)

    elif userresponse == 5:
        n = float(input("Digite o valor de n: "))

        ydata = [log(y, n) for y in ydata]

        coefficients = linearregression(xdata, ydata)
        coefficients[1] = n ** coefficients[1]

    # Printa a equação com os coeficientes
    output = types[userresponse - 1].replace("a", str(coefficients[0]))
    output = output.replace("b", str(coefficients[1]))
    
    if userresponse == 5:
        output = output.replace("n", str(n))
    
    print(output)

if __name__ == "__main__":
    main()