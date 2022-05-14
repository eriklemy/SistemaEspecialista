from sistemaEspecialista import *

def main() -> None:
    distancia = int(input("Por obsequio entre com a distancia até o local de entrega (km): "))
    hora = int(input("Diga o horario em que será realizada a entrega: "))
    min = int(input("Diga o minuto em que será realizada a entrega: "))
    
    print("Qual a previsão de clima para o dia/hora")
    print("\t<1> CHUVA_LEVE\n\
        <2> CHUVA_MODERADA\n\
        <3> ENSOLARADO\n\
        <4> NUBLADO\n\
        <5> TEMPESTADE\n\
        <6> NEBLINA")

    clima = int(input("Diga o estado climatico: "))
    is_regiao_transito_bloqueado = str(input("O transito está bloqueado (S/n)? "))
    is_evento = str(input("Há evento ocorrendo (S/n)? "))

    regiao_transito_bloqueada = True if is_regiao_transito_bloqueado.upper() == "S" else False 
    evento = True if is_evento.upper() == "S" else False 
    
    SistemaEspecialista(distancia, 
                        hora, min, clima,
                        regiao_transito_bloqueada, evento)
    
if __name__ == "__main__":
    main()
