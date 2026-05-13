def main():
    soma = 0
    try:
        # VULNERABILIDADE: eval() avalia a string inteira
        numeros = eval(input("Digite numeros separados por virgula: "))
    except Exception:
        print("Erro: entrada invalida")
        return

    for num in numeros:
        soma += num
    print(f"Soma = {soma}")

if __name__ == '__main__':
    main()
