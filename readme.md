<img src="https://github.com/mareasea/gs-web/assets/136378912/0b0af4a1-55d6-415a-ba3a-4194c90dc2a7" width="220px">

# Next GPS

## VISÃO GERAL
Next GPS é um projeto inovador para rastreamento ao vivo de carros de corrida da Fórmula E. Utilizando tecnologia avançada, o sistema coleta e transmite dados de localização em tempo real, oferecendo informações valiosas sobre a performance dos veículos e permitindo que fãs e equipes acompanhem as corridas de forma interativa e envolvente.

## OBJETIVOS DO PROJETO
- **Rastreamento em Tempo Real:** Fornecer dados de localização precisos dos carros durante as corridas.
- **Análise de Desempenho:** Coletar informações sobre velocidade e desempenho dos veículos.
- **Integração com MQTT:** Facilitar a comunicação e transmissão de dados via MQTT para visualização em tempo real.
- **Geração de Mapas Interativos:** Criar mapas que mostram a posição atual dos carros usando a biblioteca Folium.

## TECNOLOGIAS UTILIZADAS
<a href="https://www.arduino.cc/" target="_blank"><img src="https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white&labelColor=black" alt="Arduino"></a>
<a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white&labelColor=black" alt="Python"></a>
<a href="https://www.eclipse.org/paho/clients/java/" target="_blank"><img src="https://img.shields.io/badge/MQTT-FFB030?style=for-the-badge&logo=MQTT&logoColor=white&labelColor=black" alt="MQTT"></a>


## ARQUITETURA DO PROJETO
<img src="https://github.com/user-attachments/assets/d42725de-b773-4011-8f6c-a506d7f9472f">



## MONTAGEM DO PROJETO
Para montar o sistema de rastreamento, siga os passos abaixo:

### Materiais Necessários
- **ESP32:** Microcontrolador para comunicação e processamento.
- **Módulo GPS:** Para obter dados de localização (ex: NEO-6M).
- **Sensor de Velocidade:** Opcional, para medir a velocidade do veículo.
- **Conexões:** Fios de conexão, protoboard, e resistores conforme necessário.

### Passo a Passo
1. **Conexão do Módulo GPS:**
   - Conecte os pinos TX e RX do módulo GPS aos pinos RX e TX do ESP32, respectivamente.
   - Conecte o pino de alimentação (VCC) e GND.

2. **Configuração do ESP32:**
   - Instale o Arduino IDE e adicione a placa ESP32.
   - Use as bibliotecas necessárias (`TinyGPS++`, `PubSubClient` para MQTT).

3. **Upload do Código:**
   - Escreva um código para capturar dados de localização e transmiti-los via MQTT.
   - Faça upload do código para o ESP32.

4. **Visualização de Dados:**
   - Configure um broker MQTT e um cliente para receber os dados.
   - Utilize a biblioteca Folium para criar mapas interativos com a posição dos carros.

## PARCEIROS
<div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-bottom: 20px;">
    <a href="https://www.grandepremio.com.br/" target="_blank">
        <img src="https://github.com/mareasea/gs-web/assets/136378912/87836721-5822-49e5-aaea-0414226b7c6c" width="100px" alt="Grande Prêmio">
    </a>
    <a href="https://www.fiap.com.br" target="_blank">
        <img src="https://github.com/mareasea/.github/assets/136378912/8eca5082-4fc2-417d-a5c6-2160af8069f3" width="150px" alt="FIAP">
    </a>
    <a href="https://www.mahindraracing.com/" target="_blank">
        <img src="https://github.com/mareasea/gs-web/assets/136378912/2a83e492-76ac-4717-8e2b-ff4eebaec570" width="150px" alt="Mahindra Racing">
    </a>
</div>

## COLABORADORES DO PROJETO
<div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
    <a href="https://github.com/AnaTorresLoureiro" target="_blank" style="text-align: center;">
        <img src="https://avatars.githubusercontent.com/AnaTorresLoureiro" width=120 alt="Ana Laura Torres Loureiro">
        <p>Ana Laura Torres Loureiro - RM 554375</p>
    </a>
    <a href="https://github.com/MuriloCngp" target="_blank" style="text-align: center;">
        <img src="https://avatars.githubusercontent.com/MuriloCngp" width=120 alt="Murilo Cordeiro Ferreira">
        <p>Murilo Cordeiro Ferreira - RM 556727</p>
    </a>
    <a href="https://github.com/MateusLem" target="_blank" style="text-align: center;">
        <img src="https://avatars.githubusercontent.com/MateusLem" width=120 alt="Mateus da Costa Leme">
        <p>Mateus da Costa Leme - RM 557803</p>
    </a>
    <a href="https://github.com/Geronimo-augusto" target="_blank" style="text-align: center;">
        <img src="https://avatars.githubusercontent.com/Geronimo-augusto" width=120 alt="Geronimo Augusto Nascimento Santos">
        <p>Geronimo Augusto Nascimento Santos - RM 557170</p>
    </a>
    <a href="https://github.com/Vitorr-AF" target="_blank" style="text-align: center;">
        <img src="https://avatars.githubusercontent.com/Vitorr-AF" width=120 alt="Vitor Augusto França de Oliveira">
        <p>Vitor Augusto França de Oliveira - RM 555469</p>
    </a>
</div>
