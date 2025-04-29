class Pessoa():
    quantidade_pessoas = 0
    def __init__(self, nome, idade):            
        self.nome = nome
        self.idade = idade
        Pessoa.quantidade_pessoas +=1 # Dessa forma a cada instancia de Pessoa que eu criar Pessopa.quantidade_pessoas vai saver o total de pessoas instanciadas globalmente

    def quantidade_pessoax(self):
        return Pessoa.quantidade_pessoas

p1 = Pessoa("Adalmando", 24)
p2 = Pessoa("Amanda", 27)
p3 = Pessoa("Nathalya", 19)
p4 = Pessoa("Francisca", 54)
p5 = Pessoa("Armando", 58)

print(p1.quantidade_pessoax()) # 5