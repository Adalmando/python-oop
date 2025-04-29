class Numeros(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def somar_com_outro_numero(self, num3):
        self.soma = num3 + self.num1 + self.num2
        print(self.soma)

    def mostrar_soma(self):
        return self.soma
    
    def mostar_num1(self):
        print(self.num1)

    def mostar_num2(self):
        print(self.num2)    


teste = Numeros(num1=30, num2=20)
teste.somar_com_outro_numero(50)
print(teste.mostrar_soma())