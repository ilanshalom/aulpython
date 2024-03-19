
letra = input("Digite uma letra do alfabeto (maiúscula): ")

if letra.isalpha():
        if letra.upper() in ['A', 'E', 'I', 'O', 'U']:
            print("A letra digitada é uma vogal.")
        else:
            print("A letra digitada é uma consoante.")
else:
        print("Entrada inválida. Por favor, insira apenas uma letra.")


