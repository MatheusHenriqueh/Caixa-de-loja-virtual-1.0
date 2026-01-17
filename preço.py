#Calculadora de preços (loja)
#Autor: Matheus Henrique
print("Bem-vindo(a) a MaxShop! ")
print('Produzido por Matheus Ruivo!')
print('Insira seus produtos, fazemos a soma!')
print('Carregando Sistema...')
pro1 = float(input("Qual é o preço do produto??"))
pro2 = float(input("Qual é o preço do segundo produto??"))
print("Carrgando...")
somando1 = pro1 + pro2
print(f"O preço do produto um e dois somando fica {somando1:.2f}")
pro3 = float(input("Qual é o preço do terceiro produto??"))
somando2 = somando1 + pro3
print(f'Somando os três fica {somando2:.2f}.')

