""" 
    RPLM - SISTEMA ESPECIALISTA
        Erick Lemmy dos Santos Oliveira 
        Guilherme Janke
"""
from sistemaEspecialista import *
def menu() -> None:
    print("SISTEMA ESPECIALISTA EM PREVISÃO DE TEMPO DE ENTREGA")
    print("="*75)
    print("REGRAS: ")
    print("\t0 <= horario <= 23:59hrs")
    print("\tdistancia da distribuidora até o comercio (km)")
    print("\tHorarios: ")
    print("\t\tMadrugueiro (00:00 até 04:59)")
    print("\t\tFora de Pico (09:00 até 16:59 E 20:01 até 23:59)")
    print("\t\tProximo de Pico (05:00 até 06:59 E 17:00 até 18:59)")
    print("\t\tPico (07:00 até 08:59 E 19:00 até 20:59)")
    print("="*75)
def main() -> None:
    menu()

    distancia = float(input("INFORME A DISTANCIA ATÉ O LOCAL DE ENTREGA (Km): "))
    horario = str(input("INFORME O HORARIO EM QUE SERÁ REALIZADA A ENTREGA (HH:mm): "))

    print("INFORME A PREVISÃO DO CLIMA PARA DIA/HORA DA ENTREGA: ")
    print("<1> TEMPO BOM\n<2> TEMPO RUIM\n<3> TEMPO PESSIMO")

    clima = int(input("ENTRE COM O ESTADO CLIMATICO: "))
    is_evento = str(input("INFORME SE HÁ OCORRENCIA DE EVENTOS NA REGIÃO (S/n)? "))
    evento = True if is_evento.upper() == "S" else False 
   
    if (evento):
        transito_bloqueado = str(input("O TRANSITO ESTÁ BLOQUEADO NA REGIÃO PROXIMA AO EVENTO (S/n)? "))
        regiao_transito_bloqueada = True if transito_bloqueado.upper() == "S" else False 
        SistemaEspecialista(distancia, horario, clima, evento, regiao_transito_bloqueada)
    else:
        SistemaEspecialista(distancia, horario, clima, evento)

if __name__ == "__main__":
    main()
