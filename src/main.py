from sistemaEspecialista import *

def main() -> None:
    # ============== TESTE ===========================
    # transito = "baixo"
    # horario = 12
    # dia = 12
    # mes = 5
    # tempo = 12 #Min
    # feriado = False
    # clima = Clima.ENSOLARADO
    # distribuidora = {"A": 12, "B": 24, "C": 6, "D": 36}
    # distKey = "B"

    # TODO - alterar para identificar o estado do transito pelo horario 
    transito = str(input("Por obsequio entre com o estado do transito no momento <baixo, medio, alto>: "))
    horario = int(input("Por obsequio entre com o horario da entrega (apenas a parte inteira): "))
    dia = int(input("Por obsequio entre com o dia da entrega: "))
    mes = int(input("Por obsequio entre com o mes da entrega: "))
    tempo = int(input("Por obsequio entre com o tempo da entrega (min): "))
    feriado = str(input("Informe se o dia da entrega é feriado <S/N>: "))
    
    # TODO input do clima 
    clima = Clima.ENSOLARADO

    distribuidora = {}  
    while len(distribuidora) < 5:
        dist = input("Informe o local de distribuição: ")
        distancia = int(input("Entre com o distancia (m) da distribuidora até o local de entrega: "))
        distribuidora[dist] = distancia
    
    distKey = str(input("Informe a distribuidora a qual deseja verificar: "))
    
    feriado = True if feriado.upper() == "S" else False       
    SistemaEspecialista(transito, 
                        horario, dia, mes, 
                        tempo, feriado, clima, 
                        distribuidora, distKey)

if __name__ == "__main__":
    main()
