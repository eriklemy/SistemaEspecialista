from dis import dis
from constants import *

def comercialDay(distribuidora: list, horario: int, dia: int) -> bool:
    return ((0 < horario < 24) and (1 <= dia <= 31)) and len(distribuidora) < 5

def SistemaEspecialista(transito: str, horario: int, dia: int, mes: int, tempo: str, feriado: bool, clima: Clima, distribuidora: list, distKey: str) -> None:	
    if not comercialDay(distribuidora, horario, dia):
        print("DIA NÃO COMERCIAL - A ENTREGA NÃO SERA REALIZADA")
    else:
        if ((transito == "baixo") or (transito == "medio")) and (tempo < 2*distribuidora[distKey]):
            if (tempo == "chuva-moderada") or (tempo == "tempestade"):  
                print("Entrega em tempo")
            else:
                print("A entrega ira potencialmente atrasar")

        elif (((dia < DIASMES[mes])) and (feriado == True)) and ((clima == Clima.CHUVA_LEVE) or (clima == Clima.TEMPESTADE)):
            if (Clima.CHUVA_LEVE or Clima.CHUVA_MODERADA) is clima:
                print("A entrega ira potencialmente atrasar na(s) regiao X")
            else: 
                print("A entrega ira chegar dentro do tempo esperado")

        elif ((dia <= DIASMES[mes]) and (feriado == False)) and ((clima == Clima.ENSOLARADO) and (tempo < 2*distribuidora[distKey])):
            if clima in [Clima.TEMPESTADE, Clima.CHUVA_MODERADA]:
                print("A entrega ira potencialmente atrasar na(s) região X")
            else:
                print(f"A entrega ira chegar dentro do tempo esperado para {distribuidora[distKey]}")
    
        else: print("Erro")
  
