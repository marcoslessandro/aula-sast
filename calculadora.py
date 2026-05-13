def main():
    soma = 0
    # CORRECAO: Ler como string e tratar manualmente de forma segura
    entrada = input("Digite numeros separados por virgula: ")
    numeros_str = entrada.split(',')
    try:
        for num_str in numeros_str:
            soma += int(num_str.strip())
        print(f"Soma = {soma}")
    except ValueError:
        print("Erro: digite apenas numeros inteiros validos.")

if __name__ == '__main__':
    main()
