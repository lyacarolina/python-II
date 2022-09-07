from construindo_casa_poo import AreaCasa

def main():
    calculo = AreaCasa(3,2)
    print("A área de cada cômodo é de {} m².".format(calculo.area_comodo()))
    print("A área total da casa é de {} m².".format(calculo.area_total()))
      
main()