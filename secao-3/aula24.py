# T H I A G O
# 0 1 2 3 4 5
#-6-5-4-3-2-1

# nome = "Thiago"

# print(nome[0])
# print(nome[-6])
# print(10 * "-")
# print("Thi" in nome)
# print("ago" in nome)
# print("zero" in nome)
# print("zero" not in nome)


nome = input("Digite o seu nome: ")

encontrar = input("Digite oque deseja encontrar: ")

if encontrar in nome:
    print(f'Encontramos: {encontrar}')
else:
    print("Não encontramos")