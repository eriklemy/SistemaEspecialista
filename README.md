# SistemaEspecialista

### Sistema Especialista em Previsão de Tempo de Entrega

O sistema especialista em questão, irá identificar a possibilidade de atrasos em entregas levando em conta fatores como: trânsito, clima, horários, datas e eventos próximos a local de entrega.

Preve tempo de entrgas através de fatores, como:
    
- dia
- clima
- horario
- epoca do ano
- feriado
- grupo ao qual sera distribuido? (pequeno ou grande comercio)
- Região
- distancia

Com estas informações há como objetivo identificar o grau de probabilidade de uma entrega ser efetuada em tempo.

---

#### Exemplo:

- Eventos:
    - Entregue mais proximas a evento como exemplos:
        - Podem ser canceladas devido a bloqueios de acessos devido aos mesmos.
        - Terão atrasos caso não tenha os bloqueios.

- Previsão Climática :
    - Os fatores climáticos podem ou não ter interferência.
         - se chover a entrega terá atrasos devido a possibilidade de aumentar o volume de veículos nas vias.
        - A entrega em um dia ensolarado não terá atrasos devido ao clima.
- Feriado:
    - Alto fluxo rodoviario, então tem maior concentração de veiculos, resultando em tempos mais longos de entrega.

---
#### Regras:

- dias do mes <= 31, se mes > 30 -> será usado 30
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
    - Para distancia de até 15 Km(quinze quilometros) o tempo de deslocamento se mantem em 2min(dois minutos) para distancias maiores de 15Km(quinze quilometros) o sofrem um acréscimo de 1 min(um minuto) por quilometro de distancia percorrida.

--- 

VERIFICAR AQUI SE TÁ CERTO


#### Regras de inferência 

- SE distancia <= 15 tempo deslocamento 2 mim por Km
- SE distancia > 15 = tempo deslocamto 3 mim por Km
- SE horario madrugueiro E tempo bom = tempo deslocamento * 0,8
- SE horario fora de pico E tempo bom = tempo deslocamento * 1,0
- SE horario de proximo de pico E tempo bom = tempo deslocamento * 1,5
- SE horario de pico E tempo bom = tempo deslocamento * 2,0
- SE horario madrugueiro E tempo ruim = tempo deslocamento * 1,0
- SE horario fora de pico E tempo ruim = tempo deslocamento * 1,2
- SE horario de proximo de pico E tempo ruim = tempo deslocamento * 2
- SE horario de pico e tempo ruim = tempo deslocamento * 3
- SE tempo pessimo = não entrega
- SE evento E não bloqueado = tempo deslocamnto * 5,0
- SE evento e bloqueado = não entregua
