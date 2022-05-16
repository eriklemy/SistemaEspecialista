from enum import Enum, auto

class Clima_Tempo(Enum):
    TEMPO_BOM, TEMPO_RUIM, TEMPO_PESSIMO = range(3)

class EstadoTransito(Enum): 
    PICO = "pico", 
    MADRUGUEIRO = "madrugueiro"
    PROXIMO_PICO = "proximo de pico" 
    FORA_PICO = "fora de pico"
    INVALIDO = auto()

def tempo_deslocamento(distancia: int) -> float:
    if distancia <= 15:
        return 2 * distancia
    else: return 3 * distancia 

def fluxo_horario(horario: str) -> EstadoTransito:
    hora, min = horario.split(":")
    print(int(hora), min)

    if (0 <= int(hora) < 24) and (0 <= int(min) <= 59):
        if int(hora) in [7, 8, 19, 20]:
            return EstadoTransito.PICO
        elif int(hora) in [23, 0, 1, 2, 3, 4]:
            return EstadoTransito.MADRUGUEIRO
        elif int(hora) in [5, 6, 17, 18]:
            return EstadoTransito.PROXIMO_PICO
        else:
            return EstadoTransito.FORA_PICO
    else: return EstadoTransito.INVALIDO

def get_clima(tempo: int) -> Clima_Tempo:
    return Clima_Tempo(tempo - 1)

def SistemaEspecialista(distancia: int, horario: str, tempo: int, evento: bool, regiao_transito_bloqueada: bool = False) -> None:	
    t_deslocamento = tempo_deslocamento(distancia)
    print(get_clima(tempo))
    print(fluxo_horario(horario))

    if fluxo_horario(horario) != EstadoTransito.INVALIDO:

        if (fluxo_horario(horario) == EstadoTransito.MADRUGUEIRO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 0.8

        if (fluxo_horario(horario) == EstadoTransito.FORA_PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 1.0

        if (fluxo_horario(horario) == EstadoTransito.PROXIMO_PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 1.5

        if (fluxo_horario(horario) == EstadoTransito.PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_BOM):
            t_deslocamento *= 2.0

        if (fluxo_horario(horario) == EstadoTransito.MADRUGUEIRO) and get_clima(tempo) == Clima_Tempo.TEMPO_RUIM:
            t_deslocamento *= 1

        if (fluxo_horario(horario) == EstadoTransito.FORA_PICO) and get_clima(tempo) == Clima_Tempo.TEMPO_RUIM:
            t_deslocamento *= 1.2

        if (fluxo_horario(horario) == EstadoTransito.PROXIMO_PICO) and get_clima(tempo) == Clima_Tempo.TEMPO_RUIM:
            t_deslocamento *= 2.0

        if (fluxo_horario(horario) == EstadoTransito.PICO) and get_clima(tempo) == Clima_Tempo.TEMPO_RUIM:
            t_deslocamento *= 3
        
        if (fluxo_horario(horario) == EstadoTransito.FORA_PICO) and get_clima(tempo) == (Clima_Tempo.TEMPO_PESSIMO):
            t_deslocamento *= 2.5

        print("="*90)
        if evento and not regiao_transito_bloqueada:
            t_deslocamento *= 5.0
            print("A ENTREGA IRÁ DEMORAR MAIS DEVIDO HÁ OCORRENCIA DE EVENTO, PORTANTO ")

        if (get_clima(tempo) == Clima_Tempo.TEMPO_PESSIMO) and (evento and regiao_transito_bloqueada):
            print("A ENTREGA NÃO SERÁ REALIZADA POIS HÁ OCORRENCIA DE EVENTO E AS RUAS ESTÃO BLOQUEADAS!!")
        else:
            print(f"O TEMPO MEDIO DE ENTREGA É DE {t_deslocamento} MINUTOS!!")
    else:
        print("INPUT DE HORARIO INVALIDO!!")
