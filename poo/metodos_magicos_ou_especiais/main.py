class Funcionario():

    # Método construtor, chamado sempre que uma instancia de Funcionario for criada
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    # Método toString, quando chamo o f1 = Funcionario() ->  print(f1) é esse método que será retornado mostrando 
    # os dados do Funcionario da forma que eu organizar aqui
    def __str__(self):
        return ("[+] Funcionario {0} trabalha em {1} com {2} de salário".format(self.nome, self.cargo, self.salario))
    
f1 = Funcionario("Adalmando", "Dev", 2000)
print(f1)