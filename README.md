# Sistema Especialista

#### Integrantes:
- Erick Lemmy dos Santos Oliveira
- Guilherme Janke

### Sistema Especialista em Previsão de Tempo de Entrega

O sistema especialista em questão, irá identificar o tempo de entrega considerando fatores como: trânsito, clima, horários e eventos próximos ao local de entrega.

Preve tempo de entrega através de fatores, como:
- clima
- horario
- evento
- distancia

Com estas informações há como objetivo calcular e identificar o tempo medio para a realização da entregas por meio dos dados de entrada e dos multiplicadores com auxilio das inferências.

---

#### Exemplo:

- Eventos:
    - Entregue mais proximas a evento como exemplos:
        - Podem ser canceladas devido a bloqueios de acessos aos mesmos.
        - Terão atrasos caso não tenha os bloqueios.
- Previsão Climática :
    - Os fatores climáticos podem ou não ter interferência.
        - se chover a entrega terá atrasos devido a possibilidade de aumentar o volume de veículos nas vias.
        - A entrega em um dia ensolarado não terá atrasos devido ao clima.

---
#### Regras:

- 0 <= horario <= 23:59hrs 
- distancia da distribuidora até o comercio (km)
- climas permitidos [TEMPO BOM, TEMPO RUIM E TEMPO PESSIMO]  
- Regras de multiplicador
    - para horario madrugueiro o multiplicador é 0,8
    - para transito fora de pico o multiplicador é de 1 
    - pra transito moderado próximo a horário de pico (tanto para mais ou para menos do horário) o multiplicador é 1,5
    - para horário de pico o multiplicador é 2
    - para horario madrugueiro com tempo ruim o multiplicador é 1
    - para horario fora de pico em dia de tempo ruim multiplicador 1,2
    - para horario próximo de pico com tempo ruim o multiplicador é 2
    - para horario de pico com tempo ruim o multiplicador é 3
    - para horario fora de pico com tempo pessimo o multiplicador é 2,5
    - Para distancia de até 15 Km(quinze quilometros) o tempo de deslocamento se mantem em 2min(dois minutos) para distancias maiores de 15Km(quinze quilometros) o sofrem um acréscimo de 1 min(um minuto) por quilometro de distancia percorrida.

--- 

#### Regras de inferência

- SE distancia <= 15 ENTAO =tempo deslocamento 00:02 por Km
- SE distancia > 15 ENTAO =tempo deslocamento 00:03 por Km
- SE (horario >= 00:00 E horario < 05:00) E tempo bom ENTAO tempo deslocamento * 0,8
- SE ((horario >= 09:00 E horario < 17:00) OU (horario > 20:00 E horario < 00:00)) E tempo bom ENTAO tempo deslocamento * 1,0
- SE  (((horario >= 07:00 E horario =< 08:00)) OU ((horario >= 19:00 E horario =< 20:00))) E tempo bom ENTAO tempo deslocamento * 1,5
- SE ((horario >= 05:00 E horario < 07:00) OU (horario >= 17:00 E horario < 19:00)) E tempo bom ENTAO tempo deslocamento * 2,0
- SE (horario >= 00:00 E horario < 05:00) E tempo ruim ENTAO tempo deslocamento * 1,0
- SE ((horario >= 09:00 E horario < 17:00) OU (horario > 20:00 E horario < 00:00)) E tempo ruim ENTAO tempo deslocamento * 1,2
- SE (((horario >= 07:00 E horario =< 08:00)) OU ((horario >= 19:00 E horario =< 20:00))) E tempo ruim ENTAO tempo deslocamento * 2
- SE ((horario >= 05:00 E horario < 07:00) OU (horario >= 17:00 E horario < 19:00)) e tempo ruim ENTAO tempo deslocamento * 3
- SE ((horario >= 09:00 E horario < 17:00) OU (horario > 20:00 E horario < 00:00)) E tempo pessimo ENTAO tempo deslocamento * 2,5
- SE tempo pessimo ENTAO não entrega
- SE evento E evento pequeno (não tem bloqueios) ENTAO tempo deslocamEnto * 5,0
- SE evento E evento (tem bloqueios) ENTAO não entrega
