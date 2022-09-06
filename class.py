class HogwartsHouse:
    def __init__(self, name, color, founder):
        self.name = name
        self.color = color
        self.founder = founder
        
        
    def get_points_house(self):
        return "A casa {} possui 100 pontos".format(self.name)
    
    def play_quidditch(self):
        return "A pontuação do quadribol foi de 10 pontos"
    
ravenclaw = HogwartsHouse('Corvinal',
                          'Azul e Preto',
                          'Ravena Corvinal')

points_house = ravenclaw.get_points_house()
print('Pontuação = {}'.format(points_house))
