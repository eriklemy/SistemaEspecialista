from sistemaEspecialista import *

def main() -> None:
    # ============== TESTE ===========================
    transito = "baixo"
    dia = 12
    horario = 12
    distribuidora = {"A": 12, "B": 24, "C": 6, "D": 36}
    clima = Clima.ENSOLARADO
    transito = "baixo"
    tempo = 12 #Min
    feriado = False
    mes = 5
    distKey = "B"
    SistemaEspecialista(transito, 
                        horario, dia, mes, 
                        tempo, feriado, clima, distribuidora, distKey)

if __name__ == "__main__":
    main()
