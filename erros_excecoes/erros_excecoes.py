try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except ValueError:
    print("Valor inválido")
except IndexError:
    print("Valor inválido")
except:
    print("Valor inválido")
