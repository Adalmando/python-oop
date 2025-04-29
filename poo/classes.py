class Funcionario(object):
    
    def __init__(self, nome, cargo, salario):
        self.nome       = nome
        self.cargo      = cargo
        self.salario    = salario

    def mostrar_salario(self):
        print("[+] teu salário eh {0}".format(self.salario))

    def atualizar_salario(self, novo_salario):
        self.salario = novo_salario

    def mostrar_funcionario(self):
        print(f"O funcioario {self.nome}, trabalha como {self.cargo} recebendo o salário de R$ {self.salario}")

func1 = Funcionario("Adalmando", "programador", 2500)

func1.mostrar_funcionario()
func1.atualizar_salario(6000)
func1.mostrar_salario()

func1.mostrar_funcionario()