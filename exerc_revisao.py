'''#exerc_1
class Pessoa:
    def __init__(self, cpf, nome, idade, fumante):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.fumante = fumante
        
    def pessoa_nome(self):
        return "Nome da pessoa: {}".format(self.nome)
        
    def fumante_ou_nao(self):
        if self.fumante == 'N':
            return "Não fumante"
        else:
            return "Fumante"
    
    
pessoa1 = Pessoa('12345678900',
                 'João da Silva',
                 '25', 
                 'N')
print(pessoa1.pessoa_nome())
print(pessoa1.fumante_ou_nao())

#exerc_2

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade, estado_civil):
        self.estado_civil = estado_civil
        
    def situacao(self):
        if self.estado_civil == 'S':
            return "Solteiro"
        elif self.estado_civil == 'C':
            return "Casado"  
        else:
            return "Não informado"
        
pessoa2 = PessoaFisica('98765432100', 'Maria', '55', 'C')
print(pessoa2.situacao())

#exerc_3

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome, idade, ativo):
        self.cnpj = cnpj
        self.ativo = ativo
        
    def empresa_nome(self):
        return "CNPJ: {}".format(self.cnpj)
        
    def atividade(self):
        if self.ativo == 'S':
            return "CNPJ ATIVO" 
        else:
            return "CNPJ INATIVO"
        
pj = PessoaJuridica('12123456000199', 'ArcoIris LTDA', '10', 'S')
print(pj.empresa_nome())
print(pj.atividade())'''

#exerc_4

'''class Professor: 
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
print(acesso)'''


#exerc_5


class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
        
    def perimetro(self):
        return 4 * self.lado
    
calculo = Quadrado(3)
calculo.perimetro()
calculo.area()
