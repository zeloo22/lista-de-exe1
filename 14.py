print("BEM VINDO JOAO PAPO-DE-PESCADOR, HOMEM DE BEM")
peso = float(input("qual e o peso da sua pesca de hoje ? "))
if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
    print("poxa JOAO PAPO-DE-PESCADOR voce passou do limite :(")
    print(f"Como voce exedeu o limite em {excesso:.2f} quilos, voce tera q pagar {multa:.2f} reais")
else:
    print("Parabens JOAO HOMEM DE BEM voce seguiu o regulamento")
    print("Sem multas pra voce hj")