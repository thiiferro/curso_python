condicao = False
passou_no_if = None

if condicao:
    print("Faça algo")
    passou_no_if = True
else:
    print("Não faça algo")


if passou_no_if is None:
    print("Não passou no if")

if passou_no_if is not None:
    print("Passou no if")