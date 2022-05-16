""" 
    RPLM - SISTEMA ESPECIALISTA
        Erick Lemmy dos Santos Oliveira 
        Guilherme Janke
"""
from sistemaEspecialista import *

def main() -> None:
    print("SISTEMA ESPECIALISTA EM PREVISÃO DE TEMPO DE ENTREGA")
    print("REGRAS: ")
    print("\t0 <= horario <= 23:59hrs")
    print("\tdistancia da distribuidora até o comercio (km)")
    
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
