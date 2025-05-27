numero_str = input("Digite um número inteiro: ")

try:
    numero_int = int(numero_str)
    result = numero_int % 2
    if result == 0:
        print(f"O número {numero_str} é par")
    else:
        print(f'O número {numero_str} é impar')

except:
    print("O número digitado não é inteiro")



# ----------------------------------------------------------------

hora_str = input("Que horas são? ")
hora = int(hora_str)

if hora <= 11:
    print("Bom dia")
elif hora <= 17:
    print("Boa tarde")
elif hora <= 23:
    print("boa noite")
else:
    print("Isso não são horas")

# -----------------------------------------------------------------

nome = input("Digite seu primeiro nome: ")
qt_letras = len(nome)

if qt_letras <= 4:
    print("Seu nome é curto")

elif 5 == qt_letras or 6 == qt_letras:
    print("Seu nome é normal")
else: 
    print("Seu nome é muito grande")