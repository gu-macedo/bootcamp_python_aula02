import cal 

print("\n Por gentileza, escolha qual operação você deseja realizar: ")

print(""" 
1) Soma \n 
2) Resto 5 \n
3) Multiplicação \n
4) Divisão inteira \n
5) Raiz quadrada\n""")

sair = 0

while sair == 1:
    escolha = int(input("Escolha: "))
    if escolha == 1: 
        cal.soma()
    elif escolha == 2: 
        cal.resto_5()
    elif escolha == 3: 
        cal.multiplicacao()
    elif escolha == 4: 
        cal.divisao()
    elif escolha == 5: 
        cal.quadrado()
    else: "Opção inválida"
