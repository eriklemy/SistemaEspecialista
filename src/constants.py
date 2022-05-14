from enum import Enum, auto

class Regioes(Enum):
    NORTE = auto()
    NORDESTE = auto()
    SUL = auto()
    SUDESTE = auto()
    CENTRO_OESTE = auto()

class Clima(Enum): 
    CHUVA_LEVE, CHUVA_MODERADA, ENSOLARADO, NUBLADO, TEMPESTADE, NEBLINA = range(6)

class Estacoes(Enum):
    OUTONO = auto()
    INVERNO = auto()
    PRIMAVERA = auto()
    VERAO = auto()

DIASMES = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr":30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dez": 31}
