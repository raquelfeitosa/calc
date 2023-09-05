from calculadora import Calculadora

calc = Calculadora()

largura: float = float(input("Qual a largura do cômodo? "))
profundidade: float = float(input("Qual a profundidade do coômodo?"))
altura : float = 2.9

# calc.area_paredes: float = 2 * (largura + profundidade) * altura

#Eu posso colocar com dois ('' ou "")

print( "A área das paredes é : " , 
      calc.calcular_area_paredes(largura, profundidade, altura))

#calc.area_teto: float = largura * profundidade

print(
    'A área do teto é:',
    calc.calcular_area_teto(largura, profundidade) #método
)

print(
    'A litragem necessaria de tinta é:',
     calc.calcular_litragem_necessaria() #método
)