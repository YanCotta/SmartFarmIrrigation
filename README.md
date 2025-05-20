# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="./assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# SmartFarmIrrigation

## Nome do grupo
AgroTech Innovators

## 👨‍🎓 Integrantes
- [Yan Cotta](https://www.linkedin.com/in/yan-cotta/)

## 👩‍🏫 Professores
### Tutor(a)
- Lucas Gomes Moreira

### Coordenador(a)
- André Godoi Chiovato

## 📝 Sobre o Projeto
O **SmartFarmIrrigation** é um sistema inteligente de irrigação desenvolvido para a FarmTech Solutions como parte do curso de Inteligência Artificial e Machine Learning da FIAP. Este projeto simula um sistema IoT (Internet das Coisas) que utiliza um microcontrolador ESP32 na plataforma Wokwi para coletar dados de sensores de umidade do solo, pH, fósforo e potássio, e controlar um relé para irrigação com base em condições ambientais e climáticas. O sistema foi projetado para otimizar o uso da água em fazendas, irrigando apenas quando necessário, considerando critérios como umidade do solo inferior a 50%, pH entre 6 e 7, presença de fósforo e potássio, e chuva recente inferior a 1mm.

Os dados coletados pelo ESP32 são armazenados em um banco de dados **SQLite**, visualizados em um dashboard interativo desenvolvido com **Streamlit** e ajustados por meio da integração com a **API OpenWeather**, que fornece informações sobre chuvas recentes. O projeto foi implementado utilizando **C++** para a programação do ESP32, **Python** para processamento, visualização e integração de APIs, e **SQL** para gerenciamento de dados. Ele atende a todos os requisitos do curso e incorpora os desafios "Ir Além" com a criação de um dashboard interativo e a integração com uma API pública.

A modelagem de dados segue o **Modelo Entidade-Relacionamento (MER)** simplificado da Fase 2, utilizando uma única tabela chamada `irrigation_data` para armazenar as leituras dos sensores e o estado da bomba de irrigação. Essa abordagem foi escolhida para garantir eficiência e simplicidade na simulação, mantendo a integridade dos dados e facilitando as operações CRUD (Create, Read, Update, Delete).

---

## 📸 Visualizações
![Simulação Wokwi](./assets/wokwi_simulation.PNG)  
*Simulação do ESP32 no Wokwi com sensores e relé.*  
![Dashboard Streamlit](./assets/streamlit_dashboard.pdf)  
*Dashboard interativo exibindo dados dos sensores.*  
![Integração Climática](./assets/openweather_functional_api.PNG)  
*Saída da integração com a API OpenWeather.*  

*(Imagens localizadas na pasta `assets`)*

---

## 📁 Estrutura de Pastas
```
.github/                 # Configurações do GitHub (e.g., workflows)
assets/                  # Imagens (logo FIAP, capturas de tela)
document/                # Documentação (ai_project_document_fiap.md, agora excluído)
scripts/                 # Scripts Python
├── database.py          # Criação e gerenciamento do banco SQLite
├── dashboard.py         # Dashboard interativo com Streamlit
├── weather_integration.py # Integração com a API OpenWeather
├── verify_db.py         # Script para verificar o banco de dados
├── requirements.txt     # Dependências Python
src/                     # Código-fonte C++ para ESP32
├── prog1.ino            # Código principal do ESP32
.pio/build/              # Arquivos de build do PlatformIO (ignorado no git)
.vscode/                 # Configurações do Visual Studio Code
diagram.json             # Configuração do circuito no Wokwi
platformio.ini           # Configuração do PlatformIO
wokwi.toml               # Configuração do Wokwi Simulator
.gitignore, .gitattributes # Arquivos de configuração do Git
README.md                # Este arquivo
```

---

## 🗃 Modelo Entidade-Relacionamento (MER)
O MER da Fase 2 foi projetado para atender às necessidades do sistema de irrigação inteligente. Para simplificar a simulação e otimizar o desempenho, optou-se por uma única tabela chamada `irrigation_data`, que armazena todas as informações relevantes. A estrutura da tabela é a seguinte:

- **id**: Chave primária, inteiro autoincrementado.
- **humidity**: Umidade do solo (float, em porcentagem).
- **ph**: Nível de pH do solo (float).
- **phosphorus**: Presença de fósforo (booleano, 0 ou 1).
- **potassium**: Presença de potássio (booleano, 0 ou 1).
- **pump_state**: Estado da bomba de irrigação (booleano, 0 ou 1).
- **timestamp**: Data e hora da leitura (texto, formato ISO).

Essa modelagem reflete uma abordagem prática e eficiente, eliminando a necessidade de múltiplas tabelas e relações complexas, já que o foco do projeto é a simulação e a análise de dados em tempo real.

---

## 📊 Entregáveis

### Entrega 1: Sistema de Sensores e Controle com ESP32
- **Circuito**: Implementado no Wokwi, configurado em `diagram.json`.
- **Código**: `src/prog1.ino` (C++), com lógica de irrigação comentada para facilitar a compreensão.
- **Funcionalidade**: Lê dados de sensores (umidade, pH, fósforo, potássio) e ativa o relé da bomba conforme condições predefinidas.
- **Documentação**: Detalhada neste README e ilustrada em `wokwi_simulation.png`.

### Entrega 2: Armazenamento de Dados em Banco SQL
- **Script**: `database.py` (Python), responsável pela criação da tabela `irrigation_data` e operações CRUD.
- **Verificação**: `verify_db.py` para validar a integridade dos dados inseridos.
- **MER**: Simplificado, conforme descrito na seção anterior, com justificativa para a escolha de uma única tabela.

---

## 🚀 Funcionalidades "Ir Além"

### Dashboard Interativo
- **Ferramenta**: Streamlit (`dashboard.py`).
- **Funcionalidades**: Exibição de gráficos (umidade ao longo do tempo), tabelas com leituras recentes, filtros interativos e indicação da decisão de irrigação.
- **Valor Agregado**: Permite monitoramento em tempo real e análise visual dos dados.

### Integração com API Pública
- **API**: OpenWeather (`weather_integration.py`).
- **Lógica**: Verifica a quantidade de chuva recente; se > 1mm, a irrigação é desativada, mesmo que outros critérios sejam atendidos.
- **Implementação**: Usa a chave de API configurável para consultar dados climáticos em tempo real.

---

## 🔧 Como Executar o Código

### Pré-requisitos
- **IDE**: Visual Studio Code com extensões PlatformIO e Wokwi Simulator.
- **Conta OpenWeather**: Crie uma conta em [https://openweathermap.org/](https://openweathermap.org/) para obter uma chave de API.
- **Bibliotecas C++**: Arduino, DHT (instaladas via PlatformIO).
- **Bibliotecas Python**: Streamlit, Pandas, Matplotlib, Requests (listadas em `requirements.txt`).
- **Versões Recomendadas**:
  - Python 3.9 ou superior.
  - PlatformIO 6.0 ou superior.
  - Wokwi CLI (opcional para automação).

### Passos para Instalação e Execução

#### 1. Clonar o Repositório
```bash
git clone https://github.com/YanCotta/SmartFarmIrrigation.git
cd SmartFarmIrrigation
```

#### 2. Configurar o Ambiente Python
```bash
pip install -r scripts/requirements.txt
streamlit --version  # Verifique a instalação do Streamlit
```

#### 3. Configurar a Chave da API OpenWeather
Edite o arquivo `scripts/weather_integration.py` e insira sua chave:
```python
API_KEY = "SUA_CHAVE_AQUI"
```

#### 4. Executar o Banco de Dados
```bash
python scripts/database.py  # Cria o banco e a tabela
python scripts/verify_db.py  # Verifica os dados inseridos
```

#### 5. Simular o ESP32 no Wokwi
- Abra o projeto no Visual Studio Code com a extensão PlatformIO instalada.
- Compile o código `src/prog1.ino`:
  ```bash
  pio run
  ```
- Execute a simulação no Wokwi:
  - Ajuste o sensor DHT22 para umidade < 50% (ex.: 45%).
  - Configure o LDR para simular pH entre 6 e 7 (~50% no slider).
  - Pressione os botões D18 (fósforo) e D19 (potássio).
  - Verifique o Serial Monitor para saídas como:
    ```
    Humidity: 45% | Phosphorus: 1 | Potassium: 1 | pH: 6.5 | Pump: 1
    ```

#### 6. Executar o Dashboard Streamlit
```bash
streamlit run scripts/dashboard.py
```
Acesse o dashboard em [http://localhost:8501](http://localhost:8501).

#### 7. Executar a Integração Climática
```bash
python scripts/weather_integration.py
```
Saída esperada: `Irrigate? Yes` (se chuva < 1mm) ou `Irrigate? No` (se chuva > 1mm).

#### 8. Testar o Fluxo Completo
- Simule dados no Wokwi.
- Insira os dados no banco com `database.py`.
- Visualize os resultados no dashboard.
- Ajuste a decisão de irrigação com base na integração climática.

---

## 🗃 Histórico de Lançamentos
- **1.0.0**: Projeto finalizado com simulação Wokwi, banco SQLite, dashboard e integração OpenWeather.
- **0.5.0**: Integração com a API OpenWeather concluída.
- **0.4.0**: Dashboard implementado com gráficos e tabelas interativas.
- **0.3.0**: Banco SQLite configurado com operações CRUD.
- **0.2.0**: Lógica de irrigação implementada no ESP32.
- **0.1.0**: Estrutura inicial do projeto e configuração do Wokwi.

---

## 📝 Conclusão e Trabalhos Futuros
O **SmartFarmIrrigation** é uma solução completa que integra hardware simulado, armazenamento de dados, visualização e inteligência climática para otimizar a irrigação em fazendas. O projeto atende aos objetivos pedagógicos da FIAP, demonstrando habilidades em IoT, programação, banco de dados e integração de APIs. Para o futuro, sugerem-se melhorias como a implementação de sensores físicos reais, o uso de machine learning para prever necessidades de irrigação e a expansão do sistema para múltiplas zonas de cultivo.

---

## 📋 Licença
<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>