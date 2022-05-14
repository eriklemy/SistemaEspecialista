# SistemaEspecialista

### Sistema Especialista em Previsão de Tempo de Entrega

O sistema especialista em questão, irá identificar a possibilidade de atrasos em entregas e o tempo medio para a entrega ocorrer levando em conta fatores como: trânsito, clima, horários, datas e eventos próximos ao local de entrega.

Preve tempo de entrgas através de fatores, como:
    
- dia
- clima
- horario
- evento 
- feriado
- distancia
- Região (bloqueada ou nao)

---
### TODO: CHECAR COMO PODEMOS USAR OU SE SERA EXCLUIDO
- local ao qual sera enviado? (ainda não usado)
- epoca do ano (ainda não usado)
- tempo de entrega (para comparar com o calculado?)

---
Com estas informações há como objetivo identificar o grau de probabilidade de uma entrega ser efetuada em tempo.

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
- Feriado:
    - Alto fluxo rodoviario, então tem maior concentração de veiculos, resultando em tempos mais longos de entrega.

---
#### Regras:

- 0 <= horario <= 23:59hrs
- feriado local não conta 
- distancia da distribuidora até o comercio
- climas permitidos [CHUVA LEVE, CHUVA MODERADA, ENSOLARADO, NUBLADO, TEMPESTADE, NEBLINA]  

---

#### AINDA NAO USADO 
- grupo a ser distribuido (max = 5 prototipo)
- 0 < dias do mes <= 31, se dias mes > 30 -> será usado 30
- epoca do ano dentro das estações [OUTONO, INVERNO, PRIMAVERA, VERÃO] 
- regiões permitidas [NORTE, NORDESTE, SUL, SUDESTE, CENTRO-OESTE) da distribuidora

---
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

- [x] SE distancia <= 15 ENTAO tempo deslocamento = 2 mim por Km
- [x] SE distancia > 15 ENTAO tempo deslocamEto = 3 mim por Km
- [x] SE horario madrugueiro E tempo bom ENTAO tempo deslocamento * 0,8
- [x] SE horario fora de pico E tempo bom ENTAO tempo deslocamento * 1,0
- [x] SE horario de proximo de pico E tempo bom ENTAO tempo deslocamento * 1,5
- [x] SE horario de pico E tempo bom ENTAO tempo deslocamento * 2,0
- [x] SE horario madrugueiro E tempo ruim ENTAO tempo deslocamento * 1,0
- [x] SE horario fora de pico E tempo ruim ENTAO tempo deslocamento * 1,2
- [x] SE horario de proximo de pico E tempo ruim ENTAO tempo deslocamento * 2
- [x] SE horario de pico e tempo ruim ENTAO tempo deslocamento * 3
- [x] SE tempo pessimo ENTAO não entrega
- [x] SE evento E não bloqueado ENTAO tempo deslocamEnto * 5,0
- [x] SE evento e bloqueado ENTAO não entregua
