from enum import Enum

class Clima(Enum): 
    CHUVA_LEVE, CHUVA_MODERADA, ENSOLARADO, NUBLADO, TEMPESTADE, NEBLINA = range(6)


def tempo_deslocamento(distancia: int) -> int:
    if distancia <= 15:
        return 2 * distancia
    else: return 3 * distancia 

def fluxo_horario(hora: int, min: int) -> str:
    if (0 <= hora < 24) and (0 <= min <= 59):
        if hora in [6, 7, 8, 17, 18, 19]:
            return "pico"
        elif hora in [23, 0, 1, 2, 3, 4]:
            return "madrugueiro"
        elif hora in [5, 16, 20]:
            return "proximo pico"
        else:
            return "fora de pico"
    else: return "invalido"

def get_clima(clima: int):
    return Clima(clima - 1)

def SistemaEspecialista(distancia: int, hora: int , min: int, clima: int, regiao_transito_bloqueada: bool, evento: bool) -> None:	
    t_deslocamento = tempo_deslocamento(distancia)

    if fluxo_horario(hora, min) != "invalido":

        if (fluxo_horario(hora, min) == "madrugueiro" and get_clima(clima) == Clima.ENSOLARADO):        
            print("INPUT DE CLIMA INVALIDA PARA O HORARIO")

        if (fluxo_horario(hora, min) == "madrugueiro") and get_clima(clima) == (Clima.CHUVA_LEVE or Clima.NEBLINA):
            t_deslocamento *= 0.8

        if (fluxo_horario(hora, min) == "fora de pico") and get_clima(clima) == (Clima.ENSOLARADO or Clima.CHUVA_LEVE):
            t_deslocamento *= 1.0

        if (fluxo_horario(hora, min) == "proximo pico") and get_clima(clima) == (Clima.ENSOLARADO or Clima.CHUVA_LEVE):
            t_deslocamento *= 1.5

        if (fluxo_horario(hora, min) == "pico") and get_clima(clima) == (Clima.ENSOLARADO or Clima.CHUVA_LEVE or Clima.NEBLINA):
            t_deslocamento *= 2.0

        if (fluxo_horario(hora, min) == "madrugueiro") and get_clima(clima) == (Clima.CHUVA_MODERADA or Clima.NUBLADO or Clima.NEBLINA):
            t_deslocamento *= 1

        if (fluxo_horario(hora, min) == "fora de pico") and get_clima(clima) == (Clima.CHUVA_MODERADA or Clima.NUBLADO):
            t_deslocamento *= 1.2

        if (fluxo_horario(hora, min) == "proximo pico") and get_clima(clima) == (Clima.CHUVA_MODERADA or Clima.NUBLADO):
            t_deslocamento *= 2.0

        if (fluxo_horario(hora, min) == "pico") and get_clima(clima) == (Clima.CHUVA_MODERADA or Clima.NUBLADO or Clima.NEBLINA):
            t_deslocamento *= 3
        
        if (fluxo_horario(hora, min) == "fora de pico") and get_clima(clima) == (Clima.TEMPESTADE):
            t_deslocamento *= 2.5

        if evento and not regiao_transito_bloqueada:
            t_deslocamento *= 5.0

        if (get_clima(clima) == Clima.TEMPESTADE) and (evento and regiao_transito_bloqueada):
            print("A entrega não sera realizada")
        else:
            print(f"O tempo medio de entrega é de {t_deslocamento} minutos")
    else:
        print("INPUT DE HORARIO INVALIDO")
