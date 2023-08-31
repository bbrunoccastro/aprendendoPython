nome=input("Digite o nome do cliente: ")
idade=int(input("Digite a idade do cliente: "))
clienteClube=input("É Cliente Clube Awards ?")
if idade > 65:
    print("O Cliente  " + nome + " é club plus!!!! e sua idade é ")
elif clienteClube=="sim":
    print("O cliente  " + nome + " é clube Awards!!!" )
else:
    print("O cliente " + nome + " Não é fidelidade!!!!" )