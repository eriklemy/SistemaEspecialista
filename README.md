# Sistema Especialista

### Sistema Especialista em Previsão de Tempo de Entrega

O sistema especialista em questão, irá identificar o tempo de entrega considerando fatores como: trânsito, clima, horários e eventos próximos ao local de entrega.

Preve tempo de entrgas através de fatores, como:
- clima
- horario
- evento
- distancia

Com estas informações há como objetivo identificar o grau de probabilidade de uma entrega ser efetuada em um determinado tempo.

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
- distancia da distribuidora até o comercio
- climas permitidos [TEMPO BOM, TEWMPO RUIM E TEMPO PESSIMO]  
- Regras de multiplicador
    - para horario madrugueiro o multiplicador é 0,8
    - para transito fora de pico o multiplicador é de 1 
    - pra transito moderado próximo a horário de pico (tanto para mais ou para menos do horário) o multiplicador é 1,5
    - para horário de pico o multiplicador é 2
    - para horario madrugueiro com chuva o multiplicador é 1
    - para horario fora de pico em dia de chuva multiplicador 1,2
    - para horario próximo de pico com chuva o multiplicador é 2
    - para horario de pico com chuva o multiplicador é 3
    - Para distancia de até 15 Km(quinze quilometros) o tempo de deslocamento se mantem em 2min(dois minutos) para distancias maiores de 15Km(quinze quilometros) o sofrem um acréscimo de 1 min(um minuto) por quilometro de distancia percorrida.

--- 

#### Regras de inferência

- [x] SE distancia <= 15 ENTAO =tempo deslocamento 00:02 por Km
- [x] SE distancia > 15 ENTAO =tempo deslocamento 00:03 por Km
- [x] SE (horario > 00:00 E horario =< 05:00) E tempo bom ENTAO = tempo deslocamento * 0,8
- [x] SE ((horario > 09:00 OU horario =< 17:00) OU (horario > 20:00 OU horario =< 00:00)) E tempo bom ENTAO = tempo deslocamento * 1,0
- [x] SE  (((horario > 05:00 ou horario =< 06:00) OU (horario > 07:00 OU horario =< 08:00)) OU ((horario > 17:00 ou horario =< 18:00) OU (horario > 19:00 ou horario =< 20:00))) E tempo bom ENTAO = tempo deslocamento * 1,5
- [x] SE ((horario > 06:00 OU horario =< 07:00) OU (horario > 18:00 ou horario =< 19:00)) E tempo bom ENTAO tempo deslocamento * 2,0
- [x] SE (horario > 00:00 E horario =< 05:00) E = tempo ruim ENTAO tempo deslocamento * 1,0
- [x] SE ((horario > 09:00 OU horario =< 17:00) OU (horario > 20:00 OU horario =< 00:00)) E tempo ruim ENTAO = tempo deslocamento * 1,2
- [x] SE (((horario > 05:00 ou horario =< 06:00) OU (horario > 07:00 OU horario =< 08:00)) OU ((horario > 17:00 ou horario =< 18:00) OU (horario > 19:00 ou horario =< 20:00))) E tempo ruim ENTAO = tempo deslocamento * 2
- [x] SE ((horario > 06:00 OU horario =< 07:00) OU (horario > 18:00 ou horario =< 19:00)) e tempo ruim ENTAO = tempo deslocamento * 3
- [x] SE tempo pessimo ENTAO = não entrega
- [x] SE evento E evento pequeno ENTAO = tempo deslocamEnto * 5,0
- [x] SE evento E evento grande ENTAO = não entrega
