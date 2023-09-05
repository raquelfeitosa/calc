class Calculadora:
    area_paredes: float  #variaveis usadas no self litragem necessaria
    area_teto: float

#abaixos são criados os métodos
    def calcular_area_paredes(self ,largura, profundidade, altura):
        self.area_paredes= 2 * (largura + profundidade)* altura
        return self.area_paredes
    
    def calcular_area_teto(self, largura, profundidade):
        self.area_teto= largura * profundidade
        return self.area_teto 
    def calcular_litragem_necessaria(self): #Nao recebe parâmetro pq ela precisa dos valores finais do cal
        return(self.area_paredes + self.area_teto) / 10