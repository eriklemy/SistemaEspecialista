from sistemaEspecialista import *

def main() -> None:
    distancia = int(input("Por obsequio entre com a distancia até o local de entrega (km): "))
    hora = int(input("Diga o horario em que será realizada a entrega: "))
    min = int(input("Diga o minuto em que será realizada a entrega: "))
    
    print("Qual a previsão de clima para o dia/hora")
    print("\t<1> TEMPO BOM\n\
        <2> TEMPO MODERADO\n\
        <3> TEMPO RUIM")

    clima = int(input("Diga o estado climatico: "))
    transito_bloqueado = str(input("O transito está bloqueado na região proxima ao evento (S/n)? "))
    is_evento = str(input("Há evento ocorrendo (S/n)? "))

    regiao_transito_bloqueada = True if transito_bloqueado.upper() == "S" else False 
    evento = True if is_evento.upper() == "S" else False 
    
    SistemaEspecialista(distancia, 
                        hora, min, clima,
                        regiao_transito_bloqueada, evento)
    
if __name__ == "__main__":
    main()
