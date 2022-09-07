
class House:
    def __init__(self, parede, chao, teto, janela, porta):
        self.parede = parede
        self.chao = chao
        self.teto = teto
        self.janela = janela
        self.porta = porta
        
        
    def constroi_parede(self):
        return "{} em pé".format(self.parede)
    
    def piso_no_chao(self):
        return "{} colocado".format(self.chao)
    
    def pinta_teto(self):
        return "{} de branco".format(self.teto)
    
    def janela_com_iluminacao(self):
        return "{} fica onde entra sol".format(self.janela)
    
    def porta_com_acesso(self):    
        return "Deixar {} acessível".format(self.porta)
        
comodo_padrao = House('Parede branca', 'Chão de madeira','Teto pintado', 
                      'Janela de madeira','Porta de Madeira')

print("----------Cômodo Padrão----------")

print(comodo_padrao.constroi_parede(),'\n',comodo_padrao.piso_no_chao(),'\n',
      comodo_padrao.pinta_teto(),'\n',comodo_padrao.janela_com_iluminacao(),'\n',
      comodo_padrao.porta_com_acesso())


class Cozinha(House):
    def __init__(self, parede, chao, teto, janela, porta, pia, torneira):
        self.pia = pia
        self.torneira = torneira
        super().__init__(parede, chao, teto, janela, porta)
        
    def pia_marmore(self, cor):
        print("A cor da pia é {}".format(cor))
        if cor == "Preto":
            return "Fica mais chic"
        else:
            return "Fica a gosto do cliente"    
        
    def torneira_pia(self):
        if self.torneira == "Aquecida":
            return "Torneira {} é só vantagens".format(self.torneira)
        else:
            return "Vai lavar louça no frio"

   

comodo1 = Cozinha('Parede sem azulejo', 'Chão de piso frio','Teto pintado', 
                  'Janela de madeira','Porta de Madeira', 'Preto', 'Aquecida')
print("---------- Cozinha----------")
print(comodo1.pia_marmore('Preto'),'\n',
      comodo1.torneira_pia(), '\n',
      comodo1.constroi_parede(),'\n',
      comodo1.piso_no_chao(),'\n',
      comodo1.pinta_teto(),'\n',
      comodo1.janela_com_iluminacao(),'\n',
      comodo1.porta_com_acesso())
      
      
class Banheiro(House):
    def __init__(self, parede, chao, teto, janela, porta, cuba, sanitario):
        self.cuba = cuba
        self.sanitario = sanitario
        super().__init__(parede, chao, teto, janela, porta)     
        
    def cuba_banheiro(self, transparente):
        if transparente == 'Sim':
            print('Cuba transparente é bonita, porém difícil de limpar')
        else:
            print('Avaliar')  
        return transparente
    
    def vaso_sanitario(self):
        return "O vaso deve ser preto"
           
    def __cofre_secreto(self):
        return 'Acesso liberado: Contém segredo de família' 
        
    def tentando_acessar(self, pessoa):
        if pessoa == "Morador" or pessoa == "Proprietário":
            return self.__cofre_secreto()
        else:
            return "Você não tem permissão para acessar esse local! Saia daqui!"
        
print("---------- Banheiro----------")       
 
comodo2 = Banheiro('Parede sem azulejo', 'Chão de piso frio','Teto pintado', 
                  'Janela de alumínio','Porta de madeira pintada', 'Sim', 'Vaso sanitário')

acesso = comodo2.tentando_acessar('Corretor')
print(acesso)

print(comodo2.cuba_banheiro('Sim'),'\n',
      comodo2.vaso_sanitario(), '\n',
      comodo2.constroi_parede(),'\n',
      comodo2.piso_no_chao(),'\n',
      comodo2.pinta_teto(),'\n',
      comodo2.janela_com_iluminacao(),'\n',
      comodo2.porta_com_acesso())       

acesso = comodo2.tentando_acessar('Morador')
print(acesso)    


class Sala:
    def __init__(self):
        pass
    
    def formacao_sala():
        return "A gosto do cliente"
    
class Moveis(Sala):
    def __init__(self, cores):
        self.cores = cores
        super().__init__()
        
    def movel(self):
        return "A cor {} devem ornar com o restante da casa.".format(self.cores)

print("---------- Sala ----------")       
comodo3 = Moveis("Azul")  
print(comodo3.movel()) 


class AreaCasa():
    def __init__(self, lateral, base):
        self.lateral = lateral
        self.base = base
    
    def area_comodo(self):
        return self.base * self.lateral
    
    def area_total(self):
        return self.base * self.lateral * 3
    
calculo = AreaCasa(3,2)
calculo.area_comodo()
calculo.area_total()