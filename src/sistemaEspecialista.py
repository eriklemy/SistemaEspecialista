from enum import Enum, auto

class Regioes(Enum):
    NORTE = auto()
    NORDESTE = auto()
    SUL = auto()
    SUDESTE = auto()
    CENTRO_OESTE = auto()

class Clima(Enum): 
    CHUVA_LEVE = auto()
    CHUVA_MODERADA = auto()
    ENSOLARADO = auto()
    NUBLADO = auto()
    TEMPESTADE = auto()
    NEBLINA = auto()
  
class Estacoes(Enum):
    OUTONO = auto()
    INVERNO = auto()
    PRIMAVERA = auto()
    VERAO = auto()

DIASMES = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr":30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dez": 31}

# ============== TESTE ===========================
horario = 12
dia = 12
distribuidora = {"A": 12, "B": 24, "C": 6, "D": 36}
clima = Clima.ENSOLARADO
transito = "baixo"
tempo = 12 #Min
distancia = 28
feriado = False

def TUDOABAIXO():	
    if ((transito == "baixo") or (transito == "medio")) and (tempo < 2*distribuidora["B"]):
        if (tempo == "chuva-moderada") or (tempo == "tempestade"):  
            return print("Entrega em tempo")
        else:
            return print("A entrega ira potencialmente atrasar")

    elif (((dia < DIASMES["May"])) and (feriado == True)) and ((clima == Clima.CHUVA_LEVE) or (clima == Clima.TEMPESTADE)):
        if (Clima.CHUVA_LEVE or Clima.CHUVA_MODERADA) is clima:
            return print("A entrega ira potencialmente atrasar na(s) regiao X")
        else: 
            return print("A entrega ira chegar dentro do tempo esperado")

    elif ((dia <= DIASMES["May"]) and (feriado == False)) and ((clima == Clima.ENSOLARADO) and (tempo < 2*distribuidora["B"])):
        if clima in [Clima.TEMPESTADE, Clima.CHUVA_MODERADA]:
            return print("A entrega ira potencialmente atrasar na(s) região X")
        else:
            return print(f"A entrega ira chegar dentro do tempo esperado para {distribuidora[2]}")
 
    else: print("Erro")
    # if distruidora > 1: 
    #     return min(distribuidoras)


if ((horario < 24 and dia <= 31)): # == "Comercial"
    if len(distribuidora) > 5: 
        print("MUITOS GRUPOS")
    else:
        TUDOABAIXO() 
