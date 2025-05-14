# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="./assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# SmartFarmIrrigation

## Nome do grupo

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/in/your-profile">Nome do integrante 1</a>
- <a href="https://www.linkedin.com/in/your-profile">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/in/your-profile">Nome do integrante 3</a>
- <a href="https://www.linkedin.com/in/your-profile">Nome do integrante 4</a>
- <a href="https://www.linkedin.com/in/your-profile">Nome do integrante 5</a>

## 👩‍🏫 Professores:
### Tutor(a)
- <a href="https://www.linkedin.com/in/tutor-profile">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/coordinator-profile">Nome do Coordenador</a>

## 📜 Descrição

O "SmartFarmIrrigation" é um sistema inteligente de irrigação desenvolvido para a FarmTech Solutions como parte do curso de Inteligência Artificial e Machine Learning da FIAP. Este projeto simula um sistema IoT que utiliza um ESP32 no Wokwi para coletar dados de sensores (umidade do solo, pH, fósforo e potássio) e controlar um relé para irrigação com base em condições ambientais e climáticas. Os dados são armazenados em um banco SQLite, visualizados em um dashboard interativo com Streamlit e ajustados por integração com a API OpenWeather, que considera a chuva recente.

O objetivo é otimizar o uso da água em fazendas, irrigando apenas quando necessário (umidade < 50%, pH entre 6-7, presença de nutrientes e chuva < 1mm). Desenvolvido com C++ (ESP32), Python (processamento e visualização) e SQL (armazenamento), o projeto reflete habilidades avançadas em IoT, integração de APIs e visualização de dados, alinhando-se ao MER simplificado da Fase 2 do curso.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **.github**: Arquivos de configuração específicos do GitHub.
- **assets**: Imagens e elementos não-estruturados (e.g., logo FIAP).
- **config**: Arquivos de configuração do projeto.
- **document**: Documentos do projeto, com subpasta "other" para itens complementares.
- **scripts**: Scripts Python para banco de dados, dashboard e integração climática.
- **src**: Código-fonte, com subpasta "esp32" para o código do ESP32.
- **README.md**: Guia geral do projeto.
- **wokwi.toml**: Configuração do Wokwi.
- **platformio.ini**: Configuração do PlatformIO.
- **diagram.json**: Placeholder para diagramas futuros.
- **.gitignore** e **.gitattributes**: Configurações Git.
- **.pio/build**: Diretório de build do PlatformIO.
- **.vscode**: Configurações do VS Code.

## 🔧 Como executar o código

### Pré-requisitos
- **IDE**: Visual Studio Code com extensões PlatformIO e Wokwi Simulator.
- **Serviços**: Conta no OpenWeather para obter uma chave API.
- **Bibliotecas C++**: Arduino, DHT (instaladas via PlatformIO).
- **Bibliotecas Python**: Listadas em `scripts/requirements.txt`.
- **Versões**: Python 3.9+, PlatformIO 6.0+, Wokwi CLI (opcional).

### Instalação e Execução
1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/your-username/SmartFarmIrrigation.git
   cd SmartFarmIrrigation

### Configure o ESP32:
- Abra o projeto no VS Code com PlatformIO.
- Compile e envie src/esp32/prog1.ino para o Wokwi via wokwi.toml.
- Simule no Wokwi (use o botão "Run Simulation").
- Instale Dependências Python:

```bash

Copy
pip install -r scripts/requirements.txt
```

### Configure a API OpenWeather:
- Substitua YOUR_API_KEY_HERE em scripts/weather_integration.py pela sua chave (obtenha em https://openweathermap.org/).

### Execute os Scripts:
- Banco de Dados: python scripts/database.py (gera irrigation.db).
- Dashboard: streamlit run scripts/dashboard.py.
- Integração Climática: python scripts/weather_integration.py.

### Teste o Fluxo:
- Simule o ESP32 no Wokwi, insira dados no banco via database.py, visualize no dashboard e ajuste com weather_integration.py.

## 🗃 Histórico de lançamentos
### 0.5.0 - XX/XX/2024
- Integração com OpenWeather API e ajustes finais.
### 0.4.0 - XX/XX/2024
- Dashboard Streamlit implementado.
### 0.3.0 - XX/XX/2024
- Banco de dados SQLite com CRUD.
### 0.2.0 - XX/XX/2024
- Lógica de irrigação no ESP32.
### 0.1.0 - XX/XX/2024
- Estrutura inicial e simulação Wokwi.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
