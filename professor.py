#exerc_4
class Professor: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def salario(self):
        return 'R$ 1.500' 
        
    def tentando_acessar(self, pessoa):
        if pessoa == "Diretor" or pessoa == "Coordenador":
            return self.salario()
        else:
            return "Você não tem permissão para acessar essa informação"
        
usuario = Professor('José', '15')
acesso = usuario.tentando_acessar("Aluno")
print(acesso)
acesso = usuario.tentando_acessar("Diretor")
print(acesso)