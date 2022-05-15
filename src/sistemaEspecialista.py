from enum import Enum, auto
from glob import escape

# class Clima(Enum): 
#     CHUVA_LEVE, CHUVA_MODERADA, ENSOLARADO, NUBLADO, TEMPESTADE, NEBLINA = range(6)

class Clima_Tempo(Enum):
    TEMPO_BOM, TEMPO_MODERADO, TEMPO_RUIM = range(3)

class EstadoTransito(Enum): 
    PICO = "pico", 
    MADRUGUEIRO = "madrugueiro"
    PROXIMO_PICO = "proximo pico" 
    FORA_PICO = "fora de pico"
    INVALIDO = auto()

def tempo_deslocamento(distancia: int) -> float:
    if distancia <= 15:
        return 2 * distancia
    else: return 3 * distancia 

def fluxo_horario(hora: int, min: int) -> EstadoTransito:
    if (0 <= hora < 24) and (0 <= min <= 59):
        if hora in [6, 7, 8, 17, 18, 19]:
            return EstadoTransito.PICO
        elif hora in [23, 0, 1, 2, 3, 4]:
            return EstadoTransito.MADRUGUEIRO
        elif hora in [5, 16, 20]:
            return EstadoTransito.PROXIMO_PICO
        else:
            return EstadoTransito.FORA_PICO
    else: 
        return EstadoTransito.INVALIDO

def get_clima(tempo: int) -> Clima_Tempo:
    return Clima_Tempo(tempo - 1)

def SistemaEspecialista(distancia: int, hora: int , min: int, tempo: int, regiao_transito_bloqueada: bool, evento: bool) -> None:	
    t_deslocamento = tempo_deslocamento(distancia)

    if fluxo_horario(hora, min) != EstadoTransito.INVALIDO:

        if (fluxo_horario(hora, min) == EstadoTransito.MADRUGUEIRO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 0.8

        if (fluxo_horario(hora, min) == EstadoTransito.FORA_PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 1.0

        if (fluxo_horario(hora, min) == EstadoTransito.PROXIMO_PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 1.5

        if (fluxo_horario(hora, min) == EstadoTransito.PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 2.0

        if (fluxo_horario(hora, min) == EstadoTransito.MADRUGUEIRO) and get_clima(tempo) == Clima_Tempo.TEMPO_MODERADO:
            t_deslocamento *= 1

        if (fluxo_horario(hora, min) == EstadoTransito.FORA_PICO) and get_clima(tempo) == Clima_Tempo.TEMPO_MODERADO:
            t_deslocamento *= 1.2

        if (fluxo_horario(hora, min) == EstadoTransito.PROXIMO_PICO) and get_clima(tempo) == Clima_Tempo.TEMPO_MODERADO:
            t_deslocamento *= 2.0

        if (fluxo_horario(hora, min) == EstadoTransito.PICO) and get_clima(tempo) == Clima_Tempo.TEMPO_MODERADO:
            t_deslocamento *= 3
        
        if (fluxo_horario(hora, min) == EstadoTransito.FORA_PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_RUIM):
            t_deslocamento *= 2.5

        if evento and not regiao_transito_bloqueada:
            t_deslocamento *= 5.0

        if (get_clima(tempo) == Clima_Tempo.TEMPO_RUIM) and (evento and regiao_transito_bloqueada):
            print("A entrega não sera realizada")
        else:
            print(f"O tempo medio de entrega é de {t_deslocamento} minutos")
    else:
        print("INPUT DE HORARIO INVALIDO")
