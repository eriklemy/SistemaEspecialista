from sistemaEspecialista import *

def main() -> None:
    distancia = int(input("Por obsequio entre com a distancia até o local de entrega (km): "))
    horario = str(input("Diga o horario em que será realizada a entrega (HH:mm): "))

    print("Qual a previsão de clima para o dia/hora")
    print("\t<1> TEMPO BOM\n\
        <2> TEMPO RUIM\n\
        <3> TEMPO PESSIMO")

    clima = int(input("Diga o estado climatico: "))
    is_evento = str(input("Há evento ocorrendo (S/n)? "))
    evento = True if is_evento.upper() == "S" else False 
   
    if (evento):
        transito_bloqueado = str(input("O transito está bloqueado na região proxima ao evento (S/n)? "))
        regiao_transito_bloqueada = True if transito_bloqueado.upper() == "S" else False 
        SistemaEspecialista(distancia, horario, clima, evento, regiao_transito_bloqueada)
    else:
        SistemaEspecialista(distancia, horario, clima, evento)

if __name__ == "__main__":
    main()
