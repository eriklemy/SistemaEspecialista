### Sistema Especialista em Distribuição de (alguma coisa - provavelmente CERVEJA)

Controla os pontos de distribuição de através de fatores, como:
    
- dia?
- clima? 
- horario?
- epoca do ano?
- feriado?
- grupo ao qual sera distribuido? (pequeno ou grande comercio)
- Região?
- distancia

Com estas informações há como objetivo identificar o grau de probabilidade de uma entrega ser efetuada em tempo, bem como se o volume ao qual sera vendido proporcionara maior rendimento a empresa

#### Exemplo:
Eventos:
- Sera entregue a comercios mais proximos ao evento como exemplos:
    - Jogos 
    - Eventos de Corrida 
    - Teatros
    - Shows musicais

Previsão do tempo:
- se chover sera entregue a comercios mais proximos a distribuidora devido a possibilidade de aumentar o volume de veiculos nas vias

Feriado:
- Alto fluxo rodoviario, então tem maior concentração de veiculos, resultando em tempos mais longos de entrega.

---

Regras:

- dias do mes <= 31, se mes > 30 -> usar 30
- horario não superior a 24hrs
- feriado local não conta 
- grupo a ser distribuido (max = 5 prototipo)
- distancia da distribuidora até o comercio (max = 5)
- regiões permitidas [NORTE, NORDESTE, SUL, SUDESTE, CENTRO-OESTE) da distribuidora
- climas permitidos [CHUVA LEVE, CHUVA MODERADA, ENSOLARADO, NUBLADO, TEMPESTADE, NEBLINA]  
- epoca do ano dentro das 4 estações [OUTONO, INVERNO, PRIMAVERA, VERÃO] 

- Regras de multiplicador
    - para horario madrugueiro o multiplicador é 0,8
    - para transito fora de pico o multiplicador é de 1 
    - pra transito moderado próximo a horário de pico (tanto para mais ou para menos do horário) o multiplicador é 1,5
    - para horário de pico o multiplicador é 2
    - para horario madrugueiro com chuva o multiplicador é 1
    - para horario fora de pico em dia de chuva multiplicador 1,2
    - para horario próximo de pico com chuva o multiplicador é 2
    - para horario de pico com chuva o multiplicador é 3
- Para distancia de até 10 Km os multiplicadores se mantem os mesmos, para distancias maiores os multiplicadores sofrem um acréscimo de 2%(dois porcento) acada 3 Km a mais na distancia percorrida.

<pre>

TODO: ATRIBUIR OS MULTIPLICADORES PARA DETERMINAR SE CHEGARA EM TEMPO OU NÃO
TODO: CONSIDERAR REALIZAR A MEDIANA COM TODOS OS RESULTADOS PARA UM PARAMETRO MAIS PROXIMO AO IDEAL (SERA VERIFICADO NA IMPLEMENTAÇÃO)

SE ((horario E dia) => "Comercial") ENTÃO {
    SE grupos > 5 ENTAO { 
        show MUITOS GRUPOS
        exit() 
    SENAO SE
        TUDOABAIXO 
    SENAO 
	  Return 
}

@TUDOABAIXO	
SE ((transito == "baixo") OU (transito == "medio")) E ((tempo <=> 2*distancia) PARA distruidoraX) ENTÃO {
    SE (tempo == "chuva-moderada") OU (tempo == "tempestade"))  
        Resultado => "Entrega em tempo"
    SENAO 
        Resultado => "A entrega ira potencialmente atrasar"
}

SE (((dia <= 31) E (diasMes < 31)) E (feriado == V)) E ((clima == "chuva-moderada") OU (clima == "tempestade")) ENTÃO {
    SE "chovendo" EM ("Sul", "Norte, "Sudeste, "Nordeste, "Centro-Oeste")
        Resultado => "A entrega ira potencialmente atrasar na(s) região(ões) X
    SENAO 
        Resultado => "A entrega ira chegar dentro do tempo esperado"
}

SE (((dia <= 31) E (diasMes < 31)) E (feriado == F)) E (((clima == "ensolarado") E (tempo <=> 2*distancia)) ENTÃO {
    SE "chovendo" EM ("Sul", "Norte, "Sudeste, "Nordeste, "Centro-Oeste")
        Resultado => "A entrega ira potencialmente atrasar na(s) região(ões) X
    SENAO 
        Resultado => "A entrega ira chegar dentro do tempo esperado"
}

FINAL -> SE distruidoras > 1 ENTÃO 
    resultado => deve ser entregue para [menorDistancia(distribuidoras)]

</pre>




--- 
### Sistema Especialista em jogo do bixo 

Busca identificar se a jogada usada tem a possibilidade de vencer através de fatores como:
- dia 
- soma do dia
- numero de grupos
- grupos escolhidos 
- dezena
- centena 
- milhar
    - horarios?
    - animal?
    - grupo?

Para isso é necessario ter:
- [ ] soma do dia calculada (e/ou o dia que sera jogado para realização do calculo).
- [ ] grupos gerados com base na soma.
- [ ] O bixo do dia. 

Desta forma é possivel obter um conjunto de dezenas, centenas e milhares em potencial resultando na diminuição do numero de grupos e aumentando a chance de vitoria 

- Estatisticas de jogos com valores mais sorteados e mais atrasados também podem ser usados para analise e concepção  