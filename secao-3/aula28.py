usuario = input("Digite seu nome: ")

idade = input("Digite sua idade: ")

if usuario and idade:
    
    print(f"Seu nome é {usuario}")
    print(f"seu nome invertido é: {usuario[::-1]}")
    
    if " " in usuario:
        print("Seu nome contém espaço")
    else:
        print("Seu nome não contém espaços")
    
    print(f"Seu nome tem {len(usuario)} letras")
    print(f"A primeira letra do seu nome é {usuario[0]}")
    print(f"A última letra do seu nome é {usuario[len(usuario)-1]}")

else:
    print("Desculpe, você deixou campos vazios")