funcionario = {"nome":"Adalmando", "cargo":"dev", "salario":2000}

def ver_funcionario(funcionario):
    print(f"O funcionário {funcionario['nome']} trabalha como {funcionario['cargo']} e recebe R$ {funcionario['salario']},00.")

def mostrar_salario(funcionario):
    print(f"R$ {funcionario['salario']},00")

def atualizar_salario(funcionario, novo_valor):
    funcionario['salario'] = novo_valor

atualizar_salario(funcionario, 4000)
mostrar_salario(funcionario=funcionario)